a = 256
b = 256
print(a is b)#True
"""
konuya göre -5 ile 256 arasındaki sayılar için
hafıza optimizasyonu yapar.Bu aralıktaki sayılar, aynı bellek adresini paylaşır. 
Bu yüzden aynı sayı karşılaştırıldığında bu aralıktaysa `is` operatörü `True` döndürür.

"""


c = 257
d = 257
print(c is d)
#False