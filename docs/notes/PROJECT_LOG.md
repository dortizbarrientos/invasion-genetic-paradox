# Project log — decision record

A running record of design decisions, so the reasoning behind the code and the
manuscripts stays recoverable. Newest entries at the top.

---

## 2026-06-18 — Repository scaffolded

- Initialised repo and folder structure.
- Fixed the **recovery ladder** (Rungs 0–4c) as the organising spine; see README.
- Agreed scope: **two papers, one engine** — theory paper (Rungs 0–4b) and a
  perspective built on the accessibility-gated model (Rung 4c).
- **First deliverable defined:** Rungs 0–1 analytically + a two-knob SLiM design
  (number of loci L, effect-size tail) to harvest the distribution of retained
  V_A' across replicate founder draws. One figure decides whether the lottery
  switches on in a realistic regime.
- **Guardrail:** if SLiM does not reproduce the Rung 0–1 analytics exactly, the
  novel layer is not trusted. This is a stop condition, not a soft preference.

### Open questions to settle next
- Effect-size distribution for the tail knob: Gaussian vs. Laplace vs.
  Student-t (kurtosis lever)?
- Definition of "retained V_A'": measured in source environment, novel
  environment, or both (matters once Rung 4a lands)?
- N_e regime to scan for the lottery's on/off boundary.
