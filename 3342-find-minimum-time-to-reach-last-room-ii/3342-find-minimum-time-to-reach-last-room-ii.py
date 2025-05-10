import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        seen = set()
        # format of (time, x, y, take 1 -> True / False)
        heap = [(0, 0, 0, True)]

        R, C = len(moveTime) - 1, len(moveTime[0]) - 1

        while heap:
            time, x, y, take_one = heapq.heappop(heap)

            if x == R and y == C:
                return time
            
            if (x, y) in seen:
                continue
            seen.add((x, y))

            for dx, dy in directions:
                fx, fy = x + dx, y + dy
                if 0 <= fx <= R and 0 <= fy <= C:
                    to_add = 1 if take_one else 2
                    heapq.heappush(heap, (
                                max(time + to_add, moveTime[fx][fy] + to_add),
                                fx,
                                fy,
                                not take_one
                            ))
        