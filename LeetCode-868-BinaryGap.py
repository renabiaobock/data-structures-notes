# My code without help
class MySolution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        hdict = {}
        max_distance = 0
        index = 0
        one_count = 0
        for digit in binary:
            if digit == '1':
                one_count += 1
                if one_count == 1:
                    hdict['f'] = index
                elif one_count == 2:
                    hdict['l']= index
                else:
                    hdict['f'] = hdict['l']
                    hdict['l'] = index
            index += 1
            if one_count > 1:
                distance = hdict['l'] - hdict['f']
                if distance > max_distance:
                    max_distance = distance
        return max_distance

# 0ms (beats 100%) / 17.86mb (beats 6.44%)

# Copied code from best solutions

class BestSolution:
    def binaryGap(self, n: int) -> int:
        answer = 0
        pre, current = inf, 0
        while n:
            if n & 1:
                answer = max(answer, current - pre)
                pre = current
            current += 1
            n >>= 1
        return answer

# 0ms (beats 100%) / 17.65mb (beats 6.44%)
