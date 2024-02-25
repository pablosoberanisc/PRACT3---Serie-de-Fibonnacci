def ImprimirFibonacci(n):
    fibonacci=[]
    a=0
    b=1

    for i in range (n):
        fibonacci.append(a)
        a,b=b,a+b




    return fibonacci

n=int(input("..."))
print (ImprimirFibonacci(n))


    


    

