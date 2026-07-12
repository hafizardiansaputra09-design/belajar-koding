import rumus_toko

from colorama import Fore, Style

jumlah = int(input("mo beli berapah??:"))

hasil_bonus = rumus_toko.cek_bonus(jumlah)

print(Fore.GREEN + f"[INFO] {hasil_bonus}" + Style.RESET_ALL)

