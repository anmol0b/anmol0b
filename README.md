# Hi, I'm Anmol 👋

Software engineer in India writing **Rust**, **Solana programs** and **AI agent tooling**.

Most of my open-source work is fixing bugs in AI agent tools: [OpenClaw](https://github.com/openclaw/openclaw), [Agent Orchestrator](https://github.com/OrchestratorInc/agent-orchestrator), [Orca](https://github.com/stablyai/orca) and [opencode](https://github.com/anomalyco/opencode).

## 🔧 What I'm building

**Systems**

- **[parkring](https://github.com/anmol0b/parkring)**: bounded MPMC channels and queues, a work-stealing deque and a thread pool for Rust. Futex parking, checked with loom, Miri, fuzzing and ThreadSanitizer.
- **[redis-rust](https://github.com/anmol0b/redis-rust)**: a Redis server in Rust.

**Solana**

- **[Trezo](https://github.com/Elyndor-Labs/Trezo-Ai)**: onchain treasury for SaaS companies.
- **[Sentinel](https://github.com/anmol0b/Sentinel)**: governance risk oracle for Solana DAOs.
- **[Harvester](https://github.com/anmol0b/Harvester)**: permissionless yield claimer for tokenized real-world assets.
- **[P-Speed](https://github.com/anmol0b/p-speed)**: live compute-unit benchmarks for P-Token (SIMD-0266).
- **[Solana Programs](https://github.com/anmol0b/turbine-builder-assignments-Q1)**: vaults, escrow, NFTs and an AMM.

**AI**

- **[AgentGauge](https://github.com/anmol0b/AgentGauge)**: benchmark AI coding agents on real bug-fix tasks from your own codebase, in Docker sandboxes, with pass rates, cost, latency and confidence intervals.
- **[Traceify](https://github.com/anmol0b/Traceify)**: chat with any public X profile, using RAG over their tweets.
- **[VoxAI](https://github.com/anmol0b/VoxAI)**: end-to-end voice assistant pipeline.
- **[TailorTalk](https://github.com/anmol0b/tailorTalk)**: AI calendar booking assistant.
- **[BhashaBazaar](https://github.com/anmol0b/BhashaBazaar)**: translation for Indic languages.

## 🦞 Open source

**[OpenClaw](https://github.com/openclaw/openclaw)**: fixes across the macOS app, Templates, Android, Talk and the Gateway. Selected:

- [#187000](https://github.com/openclaw/openclaw/pull/187000): the macOS app no longer quits with "Client credentials unavailable" after an in-place update
- [#186107](https://github.com/openclaw/openclaw/pull/186107): iMessage replies keep working after app updates, without re-granting Automation
- [#201428](https://github.com/openclaw/openclaw/pull/201428): configure and onboarding no longer save channel tokens as plaintext
- [#198803](https://github.com/openclaw/openclaw/pull/198803) / [#198727](https://github.com/openclaw/openclaw/pull/198727): an agent left behind by a blocked Template Add can be finished with Retry or resumed from the CLI
- [#183280](https://github.com/openclaw/openclaw/pull/183280): the macOS dashboard recovers after its web content process crashes
- [#187734](https://github.com/openclaw/openclaw/pull/187734) / [#187664](https://github.com/openclaw/openclaw/pull/187664): the macOS app keeps secrets and Gateway auth when a config save fails or Tailscale exposure is turned off
- [#192394](https://github.com/openclaw/openclaw/pull/192394) / [#194782](https://github.com/openclaw/openclaw/pull/194782): Android offers retry on a TLS timeout and stops reconnecting to a Gateway that never connected
- [#191950](https://github.com/openclaw/openclaw/pull/191950) / [#182919](https://github.com/openclaw/openclaw/pull/182919): Talk stops claiming cancelled work finished; the GPT-Live relay survives output arriving before mic input
- [Full list →](https://github.com/openclaw/openclaw/pulls?q=is%3Apr+author%3Aanmol0b+is%3Amerged)

**[Agent Orchestrator](https://github.com/OrchestratorInc/agent-orchestrator)**

- [#3153](https://github.com/OrchestratorInc/agent-orchestrator/pull/3153): reap a session's Docker containers when it reaches a terminal state
- [#3150](https://github.com/OrchestratorInc/agent-orchestrator/pull/3150): PR and review workflow actions in the command palette
- [#3700](https://github.com/OrchestratorInc/agent-orchestrator/pull/3700): detect a wedged updater network stack and nudge a restart
- [#3155](https://github.com/OrchestratorInc/agent-orchestrator/pull/3155) · [#3156](https://github.com/OrchestratorInc/agent-orchestrator/pull/3156) · [#2975](https://github.com/OrchestratorInc/agent-orchestrator/pull/2975) · [#2985](https://github.com/OrchestratorInc/agent-orchestrator/pull/2985) · [#3167](https://github.com/OrchestratorInc/agent-orchestrator/pull/3167): role-specific model config reaches Crush, Droid, Copilot, Kimi and agy

**[Orca](https://github.com/stablyai/orca)**

- [#38086](https://github.com/stablyai/orca/pull/38086): the CLI uses the terminal's worktree when cwd is outside every worktree
- [#33209](https://github.com/stablyai/orca/pull/33209): finish a worktree delete that Git left half-done on macOS and Linux
- [#33190](https://github.com/stablyai/orca/pull/33190): ACP agent exits report the exit code and signal, with stderr kept as a log detail
- [#31160](https://github.com/stablyai/orca/pull/31160): Copilot sessions show under their workspace, titled with the original prompt

**Elsewhere**

- [networking](https://github.com/cb7chaitanya/networking): TCP timestamps for RTT and PAWS ([#23](https://github.com/cb7chaitanya/networking/pull/23)), SYN backlog and SYN flood protection ([#18](https://github.com/cb7chaitanya/networking/pull/18))
- [opencode](https://github.com/anomalyco/opencode/pull/58144): contain plugin slots and routes that render bare text in the TUI
- [Paradev](https://github.com/ParadevAI/Paradev/pull/9492): bound the GitHub repository walk with one deadline
- [ossdotnow](https://github.com/collabute/ossdotnow/pull/167): project launch scheduling

**Merged PRs by project** (updated daily)

<!-- OSS:START -->
- [openclaw](https://github.com/openclaw/openclaw): 47 merged · 1 open
- [agent-orchestrator](https://github.com/OrchestratorInc/agent-orchestrator): 13 merged
- [orca](https://github.com/stablyai/orca): 6 merged · 2 open
- [networking](https://github.com/cb7chaitanya/networking): 3 merged · 1 open
- [ossdotnow](https://github.com/collabute/ossdotnow): 2 merged
- [opencode](https://github.com/anomalyco/opencode): 1 merged · 2 open
- [openclaw-enterprise](https://github.com/openclaw/openclaw-enterprise): 1 merged · 1 open
- [Paradev](https://github.com/ParadevAI/Paradev): 1 merged
<!-- OSS:END -->

## 📫 Links

[Website](https://anmol0b.xyz) · [Twitter](https://twitter.com/anmol0b) · [LinkedIn](https://www.linkedin.com/in/anmol0b/) · [Email](mailto:anmolbhardwajinv@gmail.com)
