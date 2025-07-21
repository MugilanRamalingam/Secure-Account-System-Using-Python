print("Welcome to my website")
c=int(input("Enter 1 for login and 2 for create a new account : "))
# Main mapping dictionary
oops = {
    'A': 'P', 'B': 'q', 'C': '5', 'D': 'O', 'E': '7', 'F': 'L', 'G': '9', 'H': 's', 'I': 'K', 'J': 'v',
    'K': 'X', 'L': '3', 'M': '8', 'N': 'n', 'O': 'a', 'P': 'E', 'Q': 'x', 'R': 'B', 'S': 'z', 'T': 'u',
    'U': 'Y', 'V': '0', 'W': 'J', 'X': 'A', 'Y': 'G', 'Z': '6', 'a': 'I', 'b': 'r', 'c': 'h', 'd': 't',
    'e': '2', 'f': 'b', 'g': 'R', 'h': 'd', 'i': 'F', 'j': 'y', 'k': 'H', 'l': 'U', 'm': 'c', 'n': '1',
    'o': 'Z', 'p': '4', 'q': 'f', 'r': 'V', 's': 'w', 't': 'C', 'u': 'M', 'v': 'Q', 'w': 'l', 'x': 'e',
    'y': 'g', 'z': 'D', '0': 'm', '1': 'j', '2': 'k', '3': 'T', '4': 'i', '5': 'W', '6': 'p', '7': 'S',
    '8': 'N', '9': 'o',"@":"&"," ":"#"
}

# Reverse mapping for decoding
reverse_oops = {v: k for k, v in oops.items()}

def encode(value):
    cne = ""
    for i in value:
        cne += oops[i]  # Strict: will raise KeyError if i not found
    return cne

def decode(value):
    cne = ""
    for i in value:
        cne += reverse_oops[i]  # Strict: will raise KeyError if i not found
    return cne



if c==1:
    user=input("User name :")
    user=encode(user)
    mail=input("User mailid :")
    mail=encode(mail)
    passw=input("Password :")
    passw=encode(passw)
    daa=user+"="+mail+"="+passw
    fil=user+".txt"
    a=open("database.txt","r")
    chec=a.read()
    check=chec.split("*")
    a.close()
    for i in check:
        if i==daa:
            bb=True
    if bb==True:

        b=open(fil,"r")
       
        ppp=decode(b.read())
        print("your Data : ")
        print("-----------------------------------------------------")
       
        b.close()
        print(ppp)
        print("-----------------------------------------------------")
        print("If you want to delete your data press 0 ")
        op=int(input(" If you want to add new data press 1 : "))
        if op==1:
            oo=open(fil,"a")
            ww=input("Enter your data : ")
            ww=encode(ww)
            oo.write(ww)
            oo.close()
        elif op==0:
             oo=open(fil,"w")
           
             oo.write("")
             oo.close()




elif c==2:
    name=input("Name : ")
    name=encode(name)
   
    mail=input("User mailid :")
    mail=encode(mail)
    pa=input("Create a new password : ")
    co=input("conform yout password : ")
    pa=encode(pa)
    co=encode(co)
    if pa==co:
        a=open("database.txt","a")
        daa=name+"="+mail+"="+pa
        a.write(daa)
        a.write("*")
        a.close()
        ww=input("Enter your Data : ")
        ww=encode(ww)
        fil=name+".txt"
        oo=open(fil,"a")
        oo.write(ww)
        oo.close()