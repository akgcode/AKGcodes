Q5
import hashlib
given= '1001001110010010110111011011010110110101110101001010001001110001110110110000100111111110111000101101011011100010110011111100011110001110011100110011110100110110111011101110110000011001111101011101101000001111111111100010110100010101110110001111110001100111'
#first converting decimal to integer and then to hexadecimal
print("Hex of given binary",hex(int(given,2)))
list={"Mechanical Engineering", "Electrical Engineering","Electronics Engineering","Chemical Engineering"}
#finding SHA256 code of each department
for x in list:
    x=x.encode()
    print(x,"----",hashlib.sha256(x).hexdigest())
print (2**20)

Q7
import hashlib
c=0 # counter variable to ocunt 2 nos
for i in range(2**20):
    
    HASH1= hashlib.sha256(str(i).encode()).hexdigest()

    for j in range(i+1,2**20):
        HASH2= hashlib.sha256(str(j).encode()).hexdigest()
        if(HASH1[-5:] == HASH2[-5:]):
            print(i,j)
            c=c+1
            break
        if(c==2): 
            break