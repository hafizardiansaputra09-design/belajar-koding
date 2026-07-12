class HeroGame:
    def __init__(self, nama_input, peran_input):
        self.nama = nama_input
        self.peran = peran_input


    def kenalan(self):
        print(f"Halo! Gua {self.nama}. Role Gua Adalah {self.peran}")

hero_satu = HeroGame("Azure", "Marksman")
hero_dua = HeroGame("Betlehem", "Fighter")

hero_satu.kenalan()
hero_dua.kenalan()