import sys
#Se define el arreglo que nos permitirá cifrar y descifrar el mensaje
keyMatrix = "ENCRYPTABDFGHIKLMOQSUVWXZ"
#Se almacena la opción de lo que se va a hacer
key = sys.stdin.readline()
key=key[:-1]
index=""
indexX=""
indexY=""
if key == "ENCRYPT":
    message = sys.stdin.readline()  #Se lee el mensaje
    message = message[:-1].replace(" ","")
    for a in message:               #Se forma el arreglo de indices
        indexX += str(keyMatrix.index(a)//5)
        indexY += str(keyMatrix.index(a)%5)
    index = indexX + indexY         #Se concatenan los indices
    matrix=[]
    cipher=""
    #Como se está manejando un arreglo para definir la matriz utilizamos la siguiente forma
    #para poder encontrar el mapeo de cada carácter del mensaje.
    for a in range(len(message)):
        matrix=([index[2*a],index[(2*a)+1]])
        cipher+=keyMatrix[5*int(matrix[0])+int(matrix[1])]
    print(cipher)
else:
    message = sys.stdin.readline()  #Se lee el mensaje
    message = message[:-1].replace(" ","")
    #Concatenamos el mensaje a cifrar para encontrar el valor de cada índice
    for a in message:               #Se forma el arreglo de indices
        index += str(keyMatrix.index(a)//5) + str(keyMatrix.index(a)%5)
    #Partimos el arreglo a la mitad por los índices
    indexX=index[:len(index)//2]
    indexY=index[len(index)//2:]
    decipher=""
    #Mapeamos los índices al valor de cada carácter a descifrar.
    for a in range(len(message)):
        decipher += keyMatrix[5*int(indexX[a])+ int(indexY[a])]
    print(decipher)
