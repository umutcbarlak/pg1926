b_liste = []
for i in range(1,101):
    b_liste.append(i)     

a_liste = []
for i in b_liste:
    if i % 3 == 0 and i % 5 == 0 :
        a_liste.append("fizzbuzz")
        
    elif i % 3 == 0:
        a_liste.append("Fizz")
        
    elif i % 5 == 0 :
        a_liste.append("buzz")
    
    else:
        a_liste.append(i)
        
   
    
print(a_liste)
