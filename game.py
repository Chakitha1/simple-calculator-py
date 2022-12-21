a=input().split()
b=int(a[0])
c=int(a[2])
d=a[1]
if d=='+':
    print(b+c)
elif d=='-':
    print(b-c)
elif d=='*':
    print(b*c)
elif d=='/':
    print(b/c)
else:
    print(b%c)
    
#input can b sthng like '2+5'
