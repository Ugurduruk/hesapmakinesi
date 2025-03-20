from abc import ABC, abstractmethod

# Tek Sorumluluk ve Açık/Kapalı Prensibi
Sayı = float

class Islem(ABC):
    """İşlemler için soyut sınıf"""
    
    @abstractmethod
    def calistir(self, a: Sayı, b: Sayı) -> Sayı:
        pass

class Toplama(Islem):
    def calistir(self, a: Sayı, b: Sayı) -> Sayı:
        return a + b

class Cikarma(Islem):
    def calistir(self, a: Sayı, b: Sayı) -> Sayı:
        return a - b

class Carpma(Islem):
    def calistir(self, a: Sayı, b: Sayı) -> Sayı:
        return a * b

class Bolme(Islem):
    def calistir(self, a: Sayı, b: Sayı) -> Sayı:
        if b == 0:
            raise ValueError("Sıfıra bölme hatası")
        return a / b

# Bağımlılıkları Ters Çevirme Prensibi (DIP)
class HesapMakinesi:
    """Bağımlılık enjeksiyonu kullanan hesap makinesi"""
    
    def __init__(self, islem: Islem):
        self.islem = islem
    
    def hesapla(self, a: Sayı, b: Sayı) -> Sayı:
        return self.islem.calistir(a, b)

if __name__ == "__main__":
    while True:
        try:
            a = float(input("Birinci sayıyı girin: "))
            op = input("İşlem girin (+, -, *, /): ")
            b = float(input("İkinci sayıyı girin: "))
            
            islemler = {
                '+': Toplama(),
                '-': Cikarma(),
                '*': Carpma(),
                '/': Bolme()
            }
            
            if op not in islemler:
                print("Geçersiz işlem. Tekrar deneyin.")
                continue
            
            hesap_makinesi = HesapMakinesi(islemler[op])
            sonuc = hesap_makinesi.hesapla(a, b)
            print(f"Sonuç: {sonuc}")
        except Exception as e:
            print(f"Hata: {e}")