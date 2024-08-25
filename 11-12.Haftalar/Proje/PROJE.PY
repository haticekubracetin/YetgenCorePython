import time 
import calendar
print("Hoşgeldiniz.\nLütfen havalimanları seçiminizi yapınız.")

# Kodun daha doğal durması için time kütüphanesi ile işlemler arasında geçiş süresi sağladık.
time.sleep(1)
havalimanlari={ 
    1:"Ankara Esenboğa Havalimanı",
    2:"İstanbul Sabiha Gökçen Havalimanı",
    3:"Van Ferit Melen Havalimanı",
    4:"Izmir Adnan Menderes Havalimanı",
    5:"Fraport Tav Antalya Havalimanı"}

# While döngüsü ile kalkış ve varış havalimanlarını kullanıcıya seçtirdik.
while True:
    print("Havalimanları:")
    for key,value in havalimanlari.items():
        print(f"{key}:{value}")
    try:
        kalkış_seçimi=int(input("Kalkış Havalimanı numarasını giriniz:"))
        kalkış_havalimanı=havalimanlari[kalkış_seçimi]
        print("Kalkış havalimanı :" ,kalkış_havalimanı)
        print("Şimdi varış havalimanını seçiniz")
        time.sleep(1)
        break
    except KeyError:
        print("Yanlış seçim yaptınız.Lütfen kalkış havalimaını tekrar seçiniz.")
del(havalimanlari[kalkış_seçimi]) 
while True:
    for key,value in havalimanlari.items():
        print(f"{key}:{value}") 
    try:
        varış_seçimi=int(input("Varış Havalimanı numarasını giriniz:"))
        varış_havalimanı=havalimanlari[varış_seçimi]
        print("Varış  Havalimanı:",varış_havalimanı)
        break
    except KeyError:
        print("Yanlış seçim yaptınız.Lütfen tekrar varış havalimanını seçiniz.")
        time.sleep(1)
time.sleep(1)
print(f"{kalkış_havalimanı}-{varış_havalimanı} arası uçuşunuz için lütfen diğer işlemlere devam ediniz")
time.sleep(1)

# If-else kullanarak kullanıcının tarih seçmesini sağladık.
print(" ")
print("Lütfen tarih seçiniz")
while True:
    yıl=int(input("İşlem yapmak istediğiniz yılı seçiniz: "))
    if yıl<2024:
        print("Hata yaptınız tekrar yıl seçiniz.")
    else:
        break 
while True:
    aylar={
        1:"Ocak",2:"Şubat",3:"Mart",4:"Nisan",5:"Mayıs",6:"Haziran",
        7:"Temmuz",8:"Ağustos",9:"Eylül",10:"Ekim",11:"Kasım",12:"Aralık"}
    ay=int(input("İşlem yapmak istediğniz ayın numarasını giriniz(1 den 12 e kadar): ")) 
    if ay>12:
        print("Ay seçerken hata yaptınız.Tekrar seçiniz.")
    elif yıl==2024 and ay<=8:
        print("Ay seçerken hata yaptınız.Tekrar seçiniz.")
    else :
        ayı=aylar[ay]
        break

# calendar kütüphanesi kullanarak takvim oluşturduk ve ekrana yazdırdık.
a=calendar.TextCalendar(calendar.MONDAY)
b=a.formatmonth(yıl,ay)
print(b)
while True:
    gün=int(input("İşlem yapmak istediğiniz günü giriniz:")) 
    if yıl%4==0 and ay==2:
        if gün<=29:
            print(f"Tarih seçiminiz :{gün}-{ay}-{yıl}")
            break 
        else:
            print("Gün seçerken hata yaptınız.Lütfen tekrar gün seçiniz.")
    elif yıl%4!=0 and ay==2:
        if gün<=28:
            print(f"Tarih seçiminiz :{gün}-{ay}-{yıl}")
            break 
        else:
            print("Gün seçerken hata yaptınız.Lütfen tekrar gün seçiniz.")
    elif ay==1 or ay==3 or ay==5 or ay==7 or ay==8 or ay==10 or ay==12:
        if gün<=31:
            print(f"Tarih seçiminiz :{gün}-{ay}-{yıl}")
            break 
        else:
            print("Gün seçerken hata yaptınız.Lütfen tekrar gün seçiniz.")
    else:
        if gün<30:
            print(f"Tarih seçiminiz :{gün}-{ay}-{yıl}")
            break
        else:
            print("Gün seçerken hata yaptınız.Lütfen tekrar gün seçiniz.")

# Her iki farklı havalimanı arası uçuş saatlerini belirledik ve sözlükle tanımladık, kullanıcıya bunlardan seçim yaptırdık.
while True:
    havalimanlari_listesi=["Ankara Esenboğa Havalimanı","İstanbul Sabiha Gökçen Havalimanı","Van Ferit Melen Havalimanı",
                            "Izmir Adnan Menderes Havalimanı","Fraport Tav Antalya Havalimanı"]
    if kalkış_havalimanı==havalimanlari_listesi[0]:
        if varış_havalimanı==havalimanlari_listesi[1]:
            try:
                uçuş_saatleri={1:"09.00",2:"11.00",3:"13.45",4:"17.30",5:"23.00"}
                for key,value in uçuş_saatleri.items():
                    print(f"{key}:{value}")
                uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
                uçuş=uçuş_saatleri[uçuş_seç]
                print(f"Uçuşunuz:{gün}-{ayı}-{yıl} saat {uçuş}")
                break
            except KeyError:               
                print("Yanlış seçim yaptınız.Tekrar deneyiniz.")
        elif varış_havalimanı==havalimanlari_listesi[2]:
            try:
                uçuş_saatleri={1:"06.00",2:"10.00"}
                for key,value in uçuş_saatleri.items():
                    print(f"{key}:{value}")
                uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
                uçuş=uçuş_saatleri[uçuş_seç]
                print(f"Uçuşunuz:{gün}-{ayı}-{yıl} saat {uçuş}")
                break
            except KeyError:
                print("Yanlış seçim yaptınız.Tekrar deneyiniz.")
        elif varış_havalimanı==havalimanlari_listesi[3]:
            try:
                uçuş_saatleri={1:"12.00",2:"16.00",3:"22.15"}
                for key,value in uçuş_saatleri.items():
                    print(f"{key}:{value}")
                uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
                uçuş=uçuş_saatleri[uçuş_seç]
                print(f"Uçuşunuz:{gün}-{ayı}-{yıl} saat {uçuş}")
                break
            except KeyError:
                print("Yanlış seçim yaptınız.Tekrar deneyiniz.")
        elif varış_havalimanı==havalimanlari_listesi[4]:
            try:
                uçuş_saatleri={1:"07.00",2:"13.30",3:"21.45"}
                for key,value in uçuş_saatleri.items():
                    print(f"{key}:{value}")
                uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
                uçuş=uçuş_saatleri[uçuş_seç]
                print(f"Uçuşunuz:{gün}-{ayı}-{yıl} saat {uçuş}")
                break
            except KeyError:
                print("Yanlış seçim yaptınız.Tekrar deneyiniz.")
    elif kalkış_havalimanı==havalimanlari_listesi[1]:
        if varış_havalimanı==havalimanlari_listesi[0]:
            try:
                uçuş_saatleri={1:"07.00",2:"10.00",3:"15.00",4:"18.00"}
                for key,value in uçuş_saatleri.items():
                     print(f"{key}:{value}")
                uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
                uçuş=uçuş_saatleri[uçuş_seç]
                print(f"Uçuşunuz:{gün}-{ayı}-{yıl} saat {uçuş}")
                break
            except KeyError:               
                print("Yanlış seçim yaptınız.Tekrar deneyiniz.")
        elif varış_havalimanı==havalimanlari_listesi[2]:
            try:
                uçuş_saatleri={1:"08.00",2:"12.00",3:"20.00"}
                for key,value in uçuş_saatleri.items():
                    print(f"{key}:{value}")
                uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
                uçuş=uçuş_saatleri[uçuş_seç]
                print(f"Uçuşunuz:{gün}-{ayı}-{yıl} saat {uçuş}")
                break
            except KeyError:
                print("Yanlış seçim yaptınız.Tekrar deneyiniz.")
        elif varış_havalimanı==havalimanlari_listesi[3]:
            try:
                uçuş_saatleri={1:"09.00",2:"13.00",3:"19.00",4:"22.00"}
                for key,value in uçuş_saatleri.items():
                    print(f"{key}:{value}")
                uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
                uçuş=uçuş_saatleri[uçuş_seç]
                print(f"Uçuşunuz:{gün}-{ayı}-{yıl} saat {uçuş}")
                break
            except KeyError:
                print("Yanlış seçim yaptınız.Tekrar deneyiniz.")
        elif varış_havalimanı==havalimanlari_listesi[4]:
            try:
                uçuş_saatleri={1:"08.30",2:"11.150",3:"20.30",4:"23.45"}
                for key,value in uçuş_saatleri.items():
                    print(f"{key}:{value}")
                uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
                uçuş=uçuş_saatleri[uçuş_seç]
                print(f"Uçuşunuz:{gün}-{ayı}-{yıl} saat {uçuş}")
                break
            except KeyError:
                print("Yanlış seçim yaptınız.Tekrar deneyiniz.")
    elif kalkış_havalimanı==havalimanlari_listesi[2]: 
        if varış_havalimanı==havalimanlari_listesi[1]:
            try:
                uçuş_saatleri={1:"12.00",2:"16.15",3:"20.45"}
                for key,value in uçuş_saatleri.items():
                    print(f"{key}:{value}")
                uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
                uçuş=uçuş_saatleri[uçuş_seç]
                print(f"Uçuşunuz:{gün}-{ayı}-{yıl} saat {uçuş}")
                break
            except KeyError:               
                print("Yanlış seçim yaptınız.Tekrar deneyiniz.")
        elif varış_havalimanı==havalimanlari_listesi[0]:
            try:
                uçuş_saatleri={1:"09.30",2:"14.00",3:"17.15"}
                for key,value in uçuş_saatleri.items():
                    print(f"{key}:{value}")
                uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
                uçuş=uçuş_saatleri[uçuş_seç]
                print(f"Uçuşunuz:{gün}-{ayı}-{yıl} saat {uçuş}")
                break
            except KeyError:
                print("Yanlış seçim yaptınız.Tekrar deneyiniz.")
        elif varış_havalimanı==havalimanlari_listesi[3]:
            try:
                uçuş_saatleri={1:"08.00",2:"15.30"}
                for key,value in uçuş_saatleri.items():
                    print(f"{key}:{value}")
                uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
                uçuş=uçuş_saatleri[uçuş_seç]
                print(f"Uçuşunuz:{gün}-{ayı}-{yıl} saat {uçuş}")
                break
            except KeyError:
                print("Yanlış seçim yaptınız.Tekrar deneyiniz.")
        elif varış_havalimanı==havalimanlari_listesi[4]:
            try:
                uçuş_saatleri={1:"13.00",2:"19.00"}
                for key,value in uçuş_saatleri.items():
                    print(f"{key}:{value}")
                uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
                uçuş=uçuş_saatleri[uçuş_seç]
                print(f"Uçuşunuz:{gün}-{ayı}-{yıl} saat {uçuş}")
                break
            except KeyError:
                print("Yanlış seçim yaptınız.Tekrar deneyiniz.")
    elif kalkış_havalimanı==havalimanlari_listesi[3]:
        if varış_havalimanı==havalimanlari_listesi[1]:
            try:
                uçuş_saatleri={1:"07.00",2:"11.00",3:"17.45",4:"22.30"}
                for key,value in uçuş_saatleri.items():
                    print(f"{key}:{value}")
                uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
                uçuş=uçuş_saatleri[uçuş_seç]
                print(f"Uçuşunuz:{gün}-{ayı}-{yıl} saat {uçuş}")
                break
            except KeyError:               
                print("Yanlış seçim yaptınız.Tekrar deneyiniz.")
        elif varış_havalimanı==havalimanlari_listesi[0]:
            try:
                uçuş_saatleri={1:"12.00",2:"18.00",3:"21.00"}
                for key,value in uçuş_saatleri.items():
                    print(f"{key}:{value}")
                uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
                uçuş=uçuş_saatleri[uçuş_seç]
                print(f"Uçuşunuz:{gün}-{ayı}-{yıl} saat {uçuş}")
                break
            except KeyError:
                print("Yanlış seçim yaptınız.Tekrar deneyiniz.") 
        elif varış_havalimanı==havalimanlari_listesi[2]:
            try:
                uçuş_saatleri={1:"09.00",2:"11.15",3:"18.45"}
                for key,value in uçuş_saatleri.items():
                    print(f"{key}:{value}")
                uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
                uçuş=uçuş_saatleri[uçuş_seç]
                print(f"Uçuşunuz:{gün}-{ayı}-{yıl} saat {uçuş}")
                break
            except KeyError:
                print("Yanlış seçim yaptınız.Tekrar deneyiniz.") 
        elif varış_havalimanı==havalimanlari_listesi[4]:
            try:
                uçuş_saatleri={1:"06.30",2:"10.00",3:"19.45"}
                for key,value in uçuş_saatleri.items():
                    print(f"{key}:{value}")
                uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
                uçuş=uçuş_saatleri[uçuş_seç]
                print(f"Uçuşunuz:{gün}-{ayı}-{yıl} saat {uçuş}")
            except KeyError:
                print("Yanlış seçim yaptınız.Tekrar deneyiniz.")
    elif kalkış_havalimanı==havalimanlari_listesi[4]:

        if varış_havalimanı==havalimanlari_listesi[1]:
            try:
                uçuş_saatleri={1:"11.45",2:"15.00",3:"20.45",4:"23.45"}
                for key,value in uçuş_saatleri.items():
                    print(f"{key}:{value}")
                uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
                uçuş=uçuş_saatleri[uçuş_seç]
                print(f"Uçuşunuz:{gün}-{ayı}-{yıl} saat {uçuş}")
                break
            except KeyError:               
                print("Yanlış seçim yaptınız.Tekrar deneyiniz.")
        elif varış_havalimanı==havalimanlari_listesi[2]:
            try:
                uçuş_saatleri={1:"07.30",2:"14.30",3:"18.15"}
                for key,value in uçuş_saatleri.items():
                    print(f"{key}:{value}")
                uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
                uçuş=uçuş_saatleri[uçuş_seç]
                print(f"Uçuşunuz:{gün}-{ayı}-{yıl} saat {uçuş}")
                break
            except KeyError:
                print("Yanlış seçim yaptınız.Tekrar deneyiniz.") 
        elif varış_havalimanı==havalimanlari_listesi[3]:
            try:
                uçuş_saatleri={1:"09.30",2:"15.40",3:"20.00"}
                for key,value in uçuş_saatleri.items():
                    print(f"{key}:{value}")
                uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
                uçuş=uçuş_saatleri[uçuş_seç]
                print(f"Uçuşunuz:{gün}-{ayı}-{yıl} saat {uçuş}")
                break
            except KeyError:
                print("Yanlış seçim yaptınız.Tekrar deneyiniz.") 
        elif varış_havalimanı==havalimanlari_listesi[0]:
            try:
                uçuş_saatleri={1:"10.00",2:"17.00",3:"22.15"}
                for key,value in uçuş_saatleri.items():
                    print(f"{key}:{value}")
                uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
                uçuş=uçuş_saatleri[uçuş_seç]
                print(f"Uçuşunuz:{gün}-{ayı}-{yıl} saat {uçuş}")
                break
            except KeyError:
                print("Yanlış seçim yaptınız.Tekrar deneyiniz.")
print(" ")
time.sleep(1)
print("Lütfen bilet türünü ve sınıfını seçiniz.")

# Yetişkin ve çocuk, ekonomi ve prime olarak sınıflar tanımladık.
class Sınıf:
    def __init__(self, bilet_türü=None, koltuk_sınıfı=None):
        self.bilet_türü = bilet_türü
        self.koltuk_sınıfı = koltuk_sınıfı

    def biletTürü(self):
        while True:
            print("BİLET TÜRLERİ")
            bilet_türleri = {
                "Yetişkin": "Tam bilet",
                "Çocuk": "18 yaş altı çocuklar için %25 indirimli bilet"
            }
            for key, value in bilet_türleri.items():
                print(f"{key}: {value}")
            bilet_seç = str(input("Almak istediğiniz bilet türünü seçiniz: ")).capitalize()
            if bilet_seç in bilet_türleri:
                self.bilet_türü = bilet_seç
                print("Bilet türünüz: " + bilet_seç + " (" + bilet_türleri[bilet_seç] + ")")
                break
            else:
                print("Geçersiz seçim. Lütfen doğru bir bilet türü seçiniz.")
    def koltukSınıfı(self):
        while True:
            print("SINIF TÜRLERİ ve HAKLARI")
            sınıf_türleri = {
                "Ekonomi": "15 kg bagaj hakkı - 8 kg el bagajı hakkı - 500 mil puanı",
                "Prime": "25 kg bagaj hakkı - 8 kg el bagajı hakkı - 1000 mil puanı - ikram - bilet fiyatının 1.5 katı"
                }  
            for key, value in sınıf_türleri.items():
                print(f"{key}: {value}")
            sınıf_seç = str(input("Almak istediğiniz bilet sınıfını seçiniz: ")).capitalize()
            if sınıf_seç in sınıf_türleri:
                self.koltuk_sınıfı = sınıf_seç
                print("Bilet sınıfınız: " + sınıf_seç)
                break
            else:
                print("Geçersiz seçim. Lütfen doğru bir bilet sınıfı seçiniz.")

# Kullanıcının tercihlerine göre fiyatı güncelledik.
class Fiyat(Sınıf):
    def __init__(self, bilet_türü=None, koltuk_sınıfı=None, fiyat=2000):
        super().__init__(bilet_türü, koltuk_sınıfı)
        self.fiyat = fiyat

    def bilet_fiyat(self):
        if self.koltuk_sınıfı == "Ekonomi" and self.bilet_türü == "Yetişkin":
            print(f"Fiyat: {self.fiyat} TL")
        elif self.koltuk_sınıfı == "Ekonomi" and self.bilet_türü == "Çocuk":
            print(f"Fiyat: {self.fiyat * 0.75} TL")
        elif self.koltuk_sınıfı == "Prime" and self.bilet_türü == "Yetişkin":
            print(f"Fiyat: {self.fiyat * 1.5} TL")
        elif self.koltuk_sınıfı == "Prime" and self.bilet_türü == "Çocuk":
            print(f"Fiyat: {self.fiyat * 1.5 * 0.75} TL")
bilet = Sınıf()
bilet.biletTürü()
bilet.koltukSınıfı()
bilet_fiyatı = Fiyat(bilet.bilet_türü, bilet.koltuk_sınıfı)
bilet_fiyatı.bilet_fiyat()

# Kullanıcıdan kişi bilgilerini aldık.
def kişi_bilgileri():
    ad=str(input("Lütfen adınızı giriniz:")).capitalize()
    soyad=str(input("Lütfen soyadınızı giriniz:")).upper()
    tc=int(input("Lütfen 11 haneli kimlik numaranızı giriniz:"))
    yaş=int(input("Lütfen yaşınızı giriniz:"))

# Kişi ve uçuş bilgilerini içeren bileti her kullanıcı için ayrı dosyalara kaydettik.
    with open(f"{tc}.txt", "w", encoding="utf-8") as file:
        file.write(f"Adınız: {ad} {soyad}\n")
        file.write(f"TC kimlik numaranız: {tc}\n")
        file.write(f"Yaşınız: {yaş}\n")
        file.write(f"Uçuşunuz: {kalkış_havalimanı} - {varış_havalimanı}\n")
        file.write(f"Uçuş tarihi: {gün}-{ayı}-{yıl}\n")
        file.write(f"Uçuş saati: {uçuş}\n")
kişi_bilgileri()
print("Bilet hazırlandı.İyi yolculuklar dileriz.")








     



            


            


           


