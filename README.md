# Collision Blocks π Simulation (3Blue1Brown Inspired)

This project reproduces the collision-based counting puzzle from the 3Blue1Brown video “The Most Unexpected Answer to a Counting Puzzle.”  
It simulates perfectly elastic collisions between two blocks, one next to a wall and one moving toward it.  
The number of collisions depends on the mass ratio and follows the digits of π.

The repository contains both the corrected version of the program and the original version that produced incorrect results.

---

## Files in this Repository

| File | Description |
|------|-------------|
| collision_fixed.py | Final, corrected simulation |
| collision_buggy.py | Original version before fixing the issue |
| TROUBLESHOOTING.md | Short explanation of the problem and the fix |


---

## Running the Program

You can run the simulation using:
python collision_fixed.py

After running, you will be asked to enter:
- the mass of the block near the wall  
- the mass of the block that is moving toward it

---

## Troubleshooting Summary

The first version of the program did not give the correct number of collisions for some mass inputs because of floating point rounding errors around zero.  
The solution was to add a small numerical tolerance (epsilon) to stabilize the stopping condition.  
A brief explanation is provided in `TROUBLESHOOTING.md`.

---

## Reference

This project is based on the explanation from the 3Blue1Brown video:  
“The Most Unexpected Answer to a Counting Puzzle.”
https://youtu.be/HEfHFsfGXjs

