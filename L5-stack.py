# List implementation of the stack (not recomended)
s = []
s.append('https://www.cnn.com/')
s.append('https://www.cnn.com/world/')
s.append('https://www.cnn.com/europe/')
# The pop func returns the last element and deletes it
print(s.pop())
print(s)
# Indexing does not remove the last element 
print(s[-1])
print(s)

from collections import deque

# Deque collection (recomended, as they are 
# implemented with doubly linked lists, 
# you do not have to copy)
stack = deque()
stack.append('https://www.cnn.com/')
stack.append('https://www.cnn.com/world/')
stack.append('https://www.cnn.com/europe/')
print(stack.pop())

class Stack():
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
def reverse(string: str):
    stack = Stack()
    for i in string.split(' '):
        stack.push(i)
    rstr = ''
    while stack.size()!=0:
        rstr += ' ' + stack.pop()
    return rstr

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced(string):
    stack = Stack()
    for ch in string:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0
    
if __name__ == '__main__':
    print(reverse("Hello World Today"))
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))