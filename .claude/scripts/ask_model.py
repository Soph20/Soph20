#!/usr/bin/env python3
"""Send a prompt to any OpenAI-compatible chat endpoint and print the reply.

Works with OpenAI, OpenRouter, Groq, Together and local Ollama: they all speak
the same /chat/completions format. Standard library only, no installs.

Usage:
  git diff | ask_model.py "Review this diff for bugs"
  ask_model.py --model qwen/qwen3-coder --base-url https://openrouter.ai/api/v1 "..."

Config (flags override env vars):
  SECOND_OPINION_BASE_URL  default https://api.openai.com/v1
  SECOND_OPINION_MODEL     default gpt-5.5
  SECOND_OPINION_API_KEY   falls back to OPENAI_API_KEY, then a dummy value
                           (Claude Code cloud sessions inject the real key via proxy)
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

SYSTEM = (
    "You are an independent senior reviewer giving a second opinion to another AI. "
    "Be concrete and skeptical. For each issue give: location, what breaks, why, and a fix. "
    "Say 'No significant issues' if that is the truth. Do not pad."
)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("prompt", help="Instruction for the model. Stdin, if piped, is appended as context.")
    p.add_argument("--model", default=os.environ.get("SECOND_OPINION_MODEL", "gpt-5.5"))
    p.add_argument("--base-url", default=os.environ.get("SECOND_OPINION_BASE_URL", "https://api.openai.com/v1"))
    p.add_argument("--system", default=SYSTEM)
    p.add_argument("--timeout", type=int, default=300)
    a = p.parse_args()

    context = "" if sys.stdin.isatty() else sys.stdin.read()
    user = a.prompt + (f"\n\n<context>\n{context}\n</context>" if context.strip() else "")
    key = os.environ.get("SECOND_OPINION_API_KEY") or os.environ.get("OPENAI_API_KEY") or "sk-dummy"

    body = json.dumps({
        "model": a.model,
        "messages": [{"role": "system", "content": a.system}, {"role": "user", "content": user}],
    }).encode()
    req = urllib.request.Request(
        a.base_url.rstrip("/") + "/chat/completions",
        data=body,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=a.timeout) as r:
            data = json.load(r)
    except urllib.error.HTTPError as e:
        print(f"[ask_model] HTTP {e.code} from {a.base_url} ({a.model}): {e.read().decode()[:500]}", file=sys.stderr)
        return 1
    except urllib.error.URLError as e:
        print(f"[ask_model] cannot reach {a.base_url}: {e.reason}", file=sys.stderr)
        return 1

    print(f"[model: {data.get('model', a.model)}]")
    print(data["choices"][0]["message"]["content"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
