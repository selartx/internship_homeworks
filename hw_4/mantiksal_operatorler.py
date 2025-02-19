yas=int(input("yasinizi giriniz"))
if yas > 18 and yas < 65:
 print("yas 18 ve 65 arasindadir")
if yas < 18 or yas > 65:
 print("yas 18den kücük ya da 65ten büyüktür")
if not yas == 25:
 print("yas 25 degildir")
 
#gorev 2

sayi=int(input("sayi giriniz"))
if sayi%2==0 and sayi>0:
 print("true")
else :
 print("false")

#gorev 3
yas = int(input("Yaşınızı giriniz: "))
ehliyet_bilgisi = input("Ehliyetiniz var mı? (Evet/Hayır): ").lower() == 'evet'
if yas > 18 and ehliyet_bilgisi:
    print("Araba kullanabilirsiniz")
else:
    print("Araba kullanamazsınız")
