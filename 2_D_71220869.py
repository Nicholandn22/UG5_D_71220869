def hitung_mobil():
    x = 1
    solo = 0
    surabaya = 0
    jogja = 0
    magelang = 0
    while x > 0 :
        a = input('Masukkan asal mobil (ketik "done" untuk keluar): ').lower()
        if a == 'solo':
            solo += 1
            continue
        elif a == 'surabaya':
            surabaya += 1
            continue
        elif a == 'jogja':
            jogja += 1
            continue
        elif a == 'magelang':
            magelang += 1
            continue
        elif a == 'done':
            break
        break
    print(f'Jumlah mobil Solo : {solo}')
    print(f'Jumlah mobil Surabaya : {surabaya}')
    print(f'Jumlah mobil Jogja : {jogja}')
    print(f'Jumlah mobil Magelang : {magelang}')

hitung_mobil()
