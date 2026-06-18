# invasion-genetic-paradox

A theory-and-simulation study of when the loss of genetic diversity during
invasion **does** and **does not** blunt the response of a polygenic trait —
and what that implies for whether a founding population fails, naturalises, or
expands.

---

## The question

Invaders often carry depleted genetic variation, yet adapt with surprising
speed. This is the **genetic paradox of invasion**. The orthodox expectation is
that evolvability tracks diversity: lose variation, lose response. We ask under
what conditions that link **breaks** — specifically, when conditional gene
action (effects that switch on only in the novel environment, or are gated by
chromatin state) lets a founder recruit variation that the source range never
"needed", so that neutral diversity stops predicting adaptive potential.

The work is deliberately built as a **recovery ladder**: each model relaxes one
assumption, reproduces a known result, and only then reaches past it. The novel
claim earns trust only once the null — where diversity loss *does* blunt the
response — has been reproduced exactly.

---

## The recovery ladder

| Rung | Assumption set | Relaxes | Result to recover | Anchor |
|------|----------------|---------|-------------------|--------|
| **0** | Infinitesimal, additive, constant effects, infinite *N*, Gaussian stabilising selection, one optimum shift | — (base case) | Deterministic approach to optimum, rate ∝ *V*<sub>A</sub>; no paradox possible | Lande 1976 |
| **1** | Finite founders *N*<sub>e</sub> | Infinite population | *V*<sub>A</sub>′ = (1−*F*)*V*<sub>A</sub>, *F* = 1/2*N*<sub>e</sub>; diversity and evolvability fall together | Falconer & Mackay; Bürger & Lynch 1995 |
| **2** | Finite loci *L*, distribution of effect sizes | Infinitesimal limit | Retained *V*<sub>A</sub>′ becomes a random variable across founder draws; among-founder variance grows with effect-size kurtosis, shrinks with *L*. **The lottery is born here.** | Turelli & Barton |
| **3** | Demography + Allee threshold coupled to retained *V*<sub>A</sub> | Decoupled genetics/demography | Evolutionary rescue; trichotomy (fail / naturalise / invade) and a lag = time below the spread threshold | Gomulkiewicz & Holt 1995 |
| **4a** | Environment-conditional effects α<sub>i</sub>(*E*) | Constant effects | Release of cryptic variation in the novel environment | Hermisson & Wagner 2004; Paaby & Rockman 2014 |
| **4b** | Epistasis/dominance + drift | Strict additivity | Conversion of non-additive → additive variance; *V*<sub>A</sub>′ can transiently exceed *V*<sub>A</sub> | Goodnight 1988; Barton & Turelli 2004 |
| **4c** | Accessibility-gated effects (chromatin toggles expression *and* localises recombination; heat flips the gates) | — (novel instantiation) | None — this is the new model; ties theory to a measurable system | this study |

**Rungs 0–3** are the theory paper's backbone. **Rung 4c** is the spine of the
perspective. The paradox is *structurally impossible* below Rung 2: under
constant additive effects, lost diversity must blunt the response. That is the
bar everything else is measured against.

---

## Two papers, one engine

- **Theory paper** (target: *Genetics* / *TPB* / *Evolution*) — the full
  analytic + SLiM treatment, Rungs 0–4b, with the architecture-to-fate map.
- **Perspective** (target: *TREE* / *Evolutionary Applications*) — the
  conceptual map, the accessibility-gated model (4c), and the falsifiable
  **decoupling prediction**: under conditional effects, the correlation between
  neutral-marker diversity and realised adaptive response weakens toward zero.

---

## Falsifiable signatures (the guardrails against a just-so story)

1. **Decoupling (headline):** neutral diversity ↔ adaptive response correlation
   → 0 as conditional effects strengthen.
2. **Scaling:** variance in lag time across replicate invasions grows with
   effect-size kurtosis and shrinks with founder number, in the form Rung 2
   dictates.
3. **Threshold:** *P*(invade) depends on (*V*<sub>A</sub>, maladaptation) in the
   functional form rescue theory imposes — not a free fit.

If the simulations do not reproduce the Rung 0–1 analytics exactly, the creative
layer is not trusted and we stop.

---

## Repository layout

```
invasion-genetic-paradox/
├── docs/
│   ├── theory/        Analytical derivations, one file per rung (the "bar")
│   └── notes/         Working notes, decisions, reading
├── simulations/
│   ├── slim/          SLiM models (.slim), one per rung/experiment
│   └── config/        Parameter sets / sweep definitions (YAML/JSON)
├── analysis/
│   ├── R/             Post-processing, figures, statistics (annotated)
│   └── python/        pyslim / tskit pipelines, harvesting V_A' distributions
├── results/
│   ├── data/          Simulation output (git-ignored if large)
│   └── figures/       Generated figures
└── manuscript/
    ├── theory-paper/  Theory manuscript
    ├── perspective/   TREE / Evol. Appl. perspective
    └── shared/refs/   Shared bibliography
```

**Convention:** code is annotated for *both* the expert programmer and the
evolutionary biologist learning the method. Every script states, up top, which
rung it implements and which known result it must recover.

---

## First concrete deliverable

Build Rungs 0–1 analytically (`docs/theory/`), then a minimal SLiM design that
varies only two knobs — number of loci *L* and the effect-size tail — and
harvest the full distribution of retained *V*<sub>A</sub>′ across replicate
founder draws. One figure decides whether the lottery switches on in a realistic
regime or is a small-*N* curiosity, **before** any conditional-effects machinery
is built.

---

## Status

Scaffold only. See `docs/notes/PROJECT_LOG.md` for the running decision record.
