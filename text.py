class Telebe:
    def _init_(self, ad, soyad, yas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas

    def melumatlari_goster(self):
        print(f"Ad: {self.ad}, Soyad: {self.soyad}, Yaş: {self.yas}")

class Muellim(Telebe):
    def _init_(self, ad, soyad, yas, fenn):
        super()._init_(ad, soyad, yas)
        self.fenn = fenn

    def melumatlari_goster(self):
        print(f"Ad: {self.ad}, Soyad: {self.soyad}, Yaş: {self.yas}, Fənn: {self.fenn}")

telebe1 = Telebe("Nigar", "Əliyeva", 20)
telebe2 = Telebe("Elvin", "Məmmədov", 21)


muellim1 = Muellim("Aysel", "Əsgərova", 65,"Riyaziyyat")
muellim2 = Muellim("Fərid", "Soltanov", 40, "Fizika")


telebe1.melumatlari_goster()
telebe2.melumatlari_goster()

muellim1.melumatlari_goster()
muellim2.melumatlari_goster()