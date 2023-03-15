# what if there is no substring or if the length of the second string in input is greater than the first?
# return 0?
# spent 35 minutes on this
# uses two pointer variable size sliding window technique and hashmap
# O(n) space complexity O(n) time complexity as we traverse s1 only once
from collections import Counter
import math
def shortest_substring(s1: str, s2: str) -> int:
    if len(s2) > len(s1):
        return 0
    if len(s2) == 0 or len(s1) == 0:
        return 0
    p1 = 0
    p2 = 0
    counter = Counter(s2)
    r_count = len(s2)
    min_len = math.inf
    # print(counter)
    while p2 <= len(s1):
        # print("Counter within while:", counter)
        # print("r_count", r_count, " and current substring is:", s1[p1:p2+1])
        while r_count == 0:
            # print("performing min len check. min_len is: ", min_len, "p2-p1: ",p2-p1)
            min_len = min(min_len, p2-p1)
            if s1[p1] in counter:
                counter[s1[p1]] += 1
                if counter[s1[p1]] > 0:
                    r_count += 1
            p1 += 1
        if p2 < len(s1):
            if s1[p2] in counter:
                counter[s1[p2]] -= 1
                if counter[s1[p2]] >= 0:
                    r_count -= 1
        p2 += 1
    if min_len == math.inf:
        return 0
    return min_len


print(shortest_substring("abracadabra", "abc"))
# 4
print(shortest_substring("zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx"))
# 10
print(shortest_substring("dog", "god"))
# 3
print(shortest_substring("d", "i"))
# 0
print(shortest_substring("asdf", "g"))
# 0
print(shortest_substring("as", "dfgh"))
# 0
print(shortest_substring("goddess", "oe"))
# 4
print(shortest_substring("goddess", "dd"))
# 2
print(shortest_substring("goddess", "gs"))
# 6
print(shortest_substring("goddess", "ss"))
# 2
print(shortest_substring("", ""))
# 0
