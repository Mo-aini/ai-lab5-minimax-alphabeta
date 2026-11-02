# Lab 5 - minimax (manual code) with a leaf counter
import math

# code from the manual (Section 5.1)
# Maximizing player can get
def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    # Base case: targetDepth reached
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        return max(
            minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)
        )
    else:
        return min(
            minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
        )


def supplied_scores():
    scores = [3, 5, 2, 9, 0, 7]
    treeDepth = math.ceil(math.log2(len(scores)))
    # Pad scores to make a complete binary tree
    scores += [0] * (2**treeDepth - len(scores))
    return scores, treeDepth


# Task 2: count the leaf evaluations
def minimax_counted(curDepth, nodeIndex, maxTurn, scores, targetDepth, counter, visited=None):
    if curDepth == targetDepth:
        counter[0] += 1
        if visited is not None:
            visited.append(nodeIndex)
        return scores[nodeIndex]
    left = minimax_counted(curDepth + 1, nodeIndex * 2, not maxTurn, scores, targetDepth, counter, visited)
    right = minimax_counted(curDepth + 1, nodeIndex * 2 + 1, not maxTurn, scores, targetDepth, counter, visited)
    return max(left, right) if maxTurn else min(left, right)


def node_values(scores, depth):
    levels = [list(scores)]
    for d in range(depth - 1, -1, -1):
        maxTurn = (d % 2 == 0)              # root (depth 0) is MAX, players alternate
        below = levels[0]
        cur = [max(below[2 * i], below[2 * i + 1]) if maxTurn else min(below[2 * i], below[2 * i + 1])
               for i in range(len(below) // 2)]
        levels.insert(0, cur)
    return levels


def main():
    print("=" * 72)
    print("LAB 5 / Section 5.1 + Task 1  Minimax on the supplied tree")
    print("=" * 72)
    scores, treeDepth = supplied_scores()
    print("scores after padding:", scores, "| treeDepth =", treeDepth)
    print("The optimal value is:", end=" ")
    print(minimax(0, 0, True, scores, treeDepth))
    print()
    print("Bottom-up values (check for the hand trace):")
    levels = node_values(scores, treeDepth)
    for d, vals in enumerate(levels):
        role = "leaves" if d == treeDepth else ("MAX" if d % 2 == 0 else "MIN")
        print("  depth %d (%s): %s" % (d, role, vals))
    c = [0]
    v = minimax_counted(0, 0, True, scores, treeDepth, c)
    print("minimax_counted -> value %d, leaves evaluated %d of %d" % (v, c[0], len(scores)))


if __name__ == "__main__":
    main()
