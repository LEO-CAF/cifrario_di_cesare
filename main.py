# tutte le variabili

chiaro_str=""
chiaro_arr=[]
scuro_str=""
scuro_arr=[]
key=0
alf=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lettera=""
x=0

# input > controllo chiaro

while True:
    chiaro_str=input("Testo in Chiaro: ")
    if chiaro_str.isalpha():
        chiaro_arr=list(chiaro_str)
        break
    else:
        print("Inserise solo Caratteri Alfabetici senza Numeri, Spazi e Caratteri Speciali")

# input > controllo key

while True:
    key=input("Chiave: ")
    if key.isdigit():
        key=int(key)
        break
    else:
        print("Inserise solo Numeri Interi Positivi senza Spazi, Punti e Virgole")

# ciclo principale

for i in range(len(chiaro_arr)):
    x=0
    while True:
        try:
            lettera=alf[alf.index(chiaro_arr[i])+key-x]
        except:
            x+=26
        else:
            break

    scuro_arr.append(lettera)

# output

scuro_str="".join(scuro_arr)
print("Testo Criptato:",scuro_str)
