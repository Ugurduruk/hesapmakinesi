from abc import ABC, abstractmethod
import sympy as sp

# Sayı tipini tanımlama
Sayı = float

class Islem(ABC):
    """Tüm işlem sınıflarının temel sınıfı"""
    
    @abstractmethod
    def calistir(self, a: Sayı, b: Sayı = None) -> Sayı:
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

class Turev(Islem):
    """Türev işlemini gerçekleştiren sınıf"""
    
    def calistir(self, ifade: str, degisken: str = 'x') -> str:
        """Verilen matematiksel ifadenin türevini alır"""
        x = sp.Symbol(degisken)
        fonksiyon = sp.sympify(ifade)
        turev = sp.diff(fonksiyon, x)
        return str(turev)

class Integral(Islem):
    """İntegral işlemini gerçekleştiren sınıf"""
    
    def calistir(self, ifade: str, degisken: str = 'x') -> str:
        """Verilen matematiksel ifadenin integrali alır"""
        x = sp.Symbol(degisken)
        fonksiyon = sp.sympify(ifade)
        integral = sp.integrate(fonksiyon, x)
        return str(integral)

class HesapMakinesi:
    """Farklı işlemleri gerçekleştirebilen hesap makinesi"""
    
    def __init__(self, islem: Islem):
        """Hesap makinesine bir işlem sınıfı eklenir"""
        self.islem = islem
    
    def hesapla(self, a: Sayı, b: Sayı = None) -> Sayı:
        """Seçilen işlemi gerçekleştirir ve sonucu döndürür"""
        return self.islem.calistir(a, b)

if __name__ == "__main__":
    while True:
        try:
            op = input("İşlem girin (+, -, *, /, turev, integral): ")
            
            islemler = {
                '+': Toplama(),
                '-': Cikarma(),
                '*': Carpma(),
                '/': Bolme(),
                'turev': Turev(),
                'integral': Integral()
            }
            
            if op not in islemler:
                print("Geçersiz işlem. Tekrar deneyin.")
                continue
            
            if op in ['turev', 'integral']:
                ifade = input("Matematiksel ifadeyi girin: ")
                hesap_makinesi = HesapMakinesi(islemler[op])
                sonuc = hesap_makinesi.hesapla(ifade)
            else:
                a = float(input("Birinci sayıyı girin: "))
                b = float(input("İkinci sayıyı girin: "))
                hesap_makinesi = HesapMakinesi(islemler[op])
                sonuc = hesap_makinesi.hesapla(a, b)
            
            print(f"Sonuç: {sonuc}")
        except Exception as e:
            print(f"Hata: {e}")
