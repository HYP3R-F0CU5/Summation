n = int(input("n: "))
print("1.Arithmetic or 2.Geometric?")
choose = input()
if int(choose) != 1 and int(choose) != 2:
    print("Please choose 1 or 2")
    print("1.Arithmetic or 2.Geometric?")
    choose = input()
choose = int(choose)
if choose == 1:
    print("What is the common difference?")
    d = int(input("d: "))
    print("What is the first term of the series?")
    a = int(input("a: "))
    print((n/2) * ( (2*a) + d*(n-1) ) )
else:
    print("What is the common ratio?")
    r = int(input("r: "))
    print("What is the first term of the series")
    a = int(input("a: "))
    print((a*(1-r**n))/(1-r))
