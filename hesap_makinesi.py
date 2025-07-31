def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b != 0:
        return a / b
    else:
        return "Sıfıra bölme hatası!"

print("Basit Hesap Makinesi")
print("İşlemler: +, -, *, /")

sayi1 = float(input("1. sayıyı girin: "))
islem = input("İşlem türünü seçin (+, -, *, /): ")
sayi2 = float(input("2. sayıyı girin: "))

if islem == "+":
    print("Sonuç:", toplama(sayi1, sayi2))
elif islem == "-":
    print("Sonuç:", cikarma(sayi1, sayi2))
elif islem == "*":
    print("Sonuç:", carpma(sayi1, sayi2))
elif islem == "/":
    print("Sonuç:", bolme(sayi1, sayi2))
else:
    print("Geçersiz işlem.")
