x = float(input("Enter the value x: "))
n = int(input("Enter the value n: "))
s = 1
term = 1
for i in range(1,n+1):
    term = term * (x/i)
    s=s+term
print(s)