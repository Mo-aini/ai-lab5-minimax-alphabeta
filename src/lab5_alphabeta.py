# Lab 5 - alpha-beta pruning (manual code) with a leaf counter
import math


# code from the manual (Section 5.2)
def alphabeta(depth, index, maxTurn, scores, target, alpha, beta):
    if depth == target:
        return scores[index]

    if maxTurn:
        value = float('-inf')
        for i in range(2):
            value = max(value, alphabeta(depth+1, index*2+i, False, scores, target, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for i in range(2):
            value = min(value, alphabeta(depth+1, index*2+i, True, scores, target, alpha, beta))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value


SUPPLIED_AB_SCORES = [3, 5, 2, 9, 3, 5, 2, 9]


# Task 2: count the leaf evaluations
def alphabeta_counted(depth, index, maxTurn, scores, target, alpha, beta, counter, visited=None, cuts=None):
    if depth == target:
        counter[0] += 1
        if visited is not None:
            visited.append(index)
        return scores[index]
    if maxTurn:
        value = float('-inf')
        for i in range(2):
            value = max(value, alphabeta_counted(depth + 1, index * 2 + i, False, scores, target, alpha, beta, counter, visited, cuts))
            alpha = max(alpha, value)
            if alpha >= beta:
                if cuts is not None and i == 0:
                    cuts.append("MAX node (depth %d, index %d): alpha=%s >= beta=%s, right child pruned" % (depth, index, alpha, beta))
                break
        return value
    else:
        value = float('inf')
        for i in range(2):
            value = min(value, alphabeta_counted(depth + 1, index * 2 + i, True, scores, target, alpha, beta, counter, visited, cuts))
            beta = min(beta, value)
            if alpha >= beta:
                if cuts is not None and i == 0:
                    cuts.append("MIN node (depth %d, index %d): alpha=%s >= beta=%s, right child pruned" % (depth, index, alpha, beta))
                break
        return value


def main():
    print("=" * 72)
    print("LAB 5 / Section 5.2  Alpha-Beta on the supplied scores")
    print("=" * 72)
    scores = list(SUPPLIED_AB_SCORES)
    depth = int(math.log2(len(scores)))
    print("scores =", scores, "| depth =", depth)
    print(alphabeta(0, 0, True, scores, depth, float('-inf'), float('inf')))


if __name__ == "__main__":
    main()
