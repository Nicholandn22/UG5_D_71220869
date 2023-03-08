def ganti_kata(n):
    a = n.split()
    for i in range(len(a)):
        if a[i] == m:
            a[i] = o
    b = ' '.join(a)
    print(b)
n = input("Masukkan Kalimat : ")
m = input('Kata yang di cari : ')
o = input('Diganti menjadi : ')
ganti_kata(n)


