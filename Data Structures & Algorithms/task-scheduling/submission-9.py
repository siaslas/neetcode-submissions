class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t = 0

        freq, cooldown = Counter(tasks), []
        freq = [[-count, letter] for letter, count in freq.items()]
        heapq.heapify(freq)

        while freq or cooldown:
            while cooldown and cooldown[0][0] <= t:
                heapq.heappush(freq, [cooldown[0][1], cooldown[0][2]])
                heapq.heappop(cooldown)
            
            if not freq:
                t = cooldown[0][0]
                heapq.heappush(freq, [cooldown[0][1], cooldown[0][2]])
                heapq.heappop(cooldown)

            count, letter = heapq.heappop(freq)
            count += 1

            if count == 0:
                t += 1 
                continue

            start_time = t + n + 1
            heapq.heappush(cooldown, [start_time, count, letter])

            t += 1
    
        return t 





