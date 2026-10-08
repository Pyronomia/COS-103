def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

from functools import wraps

# Define the logging decorator
def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"-> Calling {func.__name__}() with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"<- {func.__name__}() finished and returned: {result}\n")
        return result
    return wrapper


# Attach the decorator to functions you want to track
@log_call
def add_numbers(a, b):
    return a + b

@log_call
def greet_user(name, title="Developer"):
    return f"Welcome aboard, {title} {name}!"


# Try it out
if __name__ == "__main__":
    add_numbers(10, 25)
    greet_user("Alex", title="Lead")

def solve(pegs, n, visited=None, path=None):
    visited = visited if visited is not None else set()
    path = path if path is not None else []
    goal = list(range(n, 0, -1))
    if pegs[1] == goal or pegs[2] == goal:
        return path
    visited.add(tuple(map(tuple, pegs)))
    for src in range(3):
        for dst in range(3):
            if src == dst or not pegs[src]:
                continue
            if pegs[dst] and pegs[dst][-1] < pegs[src][-1]:
                continue                      # bigger disk onto smaller: illegal
            pegs[dst].append(pegs[src].pop()) # try the move
            if tuple(map(tuple, pegs)) not in visited:
                result = solve(pegs, n, visited, path + [(src, dst)])
                if result is not None:
                    return result
            pegs[src].append(pegs[dst].pop()) # undo the move
    return None

print(solve([[4,3, 2, 1], [], []],4))    

def hanoi(n, start, end, spare):
    if n == 0:
        return
    hanoi(n - 1, start, spare, end)
    print("move disk", n, "from", start, "to", end)
    hanoi(n - 1, spare, end, start)

hanoi(3, "A", "C", "B")