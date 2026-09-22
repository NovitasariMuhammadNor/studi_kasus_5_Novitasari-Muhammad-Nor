# Sistem Perhitungan Biaya Parkir

total_biaya_parkir = {
    "mobil": 5000,
    "motor": 3000,
}

def hitung_biaya_parkir(jenis_kendaraan, durasi_parkir):
    if jenis_kendaraan == "mobil":
        tarif = 5000
    elif jenis_kendaraan == "motor":
        tarif = 3000

    total_biaya = tarif * durasi_parkir
    return total_biaya

jenis_kendaraan = input("masukan jenis kendaraan (mobil/motor): ")
jam_masuk = int(input("masukan jam masuk: "))
jam_keluar = int(input("masukan jam keluar: "))

lama_parkir = jam_keluar - jam_masuk

total_biaya = hitung_biaya_parkir(jenis_kendaraan, lama_parkir)

print("\n==== Hasil Perhitungan Parkir ====")
print("jenis kendaraan :", jenis_kendaraan)
print("jam masuk :", jam_masuk)
print("jam keluar :", jam_keluar)
print("lama parkir :", lama_parkir, "jam")
print("total biaya : Rp", total_biaya)
