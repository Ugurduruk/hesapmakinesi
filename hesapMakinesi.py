from abc import ABC, abstractmethod

# Sayı tipini tanımlama
Sayı = float

class Islem(ABC):
    """Tüm işlem sınıflarının temel sınıfı"""
    
    @abstractmethod
    def calistir(self, a: Sayı, b: Sayı) -> Sayı:
        """İşlem gerçekleştiren metod. Her işlem sınıfı bu metodu kendi işlevine göre implement etmelidir."""
        pass

class Toplama(Islem):
    """Toplama işlemini gerçekleştiren sınıf"""
    
    def calistir(self, a: Sayı, b: Sayı) -> Sayı:
        """Verilen iki sayıyı toplar"""
        return a + b

class Cikarma(Islem):
    """Çıkarma işlemini gerçekleştiren sınıf"""
    
    def calistir(self, a: Sayı, b: Sayı) -> Sayı:
        """Verilen iki sayıdan birini çıkarır"""
        return a - b

class Carpma(Islem):
    """Çarpma işlemini gerçekleştiren sınıf"""
    
    def calistir(self, a: Sayı, b: Sayı) -> Sayı:
        """Verilen iki sayıyı çarpar"""
        return a * b

class Bolme(Islem):
    """Bölme işlemini gerçekleştiren sınıf"""
    
    def calistir(self, a: Sayı, b: Sayı) -> Sayı:
        """Verilen iki sayıyı böler. Bölme sıfırla yapılırsa hata fırlatılır"""
        if b == 0:
            raise ValueError("Sıfıra bölme hatası")
        return a / b

class HesapMakinesi:
    """Farklı işlemleri gerçekleştirebilen hesap makinesi"""
    
    def __init__(self, islem: Islem):
        """Hesap makinesine bir işlem sınıfı eklenir"""
        self.islem = islem
    
    def hesapla(self, a: Sayı, b: Sayı) -> Sayı:
        """Seçilen işlemi gerçekleştirir ve sonucu döndürür"""
        return self.islem.calistir(a, b)

if __name__ == "__main__":
    while True:
        try:
            # Kullanıcıdan sayıları ve işlemi alıyoruz
            a = float(input("Birinci sayıyı girin: "))
            op = input("İşlem girin (+, -, *, /): ")
            b = float(input("İkinci sayıyı girin: "))
            
            # İşlem türlerine göre sınıfları ilişkilendiriyoruz
            islemler = {
                '+': Toplama(),
                '-': Cikarma(),
                '*': Carpma(),
                '/': Bolme()
            }
            
            # Geçersiz işlem durumunda kullanıcıya uyarı mesajı veriyoruz
            if op not in islemler:
                print("Geçersiz işlem. Tekrar deneyin.")
                continue
            
            # Hesap makinesini seçilen işlem sınıfıyla başlatıyoruz
            hesap_makinesi = HesapMakinesi(islemler[op])
            sonuc = hesap_makinesi.hesapla(a, b)  # Hesaplama işlemi yapılır
            print(f"Sonuç: {sonuc}")
        except Exception as e:
            print(f"Hata: {e}")