# Uses the two pointer technique for two arrays/strings
# Time complexity O(n), space complexity O(n)
# Took 20 minutes
def reverse_vowels(s: str) -> str:
    v_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    slist = list(s)
    vowels = "";
    for i in range(len(slist)):
        if slist[i] in v_set:
            vowels += slist[i]
            slist[i] = "_"
print(reverse_vowels("Uber Career Prep"))
# prints "eber Ceraer PrUp"
print(reverse_vowels("xyz"))
# prints "xyz"
print(reverse_vowels("flamingo"))
# prints "flominga"