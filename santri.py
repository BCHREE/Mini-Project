from __future__ import annotations
from base_user import User
class Santri(User):
    def __init__(self, name):
        super().__init__(name, "santri")
        self.keranjang = []

    def tambah_ke_keranjang(self, barang, jumlah):
        subtotal = barang.harga * jumlah
        self.keranjang.append({
            'nama': barang.nama,
            'qty': jumlah,
            'subtotal': subtotal
        })
        print(f"✅ {barang.nama} masuk keranjang.")