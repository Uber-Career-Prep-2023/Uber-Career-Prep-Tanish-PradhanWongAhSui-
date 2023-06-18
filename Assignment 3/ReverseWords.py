# Uses a stack 
# Time complexity - O(n)
# Space complexity - O(n)

def reversewords(line: str)-> str:
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
assert reversewords("Hello World") == "World Hello"
assert reversewords("   Hello   ") == "Hello"
assert reversewords("Hello    World") == "World Hello"
assert reversewords("Hello") == "Hello"
assert reversewords("!@#$%^&*()") == "!@#$%^&*()"
assert reversewords("123 456 789") == "789 456 123"

# took 16 minutes