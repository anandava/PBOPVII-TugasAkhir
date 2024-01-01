class Sumbangan:
    def __init__(self,nama,jumlah) -> None:
        self.__nama = nama
        self.__jumlah = jumlah
    
    def bukti(self):
        print("\nBukti Transaksi")
        print(f"nama   = {self.__nama}")
        print(f"jumlah = Rp.{self.__jumlah:,}")
    
    def get_nama(self):
        return self.__nama
    
    def get_jumlah(self):
        return self.__jumlah
    
    def informasi_dana():
        lang_total = 0
        vir_total = 0
        for i in range(len(total_langsung)):
            lang_total += total_langsung[i]
            
        for i in range(len(total_virtual)):
            vir_total += total_virtual[i]
        print("Informasi Pengumpulan Dana\n")
        print(f"Pengumpulan dana Langsung = Rp.{lang_total:,}")
        print(f"Pengumpulan dana Virtual  = Rp.{vir_total:,}")
        print(f"Pengumpulan seluruh dana  = Rp.{vir_total+lang_total:,}")
    

class Langsung(Sumbangan):
    def __init__(self, nama, jumlah,metode_bayar) -> None:
        super().__init__(nama, jumlah)
        self.metode_bayar = metode_bayar
        total_langsung.append(super().get_jumlah())
    
    def bukti(self):
        super().bukti()
        print(f"Metode Pembayaran = {self.metode_bayar}")

class Virtual(Sumbangan):
    def __init__(self, nama, jumlah,platform) -> None:
        super().__init__(nama, jumlah)
        self.platform  = platform
        total_virtual.append(super().get_jumlah())
        
    
    def bukti(self):
        super().bukti()
        print(f"Platform Pembayaran = {self.platform}")
        

class Qris(Virtual):
    def __init__(self, nama, jumlah, platform,url) -> None:
        super().__init__(nama, jumlah, platform)
        self.url = url
        self.masuk_qris(jumlah)
    
    def bukti(self):
        if self.url == f"https://{super().get_nama()}/{self.platform}":
            super().bukti()
            print(f"Jenis Pembayaran = Qris")
        else:
            print("\nTransaksi Gagal\n")
    def masuk_qris(self,total):
        if total not in total_virtual:
            total_virtual.append(total)

total_langsung = []
total_virtual = []

sumbang1 = Langsung("dava",500000,"transfer")
sumbang1.bukti()
sumbang2 = Qris("shiddiq",700000,"shopeepay","https://shiddiq/shopeepay")
sumbang2.bukti()
sumbang3 = Virtual("Habsyi",600000,"dana")
sumbang3.bukti()
sumbang4 = Qris("darma",1000000,"shopeepay","https://darma/shopeepay")
sumbang4.bukti()
sumbang5 = Langsung("Rizki",200000,"Cash")
sumbang5.bukti()


Sumbangan.informasi_dana()