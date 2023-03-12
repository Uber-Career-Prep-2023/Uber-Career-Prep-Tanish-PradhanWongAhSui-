# uses hashset technique to create a counter for each character in the string
# time complexity O(n)
# space complexity - worst case - all characters in string unique so O(n)
# took 15 minutes
def k_anagrams(k: int, s1: str, s2: str)-> bool:
    if len(s1) != len(s2):
        return False
    d = {}
    count = 0
    for i in s1:
        d[i] = d.get(i, 0) + 1
    for i in s2:
        if i in d:
            d[i] -= 1
            if d[i] == 0:
                del d[i]
        else:
            count += 1
    return count == k


print(k_anagrams(1, "apple", "peach"))
# False
print(k_anagrams(2, "apple", "peach"))
# True
print(k_anagrams(3, "cat", "dog"))
#True
print(k_anagrams(1, "debit curd", "bad credit"))
# True
print(k_anagrams(2, "baseball", "basketball"))
# False
print(k_anagrams(1, "dog", "god"))
# False
print(k_anagrams(0, "dog", "dog"))
# True