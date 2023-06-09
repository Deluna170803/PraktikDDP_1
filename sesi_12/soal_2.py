# menghitung nilai average

list = []
total = 0

n = int(input("Masukkan banyaknya data: "))

for a in range(n):
    nilai = float(input("Masukkan nilai ke-{} : ".format(a+1)))
    # append() = menambahkan nilai setelah list/ array dari belakang
    list.append(nilai)


# format() = untuk mengukur format berupa string ke layar monitor
print("\nHasil nilai total adalah : {}".format(sum(list)))

print("Hasil rata-rata adalah : {}".format(sum(list)/n))
