# Technique: Dynamic programming
# Time complexity: O(n^3)
# Space complexity: O(n)

def wordBreak(s, wordDict):
    wordDict = set([x.lower() for x in wordDict])
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
                
    return dp[n]

# Test Cases
dictionary = ["Elf", "Go", "Golf", "Man", "Manatee", "Not", "Note", "Pig", "Quip", "Tee", "Teen"]
assert wordBreak("mangolf", dictionary) == True
assert wordBreak("manateenotelf", dictionary) == True
assert wordBreak("quipig", dictionary) == False
assert wordBreak("teegolf", dictionary) == True
assert wordBreak("note", dictionary) == True
assert wordBreak("", dictionary) == True
assert wordBreak("g", dictionary) == False
assert wordBreak("manman", dictionary) == True
assert wordBreak("golftee", dictionary) == True
assert wordBreak("nottee", dictionary) == True
assert wordBreak("teetee", dictionary) == True
assert wordBreak("elfman", dictionary) == True
assert wordBreak("manelf", dictionary) == True
assert wordBreak("elfelfelf", dictionary) == True
assert wordBreak("manateemanatee", dictionary) == True
assert wordBreak("quipquip", dictionary) == True
assert wordBreak("golfnotegolfnote", dictionary) == True
assert wordBreak("abcdef", dictionary) == False
assert wordBreak("manateepig", dictionary) == True
assert wordBreak("pigmanatee", dictionary) == True
assert wordBreak("pigelf", dictionary) == True
assert wordBreak("manateeelfpig", dictionary) == True
assert wordBreak("a" * 100 + "manatee", dictionary) == False


# Approximate time taken: 31 minutes.
