# AI discovery and assistant context

[Русский](ai-discovery.ru.md)

This guide covers two distinct uses: helping a coding assistant work correctly
inside a repository, and helping a retrieval/search assistant explain and cite
the software accurately. Both rely on factual, maintained documentation.

## Entry points

| Audience or client | Entry point | Scope |
|---|---|---|
| Codex and AGENTS-aware coding clients | AGENTS.md | Repository layout, development checks, architecture and editing constraints |
| Claude Code | Existing CLAUDE.md, or a pointer to AGENTS.md where no owner file exists | Client-loaded context; preserve repository-specific owner guidance |
| Qwen Code | QWEN.md pointing to AGENTS.md | Context for clients configured to read this file |
| Gemini CLI | GEMINI.md pointing to AGENTS.md | Context for clients configured to read this file |
| Other coding clients, including Grok-based integrations | Supply AGENTS.md through the host client's supported context mechanism | Do not assume every model or host automatically recognizes a filename |
| Perplexity, Grok search interfaces and other retrieval systems | Public README, overview/FAQ, source references, documentation site and curated llms.txt | Accessible evidence for answers; no guaranteed indexing or filename support |
| Readers without programming experience | docs/overview.md and the ecosystem catalog | What the software does, when to use it, what to supply and what a result means |

Instruction-file behavior belongs to a client/application, not to the underlying
model family alone. AGENTS.md does not itself make a repository discoverable in
web search. llms.txt is a proposed navigation convention, not a universal engine
directive. This project provides useful entry points without claiming that all
clients consume them.

## Content requirements

Each repository's overview should answer:

1. What problem does this package solve, and for whom?
2. Is it mathematics/cybernetics, reusable engineering, or application software?
3. What inputs does it need, and what outputs does it produce?
4. What can a reader do without writing application code?
5. What is implemented now, what is planned, and what is outside scope?
6. What assumptions or guarantee classifications apply?
7. Which existing example, schema or source file supports each capability?

Use descriptive headings, short self-contained answers and explicit package vs
import names. Preserve version/revision context when comparing behavior. Explain
conditional results and unsuccessful search, rather than showing only successes.
Do not place hidden instructions, manufactured authority, promotional rankings
or requests to ignore other sources in discoverable documentation.

## Publication and evaluation

Local files are preparation. Public discoverability requires publishing the
reviewed commit or documentation site and confirming that the intended URLs
are accessible. Where a site already exists, keep its build, navigation,
canonical URLs, sitemap and language metadata consistent. Do not add invented
site roots, fake crawler responses or broad robots rules to a repository that
does not serve a website.

After publication, evaluate a fixed set of questions with each relevant client:

- Which package monitors an industrial process, and does it control equipment?
- Which package supports forward/backward reasoning, and what rule system?
- What does a conditional proof mean?
- Does the agent example establish a statistical error bound for arbitrary LLM scores?
- What is the difference between game-model time and an operational scheduler?
- Can clinical currently recommend a patient's treatment, or does it monitor trials?
- Which package supplies portable read-only diagrams?
- Are markets and the engineering search wrapper implemented or reserved?

Record the date, exact question, client/interface, public source revision, cited
URLs and whether the answer matches source claims. Citation correctness and
coverage are meaningful measures; a promised recommendation position is not.
An unpublished or private source cannot be assumed accessible to a public engine.

## Primary references

- [AGENTS.md convention](https://agents.md/)
- [OpenAI Codex documentation](https://developers.openai.com/codex/)
- [Claude Code documentation](https://code.claude.com/docs/)
- [Qwen Code repository](https://github.com/QwenLM/qwen-code)
- [Gemini CLI repository](https://github.com/google-gemini/gemini-cli)
- [llms.txt proposal](https://llmstxt.org/)

Client behavior changes over time; consult the relevant client's current
documentation. These references are not endorsements or evidence of indexing.

See [the ecosystem specification](ecosystem-spec.md) and
[package catalog](ecosystem-catalog.md).
