from __future__ import annotations
from admin import Admin
from santri import Santri
from koperasi import Barang

def main() -> None:
    daftar_barang: list = [
        Barang("Mikako", 1000, 15),
        Barang("La tiao", 1500, 50),
        Barang("Aoka", 2500, 30),
        Barang("Roti Gepeng", 500, 20)
    ]
    admin_koperasi = Admin("Ustadz")


    print("======= PROGRAM DI JALANKAN ========")    
    role = input("ADMIN/SANTRI ??? (ketik: santri): ").lower()

    if role == "santri":
        nama_s = input("Masukkan Nama Anda: ")
        sntr = Santri(nama_s)

        while True:
            tanya = input("Mau tambah/beli? (yes/no) ")
            if tanya == "yes" or tanya == "Yes" or tanya == "YES":
             print("Lanjut!")
            if tanya != 'yes': 
                break 

            print("--- List Barang Ready ---")
            for i, b in enumerate(daftar_barang):
                print(f"{i+1}. {b.nama} (Harga: {b.harga}, Stok: {b.stok})")
            
            pilih: int = int(input("Pilih nomor barang: ")) - 1
            item = daftar_barang[pilih]

            if item.stok <= 0:
                print("⚠️ STOK SEDANG HABIS!")
                continue

            jumlah = int(input(f"Mau Beli berapa {item.nama}? "))
            
            if jumlah <= item.stok:
                sntr.tambah_ke_keranjang(item, jumlah)
                item.stok -= jumlah # Update sisa stok di objek Barang
            else:
                print("❌ Stok tidak cukup!")

        print("\n" + "="*35)
        print("STRUK BELANJA SANTRI")
        print("="*35)
        
        total_semua: int = admin_koperasi.hitung_total(sntr.keranjang)
        
        for k in sntr.keranjang:
            print(f" {k['nama']} x{k['qty']} : Rp{k['subtotal']}")
        
        print("-" * 35)
        print(f" TOTAL BAYAR : Rp{total_semua}")
        print("="*35)
        
        print(f"Syukron {sntr.name}! Sisa stok gudang telah diupdate.")
        print("=== END ===")

if __name__ == "__main__":
    main()