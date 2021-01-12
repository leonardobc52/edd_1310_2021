""""def factorial( n ):
    if n == 0:
        resultado  1
    else:
        return factorial(n - 1) * n"""

def printRev( n ): #3
    if n > 0:
        printRev( n - 1) * n
        print( n )

def fibonacci( n ):
    if n == 1 or n == 0:
        return n
    if n > 1:
        return ( fibonacci(n-1) + fibonacci(n-2) )

def mai():
    for num in range(1,11,1):
        r = factorial(num)
        print(f"El factorial de {num} es {r}")
def main2():
    printRev( 3 )

def main3():
    for num in range(11):
        print(str(fibonacci(num)) + " , " , end="")
    pritn("")

main3()
