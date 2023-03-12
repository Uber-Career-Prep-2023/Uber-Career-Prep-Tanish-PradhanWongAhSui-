# Uses the two pointer technique for two arrays/strings
# Time complexity O(n), space complexity O(n)
# Took 20 minutes
def reverse_vowels(s: str) -> str:
    v_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    # slist = list(s)
    # vowels = ""
    # for i in range(len(slist)):
    #     if slist[i] in v_set:
    #         vowels += slist[i]
    #         slist[i] = "_"
    # j = len(vowels)-1
    # for i in range(len(slist)):
    #     if slist[i] == "_":
    #         slist[i] = vowels[j]
    #         j -= 1
    # return "".join(slist)

    i = 0
    j = len(s) - 1
    slist = list(s)
    while i < j:
        if slist[i] in v_set and slist[j] in v_set:
            slist[i], slist[j] = slist[j], slist[i]
            i += 1
            j -= 1
        elif slist[i] in v_set:
            j -= 1
        elif slist[j] in v_set:
            i += 1
        else:
            i += 1
            j -= 1
    return "".join(slist)


print(reverse_vowels("Uber Career Prep"))
# prints "eber Ceraer PrUp"
print(reverse_vowels("xyz"))
# prints "xyz"
print(reverse_vowels("flamingo"))
# prints "flominga"
print(reverse_vowels(("aaaooo")))
# oooaaa
print(reverse_vowels("TRNYplm"))
# TRNYplm
print(reverse_vowels(""))
print(reverse_vowels("tanish"))
# tinash
print(reverse_vowels("maaaaam"))
# maaaaam