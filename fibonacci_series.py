def fibonacci(n:int):
    prev = 0
    nex = 1
    
    print(nex)
    for cur in range(1,n):
        f_number = prev + nex
        prev = nex
        nex = f_number
        print(f_number)
        
        
n= int(input("Enter the length of the series:"))
fibonacci(n)