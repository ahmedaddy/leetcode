class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        res = [0] * n
        stack = []
        prev_time = 0
        for log in logs:
            l_id, state, timestamp = log.split(":")
            l_id, timestamp = int(l_id), int(timestamp)
            if state == "start":
                if stack:
                    res[stack[-1]] += timestamp - prev_time
                stack.append(l_id)
                prev_time = timestamp
            else:
                last = stack.pop(-1)
                print(timestamp, prev_time)
                res[last] += (timestamp - prev_time) + 1
                prev_time = timestamp + 1
        return res
