# gorev 1
number1 = int(input("1. sayiyi giriniz: "))
number2 = int(input("2. sayiyi   giriniz: "))

print("Toplama:", number1 + number2)

print("Cikarma number1 - number2:", number1 - number2)
print("Cikarma number2 - number1:", number2 - number1)

print("Çarpma:", number1 * number2)


if number2 != 0:
    print("Bölme number1 / number2:", number1 / number2)
    print("Tam Bölme number1 // number2:", number1 // number2)
    print("Mod Alma number1 % number2:", number1 % number2)
else:
    print("Bölme number1 / number2: Tanimsiz" )
    print("Tam Bölme number1 // number2: Tanimsiz ")
    print("Mod Alma number1 % number2: Tanimsiz ")

if number1 != 0:
    print("Bölme number2 / number1:", number2 / number1)
    print("Tam Bölme number2 // number1:", number2 // number1)
    print("Mod Alma number2 % number1:", number2 % number1)
else:
    print("Bölme number2 / number1: Tanimsiz")
    print("Tam Bölme number2 // number1: Tanimsiz")
    print("Mod Alma number2 % number1: Tanimsiz")

print("Üs Alma number1 ** number2:", number1 ** number2)
print("Üs Alma number2 ** number1:", number2 ** number1)

# gorev 2
yaricap = float(input("Yarıçapı giriniz: "))

print("Dairenin Alanı:", (yaricap ** 2) * 3.14)
