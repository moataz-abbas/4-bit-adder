
def halfAdder(a, b):
        c = a and b
        s = a^b
        return c, s

def fullAdder(a, b, cin):
        s = cin^ (a^b)
        cout = (a and b) or (cin and (a^b))
        return cout, s
        

def fourBitAdder(a,b):
    n= len(a)
    out= [0]*(n+1)
    assert n == len(b), "numbers as not equal"
    
    for i in range(n-1,-1,-1):
        #print(f"i = {i}, n = {n}")
        if ( i == n-1):
            c, out[i+1] = halfAdder(a[i], b[i])
            #print(f"if {c}, {out[i]} = {a[i]}, {b[i]}")
        else:
            #print(f"{a[i]}, {b[i]}, {c}")
            c, out[i+1] = fullAdder(a[i], b[i], c)
            #print(f"else = {c}, {out[i]} ")
            
    out[0]= c
        
    return out



#while True:
#        
#        a=input("input a = ")
#        if( a == 'q'):
#            break
#        b=input("input b = ")
#        
#        
#        a= [int(i) for i in a]
#        b= [int(j) for j in b]
#        
#        
#        print(fourBitAdder(a,b))
