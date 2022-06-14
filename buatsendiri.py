def daftar_alattulis():
    print('alattulis \t harga')
    print('pensil \t Rp.5000')
    print('buku \t Rp.4000')
    print('bolpen \tRp.3000')
    print('tipe x \t Rp.7000')
    print('lem \t Rp.5000')
    print('spidol \t Rp.8000')
daftar_alattulis()
data = input('alat tulis yang akan dibeli adalah ')
print(data)
if data == 'pensil':
    hasil = 5000
    print(f'anda harus membayar sebesar {hasil}')
if data == 'buku':
    hasil = 4000
    print(f'anda harus membayar sebesar {hasil}')
if data == 'bolpen':
    hasil = 3000
    print(f'anda harus membayar sebesar {hasil}')
if data == 'tipe x':
    hasil = 7000
    print(f'anda harus membayar sebesar {hasil}')
if data == 'lem':
    hasil = 5000
    print(f'anda harus membayar sebesar {hasil}')
if data == 'spidol':
    hasil = 8000
    print(f'anda harus membayar sebesar {hasil}')
