#With the help of ChatGPT for better time constraint
from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        rows = len(classroom)
        cols = len(classroom[0])
        litter = {}
        litter_count = 0
        start_row = 0
        start_col = 0

        for r in range(rows):
            for c in range(cols):
                if classroom[r][c] == "S":
                    start_row = r
                    start_col = c
                elif classroom[r][c] == "L":
                    litter[(r, c)] = litter_count
                    litter_count += 1

        if litter_count == 0:
            return 0

        all_collected = (1 << litter_count) - 1
        queue = deque()
        queue.append((start_row, start_col, 0, energy, 0))
        visited = {}
        visited[(start_row, start_col, 0)] = energy

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            row, col, mask, current_energy, moves = queue.popleft()
            if current_energy == 0:
                continue
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                if (new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols):
                    continue
                if classroom[new_row][new_col] == "X":
                    continue

                new_energy = current_energy - 1
                new_mask = mask

                if classroom[new_row][new_col] == "L":
                    index = litter[(new_row, new_col)]
                    new_mask = new_mask | (1 << index)

                if new_mask == all_collected:
                    return moves + 1

                if classroom[new_row][new_col] == "R":
                    new_energy = energy

                state = (new_row, new_col, new_mask)
                if (state not in visited or new_energy > visited[state]):
                    visited[state] = new_energy
                    queue.append((new_row, new_col, new_mask, new_energy, moves + 1))
        return -1


my_solution = Solution()
print(my_solution.minMoves(classroom = ["S.", "XL"], energy = 2))    #Output: 2
print(my_solution.minMoves(classroom = ["LS", "RL"], energy = 4))    #Output: 3
print(my_solution.minMoves(classroom = ["L.S", "RXL"], energy = 3))    #Output: -1