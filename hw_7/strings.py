metin = input("metin giriniz")
metin = metin.upper()  
metin=metin.strip()  
metin = metin.replace("a", "e")  
metin = metin.split()  

print("Metin Liste:", metin)

# gorev 2
metin2 = "Python programlama dili"
metin2 = metin2[::-1]
metin2 = metin2.replace("programlama", "kodlama")  
print(metin2)
