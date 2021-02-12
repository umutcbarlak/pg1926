listeGirilen = []
n = int(input("Kaç Elemanlı Liste İstiyorsunuz?: "))
for i in range(0, n):
   print("Elemanı Gir No-{}: ".format(i+1))
   elm = int(input())
   listeGirilen.append(elm)
print("Girilen Liste:",listeGirilen)

yeni_liste=[]

for i in listeGirilen :
    if i == 0 :
        yeni_liste.append(i)
    i=i+1

for i in listeGirilen:
    if i != 0:
        yeni_liste.append(i)
    i=i+1

    

print("Yeni Liste:",yeni_liste)
        
    