chiaro_str=input("Testo in Chiaro: ")
chiaro_arr=[]
scuro_str=""
scuro_arr=[]
chiave=int(input("Chiave: "))
alf=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","u","v","w","x","y","z"]

chiaro_arr=list(chiaro_str)

for i in range(len(chiaro_arr)):
    lettera=alf[alf.index(chiaro_arr[i])+chiave]
    scuro_arr.append(lettera)

scuro_str="".join(scuro_arr)
print(scuro_str)
