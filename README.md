# AI Lab 5 - Minimax and Alpha-Beta Pruning

Lab 5 for the AI lab course (CS4944). A hand trace of the manual tree with minimax, a counter for leaf evaluations in both algorithms, and a test of how branch order changes alpha-beta pruning.

## Files

- `main.py` runs everything
- `src/lab5_minimax.py` minimax from the manual (Section 5.1) plus the counter
- `src/lab5_alphabeta.py` alpha-beta from the manual (Section 5.2) plus the counter
- `src/lab5_compare.py` Task 3, the reordering test
- `outputs/output.txt` output of my run
- `report/Lab5_Report_Mohammed_Emad_ALaini.docx` the report

## How to run

Only Python 3 is needed, no extra packages.

```
python main.py
```

## Results

Task 1: the tree [3, 5, 2, 9, 0, 7] is padded by the manual code to [3, 5, 2, 9, 0, 7, 0, 0]. Depth 3, MAX at the root.

| Depth | Player | Values |
|-------|------|--------|
| 0 | MAX | 5 |
| 1 | MIN | 5, 0 |
| 2 | MAX | 5, 9, 7, 0 |
| 3 | leaves | 3, 5, 2, 9, 0, 7, 0, 0 |

Task 2, leaves evaluated:

| Tree | Value | Minimax | Alpha-Beta |
|------|-------|---------|------------|
| 5.1 [3,5,2,9,0,7,0,0] | 5 | 8 | 8 |
| 5.2 [3,5,2,9,3,5,2,9] | 5 | 8 | 6 |

Task 3, reordering the 5.2 tree:

| Order | Value | Alpha-Beta leaves |
|----------|-------|-------------------|
| original | 5 | 6 |
| swap children of right MIN node | 5 | 8 |
| best first at every node | 5 | 5 |
| worst first at every node | 5 | 8 |

The value stays 5 every time, only the pruning changes. Note: the zeros added by the padding act like real leaves. Without padding the value would be 7 (I explain this in the report).

In `alphabeta()` I only fixed the indentation so it runs in Python, the logic is the manual's.

## Author

Mohammed Emad ALaini

MIT License, see LICENSE.
