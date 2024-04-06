class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        d = {}
        for i in logs:
            birth, death = i
            for year in range(birth, death):
                if year not in d:
                    d[year] = 1
                else:
                    d[year] += 1
        max_population = max(d.values())
        m = [year for year, population in d.items() if population == max_population]

        return min(m)
