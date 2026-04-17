# GsoC26-OmegaUp-Challenges

This repository contains algorithm problems I solved while preparing my application for **Google Summer of Code 2026** through **omegaUp**.

Even did not go through the full application process in order to prioritize startup work and university assignments, I wanted to publish the work as part of my learning journey and technical portfolio. Each problem was solved independently and then assisted with Cursor, which allowed comparing algorithms and learning new ways to solve a problem through Python code.

## Included Problems

- `GsoC - OmegaUp - Problem1 SelfMade.py`
- `GsoC - OmegaUp - Problem1 Cursor.py`
- `GsoC - OmegaUp - Problem2 SelfMade.py`
- `GsoC - OmegaUp - Problem2 Cursor.py`

## Problem 1 - Polyomino Placement

### What the problem asks

You are given:

- A polyomino shape represented as a matrix of `0` and `1`.
- A board represented as a matrix where occupied cells are non-zero and empty cells are `0`.

The task is to determine whether the polyomino can be placed on the board without overlapping occupied cells.

The piece can be transformed using:

- Rotations (`0`, `90`, `180`, `270` degrees)
- Horizontal flip

If at least one valid placement exists, print `YES`; otherwise print `IMPOSSIBLE`.

### What was implemented

- Extraction of polyomino blocks from the input matrix.
- Normalization of block coordinates to test placements consistently.
- Transformation logic for rotations and flip.
- Full search across all valid board positions for each transformation.

## Problem 2 - Grade Frequency by Course

### What the problem asks

You are given several courses, and each course includes a list of student grades represented by letters from `A` to `F`.

The task is to:

- Count how many times each grade (`A`, `B`, `C`, `D`, `E`, `F`) appears per course.
- Compute the overall totals across all courses.
- Print the per-course counts and final total in a fixed format.

### What was implemented

- Two versions for comparison: a self-made implementation and a Cursor-assisted implementation.
- Input parsing for multiple courses.
- Per-course frequency counting using a fixed-size counter array.
- Global accumulation of totals.
- Formatted output generation for each course and the final aggregate line.

## Why This Repository Exists

This repository represents consistency, growth, and practical problem-solving work done during my GSoC preparation process.
