# what if there is no substring or if the length of the second string in input is greater than the first?
# return 0?

def shortest_substring(s1 : str, s2: str) -> int:
    p1 = 0
    min_length = len(s1)
    set1 = set(s2)
    while p1 < len(s1):
        if s1[p1] in set1:
            set1.remove(s1[p1])
            p2 = p1+1
            while p2 < len(s1):
                if s1[p2] in set1:
                    set1.remove(s1[p2])
                if len(set1) == 0:
                    break
            if len(set1) == 0 and min_length > (p2-p1):
                min_length = p2-p1
    return min_length


print(shortest_substring("abracadabra", "abc"))
# 4
print(shortest_substring("zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx"))
# 10
print(shortest_substring("dog", "god"))
# 3