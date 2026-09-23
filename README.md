# studi_kasus_5_Novitasari-Muhammad-Nor  

Nama : Novitasari Muhammad Nor  
Nim : 26091160082

# *Penjelasan tentang coding Sistem Perhitungan Biaya Parkir juga fungsinya*     

1. def hitung_biaya_parkir(jenis_kendaraan, durasi_parkir): digunakan untuk membuat function yang menerima jenis kendaraan dan durasi parkir sebagai parameter. Percabangan if digunakan untuk menentukan tarif Mobil sebesar Rp5.000 per jam, sedangkan elif menentukan tarif Motor sebesar Rp3.000 per jam. Selanjutnya, total_biaya = tarif * durasi_parkir digunakan untuk menghitung total biaya parkir berdasarkan tarif dan lama parkir. Terakhir, return total_biaya digunakan untuk mengembalikan hasil total biaya parkir.
<img width="319" height="101" alt="image" src="https://github.com/user-attachments/assets/67172f42-71ca-468f-8a7c-b7ff6666f3ab" />



2. jenis_kendaraan = input(...) digunakan untuk meminta pengguna memasukkan jenis kendaraan, yaitu Mobil atau Motor. jam_masuk = int(input(...)) digunakan untuk memasukkan jam masuk kendaraan dalam bentuk angka, sedangkan jam_keluar = int(input(...)) digunakan untuk memasukkan jam keluar kendaraan. Data jam masuk dan jam keluar nantinya digunakan untuk menghitung lama parkir.
<img width="371" height="48" alt="image" src="https://github.com/user-attachments/assets/e84b56a2-52a7-4957-a830-2d9d989408e7" />
  

3. lama_parkir = jam_keluar - jam_masuk digunakan untuk menghitung berapa lama kendaraan parkir dengan cara mengurangi jam keluar dengan jam masuk. Hasilnya disimpan dalam variabel lama_parkir dan nantinya digunakan untuk menghitung total biaya parkir.

<img width="290" height="20" alt="image" src="https://github.com/user-attachments/assets/ee1db24e-7839-4872-9f12-04d9d5cbb2d9" />
  

  
4. total_biaya = hitung_biaya_parkir(jenis_kendaraan, lama_parkir) digunakan untuk memanggil function hitung_biaya_parkir() dengan memasukkan jenis kendaraan dan lama parkir. Hasil perhitungan dari function tersebut kemudian disimpan ke dalam variabel total_biaya untuk ditampilkan sebagai total biaya parkir.

<img width="336" height="21" alt="image" src="https://github.com/user-attachments/assets/e3482f2b-09a4-4f2c-abf0-fbc5b1a30add" />
 


5. print() digunakan untuk menampilkan hasil program, yaitu jenis kendaraan, jam_masuk, jam_keluar, lama_parkir, dan total_biaya_parkir. Baris print("\n==== Hasil Perhitungan Parkir ====") menampilkan judul hasil, sedangkan baris berikutnya menampilkan data yang sudah dimasukkan dan dihitung sebelumnya. Jadi, pengguna dapat melihat seluruh hasil perhitungan biaya parkir dengan jelas.
<img width="336" height="76" alt="image" src="https://github.com/user-attachments/assets/d61eb766-a5c6-4398-a5a2-edd6e7d7cc3b" />
  


# *hasil output*
- jika parkir mobil
<img width="629" height="98" alt="image" src="https://github.com/user-attachments/assets/a21b0b9c-0939-4e64-810d-9a44cde99063" />

- jika parkir motor    
<img width="613" height="101" alt="image" src="https://github.com/user-attachments/assets/58e74fdc-dda0-422b-ab2a-2eff733ce4ea" />




6. *Selesai*
    

*Sekian Penjelasan tentang coding Sistem Perhitungan Biaya Parkir juga fungsinya, jika ada salah kata maupun ketikan saya mohon maaf dan terimakasihh:)* 






