# Recursion = a function that calls itslef from within
# Step 1: divide a problem into minor ones
# Step 2: base condition determines when the recursive 
# function should stop calling itself and return a result
# Step 3: return answer to the base condition to solve all the subproblems

# Sum of all numbers. Iterative approach
def find_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i

# Recursive approach
def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n - 1)

# Fibonacci sequence. The recursive calls continue until the base case is reached, 
# where the function returns the Fibonacci number directly without making further recursive calls
def find_fib(n):
    if n == 0 or n ==1:
        return n
    return find_fib(n - 1) + find_fib(n - 2)

print(find_fib(6))

# How recursion call-stack works?
# 1. When the initial recursive function is called, a new frame is added to the call stack to represent that function call.
# 2. The function's parameters and local variables are stored in the frame of the call stack.
# 3. If the recursive function makes another recursive call within its execution, a new frame is added to the top of the call stack to represent the new function call.
# 4. The new frame contains its own set of parameters and local variables.
# 5. This process continues as long as there are recursive calls being made. Each new call adds a new frame to the top of the call stack.
# 6. When a base case is reached (a condition that stops the recursion), the function starts to return its results.
# 7. As each recursive call completes its execution and returns, its frame is removed from the call stack.
# 8. The function returns to the previous frame on the call stack and continues its execution from where it left off.
# 9. This process continues until all the frames are removed from the call stack, and the initial function call completes.