def Fibonacci(n): 
    if n<0: 
        print("Incorrect input. Input isn't negative!") 
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
    
fib_30 = []
for i in range(1, 31):
    fib_30.append(Fibonacci(i))

num = int(input("Number: "))  
print(Fibonacci(num))

print("\nFirst 30 Fibonacci Number")
print("Count - Fib")
for count, i in enumerate(fib_30, 1):
    print(count,"------", i)