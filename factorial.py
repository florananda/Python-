#N = int(raw_input())

fact = 1

if N< 0:
    fact=0
if N>1:   
    for i in range(1,N+1):
        fact = fact * i
    
print(fact)
