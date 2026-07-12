def hitung_suka2gua(harga_ram, harga_ssd, uang_gua):
    sisa_kurang = harga_ram + harga_ssd - uang_gua
    return sisa_kurang
kekurangan_gua = hitung_suka2gua(500000, 1000000, 1200000)

print(f"duit lu masi kurang {kekurangan_gua} le buat belinya, cemungut ngodingnya :)")