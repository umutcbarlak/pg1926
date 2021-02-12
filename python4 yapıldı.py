listeGirilen = []
n = int(input("Kaç Elemanlı Liste İstiyorsunuz?: "))
for i in range(0, n):
   print("Elemanı Gir No-{}: ".format(i+1))
   elm = int(input())
   listeGirilen.append(elm)
print("Girilen Liste:",listeGirilen)

tek_sayılar = []

for i in listeGirilen:
    if i % 2 !=0:
        tek_sayılar.append(i)
    i =i+1
print("En büyük Sayımız",max(tek_sayılar))