# Troubleshooting the Collision Blocks Simulation

This file explains the problem encountered in the original simulation and how it was fixed.

---

## The Problem

The program simulates elastic collisions between two blocks to count the total number of collisions. Initially, the code produced incorrect results for some inputs. For example:

- Input: m1 = 1, m2 = 1  
- Expected collisions: 3  
- Original output: 0  

The simulation stopped early, producing wrong counts, especially for small or equal masses.

---

## Cause

The issue was due to floating point rounding errors. Velocities that should have been exactly zero appeared as tiny positive or negative numbers. The stopping condition relied on exact comparisons, so the program incorrectly thought the simulation was finished.

---

## The Fix

A small tolerance value (eps = 1e-12) was added. Velocities within ±eps of zero are treated as zero. The stopping condition and wall collision checks were updated:

```python
eps = 1e-12

if v1 > -eps and v2 > -eps and v2 >= v1 - eps:
    break

if v1 < -eps:
    v1 = -v1
    count += 1
    continue
```
This prevents early termination caused by tiny rounding errors, ensuring the simulation continues until no further collisions can physically occur.

## Result
After the fix, the simulation correctly counts collisions for all tested mass ratios. The corrected version is in collision_fixed.py, while the original version is preserved in collision_buggy.py for reference.
