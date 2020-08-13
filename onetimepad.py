import random
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ','A','B','C','D','E','F','G','H','I']

def generate_key(size):
    string=""
    for i in range(size):
        string+=str(random.randint(0,1))
    return string

def conv_to_bin(num):
    binario = bin(num)[2:]
    while (len(binario)<5):
        binario='0'+binario
    return binario

def xor(str1,str2):
    str3=''
    for i in range(len(str1)):
        if (str1[i]==str2[i]):
            str3+='0'
        else:
            str3+='1'
    return str3

def encrypt(string):

    global key
    print("Gerando Key...")
    key=generate_key(len(string)*5)
    print("Key = ",key)
    print()
    
    global encriptado
    binario=''
    print("Convertendo",string,"para binário...")
    
    for i in string:
        if (i==' '):
            enc = 26
        else:
            enc= ord(i)-97
        binario += conv_to_bin(enc)

    print("Binário = ", binario)
    print()
    
    print("Encriptando...")
    encriptado=xor(binario,key)
    print("Encriptado = ",encriptado)

    print()
    print("Enviando: ",end='')
    msg=''
    for i in range(len(encriptado)//5):
        stri=encriptado[5*i:5*i+5]
        soma=0
        for i in range(5):
            soma+=2**i * int(stri[4-i])
        msg+=lista[soma]

    print(msg)
    
def decrypt(string, key):
    print("Decriptando...")
    decriptado = xor(string,key)
    print("Decriptado = ",decriptado)
    print()
    
    print("Convertendo para mensagem...")

    mensagem=''
    for i in range(len(decriptado)//5):
        stri=decriptado[5*i:5*i+5]
        soma=0
        for i in range(5):
            soma+=2**i * int(stri[4-i])
        mensagem+=lista[soma]
    print("Mensagem = " ,mensagem)
                
            
            
    
       
            
