#!/usr/bin/env python3
"""
Numerical illustration of the accessibility -> recombination -> diversity model.

This is not a schematic: every curve is computed from the equations in the
note, so the figure doubles as a check that the model recovers the two
load-bearing results — (i) crossover redistribution is EXACTLY zero-sum under
homeostasis, and (ii) the sign of the diversity change matches the sign of the
local opening relative to the genome-wide mean.

Light theme throughout (no dark backgrounds).
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams.update({
    "font.family": "serif", "font.size": 10, "axes.linewidth": 0.6,
    "figure.facecolor": "white", "axes.facecolor": "white",
    "savefig.facecolor": "white",
})

AMBER, GRAY, TEAL, BAND = "#BA7517", "#888780", "#0F6E56", "#F4D9A8"

# --- genome coordinate -------------------------------------------------------
x = np.linspace(0.0, 1.0, 4000)
dx = x[1] - x[0]

def gauss(mu, sd, amp):
    return amp * np.exp(-(x - mu) ** 2 / (2 * sd ** 2))

# --- control accessibility a0(x): baseline + three open peaks ----------------
a0 = 0.20 + gauss(0.25, 0.045, 1.0) + gauss(0.55, 0.045, 0.6) + gauss(0.80, 0.045, 0.9)

# --- heat opens the middle region (0.55) more than the genome-wide average ---
a1 = a0 + gauss(0.55, 0.045, 1.5)          # delta a concentrated at one region

# --- homeostasis: total crossovers fixed -> map = R * (a / integral a) -------
R = 1.0
A0, A1 = np.trapezoid(a0, x), np.trapezoid(a1, x)
p0, p1 = a0 / A0, a1 / A1                   # normalised placement densities
r0, r1 = R * p0, R * p1                     # recombination maps
dr = r1 - r0                               # redistribution

# CHECK 1: redistribution is zero-sum (integral of dr ~ 0) --------------------
zero_sum = np.trapezoid(dr, x)
print(f"[check 1] integral of delta-r (should be ~0): {zero_sum:.3e}")

# CHECK 2: sign of dr matches sign of (g - <g>_p), g = da/a -------------------
g = (a1 - a0) / a0
g_mean = np.trapezoid(p0 * g, x)               # accessibility-weighted mean opening
pred_sign = np.sign(g - g_mean)
got_sign = np.sign(dr)
agree = np.mean(pred_sign[np.abs(dr) > 1e-6] == got_sign[np.abs(dr) > 1e-6])
print(f"[check 2] sign(delta-r) == sign(g - <g>): {agree*100:.1f}% of informative sites")

# --- diversity under linked selection: pi = pi0 * B(r), B increasing ---------
# illustrative recurrent-sweep / BGS-type kernel, monotone increasing in r
rbar = np.trapezoid(r0, x)                      # mean map density for normalisation
beta = 0.45
B = lambda r: np.exp(-beta * rbar / r)
pi0 = 1.0
pi_c, pi_h = pi0 * B(r0), pi0 * B(r1)

# CHECK 3: sign of delta-pi matches sign of delta-r --------------------------
dpi = pi_h - pi_c
agree_pi = np.mean(np.sign(dpi)[np.abs(dr) > 1e-6] == got_sign[np.abs(dr) > 1e-6])
print(f"[check 3] sign(delta-pi) == sign(delta-r): {agree_pi*100:.1f}% of informative sites")

# ============================== plot =========================================
fig, ax = plt.subplots(3, 1, figsize=(6.6, 6.4), sharex=True)
opened = (x > 0.47) & (x < 0.63)
for a in ax:
    a.axvspan(0.47, 0.63, color=BAND, alpha=0.45, lw=0)
    a.spines[["top", "right"]].set_visible(False)
    a.set_yticks([])

# Panel A: accessibility, control vs heat
ax[0].plot(x, a0, color=GRAY, lw=1.6, label="control")
ax[0].plot(x, a1, color=AMBER, lw=2.0, label="heat")
ax[0].set_ylabel("accessibility\n$a(x)$")
ax[0].legend(frameon=False, loc="upper right", fontsize=9)

# Panel B: redistribution of crossovers (zero-sum)
ax[1].axhline(0, color="#B4B2A9", lw=0.8)
ax[1].fill_between(x, 0, dr, where=dr > 0, color=AMBER, alpha=0.85, lw=0)
ax[1].fill_between(x, 0, dr, where=dr < 0, color=GRAY, alpha=0.55, lw=0)
ax[1].set_ylabel("change in\nrecombination\n$\\Delta r(x)$")
ax[1].text(0.55, ax[1].get_ylim()[1]*0.72, "+", ha="center", color=AMBER, fontsize=15)
ax[1].text(0.02, ax[1].get_ylim()[0]*0.7,
           r"$\int \Delta r\,dx = 0$", fontsize=9, color="#5F5E5A")

# Panel C: diversity, control vs heat
ax[2].plot(x, pi_c, color=GRAY, lw=1.4, ls=(0, (4, 3)), label="before")
ax[2].plot(x, pi_h, color=TEAL, lw=2.0, label="after (long run)")
ax[2].set_ylabel("diversity\n$\\pi(x)$")
ax[2].set_xlabel("genome coordinate $x$")
ax[2].legend(frameon=False, loc="upper right", fontsize=9)
ax[2].annotate("", xy=(0.55, pi_h[np.argmin(np.abs(x-0.55))]),
               xytext=(0.55, pi_c[np.argmin(np.abs(x-0.55))]),
               arrowprops=dict(arrowstyle="-|>", color=TEAL, lw=1.4))

fig.align_ylabels(ax)
fig.tight_layout(h_pad=0.8)
fig.savefig("kelp-theory-note/model_illustration.pdf", bbox_inches="tight")
fig.savefig("kelp-theory-note/model_illustration.png", dpi=150, bbox_inches="tight")
print("saved model_illustration.pdf / .png")
