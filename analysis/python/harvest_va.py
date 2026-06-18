"""
harvest_va.py
-------------------------------------------------------------------------------
RUNG:     2 (post-processing)
PURPOSE:  Read SLiM/tree-sequence output across replicate founder draws and
          assemble the distribution of retained additive variance V_A'.
RECOVERS: mean(V_A') across replicates should match (1 - 1/2Ne) * V_A (Rung 1);
          among-replicate variance should fall toward 0 as L grows (Rung 2).

STATUS:   stub.

Annotated for both the expert and the newcomer: every step states what it
computes and why, so the pipeline doubles as a worked example.
"""

# import tskit, pyslim, numpy as np   # to be added
# def retained_additive_variance(...): ...
