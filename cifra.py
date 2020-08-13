alfabeto = [chr(i) for i in range(97,97+26)]

def encrypt(string,cifra = 3):
    global encriptado
    encriptado=""
    print("Encriptando...")
    for i in string:
        if (i==" "):
            encriptado+=" "
        else:
            encriptado+= alfabeto[(ord(i)- 97 + cifra)%26]
    print("Encriptado = ",encriptado)

def decrypt(string, cifra = 3):
    global decriptado
    decriptado = ""
    print("Decriptando...")
    for i in string:
        if (i==" "):
            decriptado+=" "
        else:
            decriptado+=alfabeto[(ord(i) - 97 - cifra)%26]
    print("Decriptado = ",decriptado)
    
        
    


