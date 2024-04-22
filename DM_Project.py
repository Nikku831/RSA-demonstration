import random
import math

#check if prime
def ifPrime(y):
    for i in range(2,int(y**0.5)+1):
        if y%i==0:
            return 0
    return 1

def genPnum():
    x = random.randint(1000,1000000)        # generate random number
    if ifPrime(x)==1:
        return x
    else:
        return genPnum()

# generate the key elements
def genKey():
    p=genPnum()
    q=genPnum()
    while p==q:
        q=genPnum()
    n=p*q
    phi=(p-1)*(q-1) 
    for i in range(2,phi):
        if math.gcd(i,phi)==1:
            e = i
            break
    d = pow(e,-1, phi)
    return [n,e,d]

#user menu
def options():
    print("Options:\n\
        1 - Generate Key Pair\n\
        2 - Encrypt message \n\
        3 - Decrypt message \n\
        4 - Show whole process\n\
        5 - Exit\n")


while True:
    options()
    sel=input("Enter choice:")
    if sel=='1':
        n,e,d = genKey()
        print("\tPublic key pair =","(",n,",",e,")")
        print("\tPrivate key pair =","(",n,",",d,")")

    elif sel=='2':
        msg,c=[],[]
        n,e,d=genKey()
        O_msg = list(input("Enter message:"))
        
        for i in range(len(O_msg)):
            msg.append(ord(O_msg[i]))
        print("\tMessage data = ", msg)

        for i in msg:
            c.append(pow(i, e, n))
        print("\tEncrypted data = ", c,"\nPrivate keys are",'(',n,',',d,')',"\n(This is of the form (n,d) )\n!!!KEEP THIS DATA SAFE FOR DECRYPTION!!!")

    elif sel=='3':
        try:
            m,c,dec_msg=[],[],[]
            c1=input("Enter encrypted data values separated by spaces(no parenthesis):")
            c2=c1.split()
            for i in c2:
                c.append(int(i))
            n=int(input("Enter n value:"))
            d=int(input("Enter d value:"))
            for i in c:
                m.append(pow(i, d, n))
            for i in m:
                dec_msg.append(chr(i))
            print("\tOriginal Message Sent = ", "".join(dec_msg))
        except:
            print("Error encountered... Shutting down the system...")
            break


    elif sel=='4':
        n,e,d=genKey()
        print(f"Step 1...\n\tPublic Keys are ({n},{e})\n\tPrivate Keys are ({n},{d})")
        msg,c,m,dec_msg=[],[],[],[]
        print("Step 2...\n")
        O_msg = list(input("\tEnter message:"))
        for i in range(len(O_msg)):
            msg.append(ord(O_msg[i]))
        print("\tMessage data = ", msg)

        for i in msg:
            c.append(pow(i, e, n))
        print("\tEncrypted data = ", c,"\nStep 3...")
        for i in c:
            m.append(pow(i, d, n))
        for i in m:
            dec_msg.append(chr(i))
        print("\tOriginal Message Sent = ", "".join(dec_msg))
        print("\tData decrypted successfully...\nNow exiting!!")
    elif sel=='5':
        break
    else:
        print("Please enter valid choice!!")
