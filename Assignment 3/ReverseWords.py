def reversewords(line: str)-> str:
    # Time - O(n), space - O(n)
    
    words = line.split()  
    stack = []
    
    for word in words:
        stack.append(word)  
    
    reversed_words = []
    while stack:
        reversed_words.append(stack.pop())  
    
    return ' '.join(reversed_words)

assert reversewords("Uber Career Prep") == "Prep Career Uber"
assert reversewords("Emma lives in Brooklyn, New York.") == "York. New Brooklyn, in lives Emma"
assert reversewords("") == ""
assert reversewords("hellothere") == "hellothere"

# took 10 minutes
