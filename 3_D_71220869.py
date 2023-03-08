import math
a = 1
while True:
    jarak = (input('Masukkan jarak awal (dalam meter): '))
    if jarak.isdigit()  :
        jarak1 = int(jarak)
        ke5 = int(input('Masukkan sudut elevasi pada menit ke-5 (dalam derajat): '))
        h5 = math.radians(ke5)
        t5 = math.tan(h5)
        ke6 = int(input('Masukkan sudut elevasi pada menit ke-6 (dalam derajat): '))
        h6 = math.radians(ke6)
        t6 = math.tan(h6) #nilai tan
        tggi = jarak1 *(t5)
        jrk = jarak1*(t6-t5)
        slsh = jrk *t6
        print('Ketinggian drone saat menit ke 5 adalah %.2f'%(tggi),'meter')
        print('Selisih ketinggian drone saat menit ke-5 dan ke-6 adalah %.2f'%(slsh),'meter')
        continue
    
    elif jarak.lower() == 'stop' or 'berhenti':
        for i in range(1):
            print('Program dihentikan')
        break
