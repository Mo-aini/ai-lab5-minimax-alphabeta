# Lab 5 - compare minimax and alpha-beta on the same tree
import math

try:
    from .lab5_minimax import minimax, minimax_counted, supplied_scores
    from .lab5_alphabeta import alphabeta, alphabeta_counted, SUPPLIED_AB_SCORES
except ImportError:                     # so it also runs as: python src/lab5_compare.py
    from lab5_minimax import minimax, minimax_counted, supplied_scores
    from lab5_alphabeta import alphabeta, alphabeta_counted, SUPPLIED_AB_SCORES

INF = float("inf")


def count_both(scores, depth):
    mc, mv = [0], []
    m = minimax_counted(0, 0, True, scores, depth, mc, mv)
    ac, av, cuts = [0], [], []
    a = alphabeta_counted(0, 0, True, scores, depth, -INF, INF, ac, av, cuts)
    return m, mc[0], a, ac[0], av, cuts


def swap_at(scores, depth, level, index):
    s = list(scores)
    span = 2 ** (depth - level)          # leaves under that node
    start = index * span
    half = span // 2
    s[start:start + half], s[start + half:start + span] = s[start + half:start + span], s[start:start + half]
    return s


def order_tree(scores, depth, best_first=True):
    def rec(lo, hi, d, maxTurn):
        if d == depth:
            return [scores[lo]], scores[lo]
        mid = (lo + hi) // 2
        l_leaves, l_val = rec(lo, mid, d + 1, not maxTurn)
        r_leaves, r_val = rec(mid, hi, d + 1, not maxTurn)
        left_better = (l_val >= r_val) if maxTurn else (l_val <= r_val)
        keep = left_better if best_first else not left_better
        leaves = l_leaves + r_leaves if keep else r_leaves + l_leaves
        return leaves, (max(l_val, r_val) if maxTurn else min(l_val, r_val))
    return rec(0, len(scores), 0, True)[0]


def report(title, scores, depth):
    m, mc, a, ac, av, cuts = count_both(scores, depth)
    print("%s" % title)
    print("  leaves: %s" % scores)
    print("  Minimax   : value %d, leaves evaluated %d" % (m, mc))
    print("  Alpha-Beta: value %d, leaves evaluated %d (evaluated leaf positions %s)" % (a, ac, av))
    for c in cuts:
        print("    cut: " + c)
    print("  values agree:", m == a)
    return m, mc, a, ac


def main():
    print("=" * 72)
    print("LAB 5 / Task 2  Leaf-evaluation counters on both algorithms")
    print("=" * 72)
    mm_scores, mm_depth = supplied_scores()
    ab_scores = list(SUPPLIED_AB_SCORES); ab_depth = int(math.log2(len(ab_scores)))
    rows = []
    rows.append(("Section 5.1 tree (padded)",) + report("Section 5.1 tree (Minimax driver):", mm_scores, mm_depth))
    print()
    rows.append(("Section 5.2 tree",) + report("Section 5.2 tree (Alpha-Beta driver):", ab_scores, ab_depth))
    print()
    print("Supplied functions called directly (reference check: same root value):")
    print("  5.1 tree: minimax =", minimax(0, 0, True, mm_scores, mm_depth),
          "| alphabeta =", alphabeta(0, 0, True, mm_scores, mm_depth, -INF, INF))
    print("  5.2 tree: minimax =", minimax(0, 0, True, ab_scores, ab_depth),
          "| alphabeta =", alphabeta(0, 0, True, ab_scores, ab_depth, -INF, INF))
    print()
    print("=" * 72)
    print("LAB 5 / Task 3  Branch reordering: pruning changes, value does not")
    print("=" * 72)
    for label, scores, depth in (("5.1 tree", mm_scores, mm_depth), ("5.2 tree", ab_scores, ab_depth)):
        variants = [
            ("original order", scores),
            ("swap root's two branches", swap_at(scores, depth, 0, 0)),
            ("swap children of left MIN node", swap_at(scores, depth, 1, 0)),
            ("swap children of right MIN node", swap_at(scores, depth, 1, 1)),
            ("best-first ordering (every node)", order_tree(scores, depth, True)),
            ("worst-first ordering (every node)", order_tree(scores, depth, False)),
        ]
        print("%s:" % label)
        print("  ordering | leaves | Minimax value | Alpha-Beta value | Minimax leaves | Alpha-Beta leaves | pruned")
        for name, s in variants:
            m, mc, a, ac, _, _ = count_both(s, depth)
            rows.append((label + ": " + name, m, mc, a, ac))
            print("  %s | %s | %d | %d | %d | %d | %d" % (name, s, m, a, mc, ac, mc - ac))
        print()
    print("Edge case: the padding value of the Section 5.1 driver changes the answer")
    print("  pad | leaves | Minimax value")
    for pad in (0, 99):
        s = [3, 5, 2, 9, 0, 7] + [pad] * 2
        print("  %d | %s | %d" % (pad, s, minimax(0, 0, True, s, 3)))
    print("  Without padding, the right MIN node has only the branch (0, 7), worth max(0, 7) = 7,")
    print("  so the real game value would be max(5, 7) = 7; the zero padding adds a fake MIN option worth 0.")


if __name__ == "__main__":
    main()
