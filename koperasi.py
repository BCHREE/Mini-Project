from __future__ import annotations
class Barang:
    def __init__(self, nama: str, harga: int, stok: int):
        self.nama = nama
        self.harga = harga
        self.__stok = stok # Encapsulation

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, value):
        self.__stok = value