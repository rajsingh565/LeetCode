class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervals, seen = [], set()
        
        # make intervals
        for i in range(len(s)):
            if s[i] not in seen:
                intervals.append([i, s.rfind(s[i])])
                seen.add(s[i])
        
        # merge intervals
        i = 1
        while i < len(intervals):
            if intervals[i][0] < intervals[i-1][1]:
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
                intervals.pop(i)
            else: i += 1

        return [i[1] - i[0] + 1 for i in intervals]