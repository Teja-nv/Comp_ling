slovar=dict()
print("Введите общее количество слов в требуемом словаре(число должно быть четным):")
n=int(input())
n=n/2
a=1

while(n>0):
    print("Введите слово на английском:")
    eng=str(input())
    i=0
    k=0
    p=0
    q=0
    for i in range (len(eng)):
        p=eng[i]
        if (ord(p)>65 and ord(p)<90) or(ord(p)>97 and ord(p)<122):
             slovar[a]=eng   
        else:
            print("Некорректный язык")
            break
    
  
            

    print("Введите слово на русском:")
    ru=str(input())
    for k in range(len(ru)):
        q=ru[k]
        if (ord(q)>1040 and ord(q)<1103):
            slovar[a+1]=ru
        else:
        
            print("Некорректный язык")
            break
      
           

    
    n-=1
    a+=2
  
print(slovar)
