# program membentuk persegi

panjang_persegi = int(input("Masukkan banyaknya sisi : "))
lebar_persegi = panjang_persegi
for i in range(panjang_persegi):
    for j in range(lebar_persegi):
        print(" #",  end=" ")
    print()

# butuh dua print karena :
# 1. untuk for j(lebar persegi)
# 2. untuk for i (panjang persegi)
