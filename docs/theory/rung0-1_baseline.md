# Rungs 0–1: The deterministic null and the founder bottleneck

> **Purpose.** Fix the bar. Before any claim about the paradox, reproduce the
> standard results that say diversity loss *should* blunt the polygenic
> response. Nothing below is novel — and that is the point.

---

## Rung 0 — Deterministic null (Lande 1976)

**Assumptions.** Infinitesimal model; strictly additive, constant effects;
infinite population; Gaussian stabilising selection about an optimum; a single
shift of the optimum by Δθ at *t* = 0.

**Result to recover.** Exponential approach of the mean phenotype to the new
optimum, with a rate set by the additive variance.

*(Derivation to be written: mean-phenotype dynamics, time constant τ, the
explicit statement that with infinite N no variation is lost and therefore no
paradox can arise. Annotated for both the mathematician and the biologist.)*

---

## Rung 1 — Founder bottleneck (Falconer & Mackay; Bürger & Lynch 1995)

**Assumptions.** As Rung 0, but a finite number of founders draws an effective
size *N*<sub>e</sub>; effects remain additive and constant.

**Result to recover.** Additive variance erodes with inbreeding,
*V*<sub>A</sub>′ = (1 − *F*)·*V*<sub>A</sub> with *F* = 1/(2*N*<sub>e</sub>), so
the response slows in lockstep with heterozygosity. Diversity and evolvability
move **together** — the orthodox, paradox-free world.

*(Derivation to be written: expectation over founder sampling, the per-locus
2pq term, why the expectation alone hides the lottery that appears at Rung 2.)*

---

## What this buys us

A quantitative bar. Any later model that claims diversity loss leaves the
response intact must be shown to *depart* from these results — and the SLiM
implementation must reproduce them exactly before it is trusted to explore
beyond them.
