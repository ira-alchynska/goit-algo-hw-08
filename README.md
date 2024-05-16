# Cable Connection Cost Minimization

This program demonstrates how to minimize the cost of connecting network cables of various lengths using a min-heap.

## Problem Statement

Given several network cables of different lengths, they need to be combined two at a time into a single cable using connectors. The cost of connecting two cables is equal to the sum of their lengths, and the total cost is the sum of connecting all cables. The task is to find the order of combining the cables that results in the minimum total cost.

## Solution

The solution uses a min-heap to ensure the smallest lengths are always combined first, which minimizes the overall cost.

### Steps:

1. **Initial Cable Lengths:** [4, 3, 2, 6]
2. **Place them into a Min-Heap:** [2, 3, 4, 6]
3. **Extract the two smallest lengths:** 2 and 3. Combine them: 2 + 3 = 5. Total cost: 5. New state of the heap: [4, 5, 6]
4. **Extract the next two smallest lengths:** 4 and 5. Combine them: 4 + 5 = 9. Total cost: 5 + 9 = 14. New state of the heap: [6, 9]
5. **Extract the next two smallest lengths:** 6 and 9. Combine them: 6 + 9 = 15. Total cost: 14 + 15 = 29. New state of the heap: [15]
6. **Only one element left in the heap, algorithm completes.**

Thus, the minimum cost to connect the cables is 29.



