daftar_buku = ['seven habits', 'how to inflluence people', 'the power of kepepet', '36cmderajat']
print("Tampilkan variable daftar_buku")
print(daftar_buku)

print('\nProses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[1])

print('\nTampilkan dengan for in range pakai angka 0, 3. hanya terbatas 1-3 buku')
for i in range(0, 3):
    print(daftar_buku[i])

print('\nTampilkan dengan for in range (semua daftar muncul)')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [2, 'pecah belah ke 3', -212, 45.987]
print('\nTampilkan dengan for in range, dimana tipe data tiap elemen berbeda2')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar_buku')
daftar_buku = ['seven habits', 'how to inflluence people', 'the power of kepepet', '36cmderajat']
print('\nTambahkan 1 buku baru')
daftar_buku.append('dunia matematika kelas 5')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nClear List')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\nGanti elemen (buku) pertama')
daftar_buku = ['seven habits', 'how to inflluence people', 'the power of kepepet', '36cmderajat']
daftar_buku[0] = 'eight habits'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen (buku) ke-2 (0=ke1, 1=ke2, 2=ke3')
daftar_buku = ['seven habits', 'how to inflluence people', 'the power of kepepet', '36cmderajat']
buku = daftar_buku.pop(1)
daftar_buku[0] = 'eight habits'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nbuku yang diambil tadi')
print(buku)

print('\nperintah pop aja')
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\npop-1 (menghapus kedua dari belakang)')
daftar_buku = ['seven habits', 'how to inflluence people', 'the power of kepepet', '36cmderajat']
daftar_buku.pop(-2)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])



print('\nmenghapus daftar, list comprehension')
daftar_buku = ['seven habits', 'how to inflluence people', 'the power of kepepet', '36cmderajat']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


