
def loop_fact(n):
    result = 1
    for number in range(1,n):
        result = result*number
    return n*result

def fact(n):
    if n<=1:
        return 1
    return n * fact(n-1)

def main():
    my_n = int(input("what number shall we calculate factorial:"))
    result = fact(my_n)
    print(f"the result is {result}")

