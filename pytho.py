# cook your dish here
t=int(input("Enter t"))
while(t):
    n=int(input("Enter n"))
    s=input("Enter s")
    d="YES"
    count=0
    for i in s:
        if(i!=['a','e','i','o','u']):
            count=count+1
        else:
            count=0
        if(count>=4):
            d="NO"
    t=t-1
    print(d)