#Fib series (user input)
fib = [0, 1]
n = int(input())

if n<=0:
    print("Enter valid term  number")
elif n<3:
    print("Term is: "+str(fib[n-1]))
else:
    for i in range (n-2):
        fib.append(fib[i]+fib[i+1])
    print("Term is: "+str(fib[n-1]))

    
