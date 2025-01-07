#happy nmber

num=int(input("num :"))
def happy_num(n):
    past = set()
    while n!=1:
        n = sum(int(i)**2 for i in str(n))
        if n in past :
            return false
    past.add
    return true
print(happy_num(num))
