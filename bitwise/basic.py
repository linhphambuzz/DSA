''' notes for bit wise operator '''

a,b= 23,24 
aa,bb=int(bin(a),2), int(bin(b),2)
#bin(a)='0b10111', bin(b)='0b11000' 

# 1. BITWISE AND : (a&b)=a x b 

mul=aa&bb #1&0=0 0&0=0 1&1=1  


#2. BITWISE OR: (a|b)=a+b-(axb)=a+b-(a&b) 

'''given 2 numbers, perform their sum without "+" operand''' 

sum=lambda x,y: (int(bin(x),2)|int(bin(y),2)) + (int(bin(x),2)&int(bin(y),2))
assert sum(5,2)== (5+2) 
assert sum(-8,-10)== (-8+-10) 

#3. BITWISE XOR: 1^0=1; 0^0=0; 1^1=0; 0^1=1 
#(a^b)=(a+b)%2 
xor=lambda x,y: (x and not y) or (y and not x) 

#4. BITWISE NOT: ~1=0 ; ~0=1 

#5. LEFT SHIFT: a<<n = ax (2^n); 
#shift bit to left by n, fill 0 to the right if necessary  

#6: RIGHT SHIFT: a>>n=a/ (2^n) 



'''     IMPORTANT: BITMASK          '''

#get bit at a given indx
def getbit(value,indx): 
    return value & (1<<indx)
import math 
assert getbit(0b1010,3)==math.pow(2,3)
assert getbit(0b1010,2)==0

def get_normalized_bit(value,indx): 
    return (value >> indx) & 1 
assert get_normalized_bit(0b1010,3)==1
assert get_normalized_bit(0b1010,2)==0
   
#set bit at a given indx
def setbit(value,indx):
    return value| (1<<indx)




