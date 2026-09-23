# studi_kasus_5_Novitasari-Muhammad-Nor  

Nama : Novitasari Muhammad Nor  
Nim : 26091160082

# *Penjelasan tentang coding Sistem Perhitungan Biaya Parkir juga fungsinya*     

1. def hitung_biaya_parkir(jenis_kendaraan, durasi_parkir): digunakan untuk membuat function yang menerima jenis kendaraan dan durasi parkir sebagai parameter. Percabangan if digunakan untuk menentukan tarif Mobil sebesar Rp5.000 per jam, sedangkan elif menentukan tarif Motor sebesar Rp3.000 per jam. Selanjutnya, total_biaya = tarif * durasi_parkir digunakan untuk menghitung total biaya parkir berdasarkan tarif dan lama parkir. Terakhir, return total_biaya digunakan untuk mengembalikan hasil total biaya parkir.
<img width="544" height="95" alt="image" src="https://github.com/user-attachments/assets/2b8714d2-66b5-4079-af45-6e1f3f963276" />


2. jenis_kendaraan = input(...) digunakan untuk meminta pengguna memasukkan jenis kendaraan, yaitu Mobil atau Motor. jam_masuk = int(input(...)) digunakan untuk memasukkan jam masuk kendaraan dalam bentuk angka, sedangkan jam_keluar = int(input(...)) digunakan untuk memasukkan jam keluar kendaraan. Data jam masuk dan jam keluar nantinya digunakan untuk menghitung lama parkir.
<img width="496" height="42" alt="image" src="https://github.com/user-attachments/assets/8aa83fc2-8f21-4e70-89a0-12de68a49f68" />  

3. lama_parkir = jam_keluar - jam_masuk digunakan untuk menghitung berapa lama kendaraan parkir dengan cara mengurangi jam keluar dengan jam masuk. Hasilnya disimpan dalam variabel lama_parkir dan nantinya digunakan untuk menghitung total biaya parkir.

<img width="299" height="23" alt="image" src="https://github.com/user-attachments/assets/af28c702-11c1-4342-a295-b8f493459226" />  

  
4. total_biaya = hitung_biaya_parkir(jenis_kendaraan, lama_parkir) digunakan untuk memanggil function hitung_biaya_parkir() dengan memasukkan jenis kendaraan dan lama parkir. Hasil perhitungan dari function tersebut kemudian disimpan ke dalam variabel total_biaya untuk ditampilkan sebagai total biaya parkir.

<img width="326" height="21" alt="image" src="https://github.com/user-attachments/assets/70c25e1a-82bd-45c7-8c38-c590963f770e" />  


5. print() digunakan untuk menampilkan hasil program, yaitu jenis kendaraan, jam_masuk, jam_keluar, lama_parkir, dan total_biaya_parkir. Baris print("\n==== Hasil Perhitungan Parkir ====") menampilkan judul hasil, sedangkan baris berikutnya menampilkan data yang sudah dimasukkan dan dihitung sebelumnya. Jadi, pengguna dapat melihat seluruh hasil perhitungan biaya parkir dengan jelas.
<img width="549" height="69" alt="image" src="https://github.com/user-attachments/assets/e5ba3c4c-f8ea-4821-b530-f77f805dea92" />  


# *hasil output*
- jika parkir mobil
<img width="629" height="98" alt="image" src="https://github.com/user-attachments/assets/a21b0b9c-0939-4e64-810d-9a44cde99063" />

- jika parkir motor    
<img width="613" height="101" alt="image" src="https://github.com/user-attachments/assets/58e74fdc-dda0-422b-ab2a-2eff733ce4ea" />




7. *Selesai*
    

*Sekian Penjelasan tentang coding Sistem Perhitungan Biaya Parkir juga fungsinya, jika ada salah kata maupun ketikan saya mohon maaf dan terimakasihh:)* 






