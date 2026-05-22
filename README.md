# Hi, I'm Soph 👋

Currently working on **Promix** — an AI-native workforce. Mnemos, HoliPet, and Vantx run on top of it.

## My stack
![Claude Code](https://img.shields.io/badge/Claude_Code-1e293b?style=flat-square&logo=anthropic&logoColor=white) ![MCP](https://img.shields.io/badge/MCP-Protocol-1e293b?style=flat-square&logoColor=white) ![Python](https://img.shields.io/badge/Python-1e293b?style=flat-square&logo=python&logoColor=white) ![TypeScript](https://img.shields.io/badge/TypeScript-1e293b?style=flat-square&logo=typescript&logoColor=white) ![Claude API](https://img.shields.io/badge/Claude_API-1e293b?style=flat-square&logo=anthropic&logoColor=white) ![ChatGPT](https://img.shields.io/badge/ChatGPT-1e293b?style=flat-square&logo=openai&logoColor=white) ![Gemini](https://img.shields.io/badge/Gemini-1e293b?style=flat-square&logo=googlegemini&logoColor=white) ![Cursor](https://img.shields.io/badge/Cursor-1e293b?style=flat-square&logo=cursor&logoColor=white) ![Lovable](https://img.shields.io/badge/Lovable-1e293b?style=flat-square&logoColor=white) ![NotebookLM](https://img.shields.io/badge/NotebookLM-1e293b?style=flat-square&logo=google&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-1e293b?style=flat-square&logo=openai&logoColor=white) ![SQL](https://img.shields.io/badge/SQL-1e293b?style=flat-square&logo=postgresql&logoColor=white) ![Figma](https://img.shields.io/badge/Figma-1e293b?style=flat-square&logo=figma&logoColor=white) ![Linear](https://img.shields.io/badge/Linear-1e293b?style=flat-square&logo=linear&logoColor=white) ![Jira](https://img.shields.io/badge/Jira-1e293b?style=flat-square&logo=jira&logoColor=white) ![Notion](https://img.shields.io/badge/Notion-1e293b?style=flat-square&logo=notion&logoColor=white) ![Supabase](https://img.shields.io/badge/Supabase-1e293b?style=flat-square&logo=supabase&logoColor=white) ![Vercel](https://img.shields.io/badge/Vercel-1e293b?style=flat-square&logo=vercel&logoColor=white) ![Google Stitch](https://img.shields.io/badge/Google_Stitch-1e293b?style=flat-square&logo=google&logoColor=white) ![Perplexity](https://img.shields.io/badge/Perplexity-1e293b?style=flat-square&logo=perplexity&logoColor=white) ![Jupyter](https://img.shields.io/badge/Jupyter-1e293b?style=flat-square&logo=jupyter&logoColor=white)

## What I work on

- **AI agent orchestration**: multi-agent teams, sequential workflows, constitutional rules, quality gates, institutional memory
- **Agentic developer tools**: Claude Code skills, CODEX, MCP integrations, scheduled tasks, capture-to-workflow pipelines
- **AI deployment patterns**: how to structure agents, handle failure modes, manage context, evaluate outputs
- **Product + engineering**: seven years shipping APIs, delivery tooling, and platforms at scale — I build what I spec

## What I'm building

- **[Mnemos](https://github.com/Soph20/mnemos-capture)** — A knowledge pipeline for agentic workflows. Paste any resource — articles, threads, transcripts, ideas — and an LLM extracts the insight, tags it, and commits it to a GitHub repo you own. Your AI agents pull from it via MCP or Git. Built with Haiku 4.5, prompt caching, and BYOK — costs under $1/month. [Live](https://mnemos-capture.vercel.app).

- **Promix OS** — An agentic workforce runtime: 16 specialized agents with hard role boundaries, 121 reusable skills, quality gates with standardized verdicts, and institutional memory across sessions. Runs inside Claude Code *or* standalone — its own CLI, daemon, MCP server, multi-provider router (Claude, OpenAI, Gemini), and web dashboard. Architecture is deliberately thin — the IP lives in the prompts and skills, not the runtime — because the right bet is that models keep improving. Powers the three products on this page.

- **[HoliPet](https://app.holipet.io/auth)** — All-in-one pet care platform for: food subscriptions, vet booking, services, and payments in one place. The interesting part is the routing layer. Every free-text message in four languages (EN/ES/IT/NL) hits a two-tier classification system — but the tiers aren't symmetric. Tier 1 is deterministic: a multilingual distress-keyword dictionary plus sentence-transformer embeddings (cosine ≥ 0.90) catches SOS intents before any LLM runs. That was a deliberate architectural choice — for a safety-critical intent, you don't want a probabilistic model as your first line. Tier 2 routes everything else through a locally hosted Llama 3 70B; local inference was a conscious call for data privacy and cost control, not a default. Evaluation uses a labeled ground-truth set scored with semantic similarity — next iteration layers in per-class F1 and a confusion matrix, with SOS recall weighted highest because false negatives aren't symmetric. [More information](https://holipet.lovable.app/)

## About me

Seven years shipping at scale — APIs, delivery tooling, platforms. Trilingual (ES/EN/FR). I learn by building: every system above exists because I hit the problem myself and couldn't find the right tool. 

Quoted in [Forbes Centroamérica](https://forbescentroamerica.com/2025/07/17/pettech-una-industria-que-crece-y-representa-nuevas-oportunidades-de-negocio-en-latinoamerica/) as founder of HoliPet on the LATAM pet tech market.
