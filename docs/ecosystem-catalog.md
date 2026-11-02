# Sequentialist package catalog

[Русский](ecosystem-catalog.ru.md)

The ecosystem has three logical layers and two naming families. sequential-*
contains mathematics, cybernetics and abstractions of algorithms. sequentialist-*
contains reusable software engineering and application software.

| Package | Layer | Current role |
|---|---|---|
| [sequential-analysis](https://github.com/andre-a-no/sequential-analysis) | Methods | Sequential statistical inference, filtering, forecasting and declared procedure guarantees |
| [sequential-search](https://github.com/andre-a-no/sequential-search) | Methods | Experiment contracts, state envelopes and finite forward/backward/bidirectional implication reasoning in the development checkout |
| [sequential-games](https://github.com/andre-a-no/sequential-games) | Methods | Explicit-state stochastic interaction and virtual-time reference simulation in the development checkout |
| [sequentialist-core](https://github.com/andre-a-no/sequentialist-core) | Engineering | Application specs, durable tasks, storage, replay, audit and reports |
| [sequentialist-visuals](https://github.com/andre-a-no/sequentialist-visuals) | Engineering | Standalone read-only HTML/SVG search and event views in the development checkout |
| [sequentialist-search](https://github.com/andre-a-no/sequentialist-search) | Engineering, reserved | No implementation yet; the responsibility of a future search application wrapper remains a design decision |
| [sequentialist-agentic](https://github.com/andre-a-no/sequentialist-agentic) | Application | Tool-agent example, cited retrieval and trusted-rule geometry example; new reasoning needs a compatible development checkout |
| [sequentialist-ab](https://github.com/andre-a-no/sequentialist-ab) | Application | Experiment assignment, sequential A/B analysis and audited decisions |
| [sequentialist-quality](https://github.com/andre-a-no/sequentialist-quality) | Application | Sequential acceptance sampling, inspection schemes and disposition records |
| [sequentialist-monitor](https://github.com/andre-a-no/sequentialist-monitor) | Application | Advisory equipment/process monitoring and alarm management; no automatic process control claim |
| [sequentialist-clinical](https://github.com/andre-a-no/sequentialist-clinical) | Application | Interim clinical-trial monitoring and reports; not patient treatment selection |
| [sequentialist-markets](https://github.com/andre-a-no/sequentialist-markets) | Application, reserved | No implementation yet; risk/backtest/strategy monitoring is planned scope |

Release/mlops applications and engineering messengers/connectors are mentioned
as future scope in family documents. Their repositories were not accessible at
the documented addresses during this preparation; this is not a statement that
they cannot exist privately or under another name.

## How to choose without reading code

- Use analysis when the central question is what can be inferred from a stream.
- Use search when the central question is which inference or branch to explore.
- Use games when other participants and the environment change the situation
  while a participant chooses or waits.
- Use core to make an application durable and auditable.
- Use visuals to inspect or share the result without altering its meaning.
- Use a domain package when it already models your subject and workflow.

These choices compose. An industrial diagnostic application might use monitor
for observations, search for diagnostic alternatives and core for audit. That
composition is a target architecture, not a claim that diagnosis is already
implemented in monitor.

New work described as a development checkout may be absent from released tags
or the public default branch until it is published. Always check the relevant
repository revision and dependency pins before relying on a new API.

See [the full specification](ecosystem-spec.md),
[AI discovery guide](ai-discovery.md) and [core overview](overview.md).
