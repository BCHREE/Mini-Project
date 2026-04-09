from __future__ import annotations
from base_user import User

class Admin(User):
    def __init__(self, name: str):
        super().__init__(name, "admin")

    def hitung_total(self, keranjang: list) -> int:
        total = sum(item['subtotal'] for item in keranjang)
        print(f"\n[ADMIN] Menghitung total belanja...")
        return total