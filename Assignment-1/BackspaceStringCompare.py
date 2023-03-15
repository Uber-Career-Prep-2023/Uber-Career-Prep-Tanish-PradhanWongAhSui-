# uses two pointer technique, two arrays/strings
# time complexity O(n)
# space complexity O(n)
# no confusing edge cases. straightforward question, not vague
# what if it begins with a #?
# assuming neither string begins with a #
# took about 15 minutes

def back_space_compare(s1: str, s2: str) -> bool:
    a1 = []
    a2 = []
    for i in s1:
        if i == "#":
            if a1:
                a1.pop()
        else:
            a1.append(i)
    for i in s2:
        if i == "#":
            if a2:
                a2.pop()
        else:
            a2.append(i)
    return a2 == a1

print(back_space_compare("###", "#######"))
#True
print(back_space_compare("#", ""))
# True
print(back_space_compare("12309####", "##########2"))
# False
print(back_space_compare("12309####", "1##########1"))
#True
print("Given test cases:")
print(back_space_compare("Uber Career Prep", "u#Uber Careee#r Prep"))
# True
print(back_space_compare("abcde", "abcde"))
# True
print(back_space_compare("abcdef###xyz", "abcw#xyz"))
# True
print(back_space_compare("abcdef###xyz", "abcdefxyz###"))
# False
print(back_space_compare("", ""))
# True