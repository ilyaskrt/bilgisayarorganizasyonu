import socket
import time
import os
import sys

def checkArg():
    if len(sys.argv) != 2:
        print("HATA. Yanlış Sayıda Argüman Girdiniz. Bir Dahaki Sefere Lütfen 1 Argüman Girin!")
        sys.exit()
    else:
        print("1 Argüman Var. Devam Edebilirsiniz")

def checkPort():
    if int(sys.argv[1]) <= 5000:
        print("Port Numarası Geçersiz. Bir Dahaki Sefere Geçerli Port Numarası Girin.")
        sys.exit()
    else:
        print("Port Numarası Kabul Edildi!")

def ServerList():
    print("Komut Gönderme Onaylandı.")
    msg = "Geçerli Liste Komutu. Devam Et."
    msgEn = msg.encode('utf-8')
    s.sendto(msgEn, clientAddr)
    print("Mesaj Gönderildi.")

    print("Sunucuda Liste Fonksiyonu")

    F = os.listdir(path="C:/Users/ataar/AppData/Local/Programs/Python/Python38")
    
    Lists = []
    for file in F:
        Lists.append(file)
    ListsStr = str(Lists)
    ListsEn = ListsStr.encode('utf-8')
    s.sendto(ListsEn, clientAddr)
    print("Sunucudan Gönderilen Liste")

def ServerExit():

    print("İstemciye Mesaj Gönderme! Soket Kapatılıyor.")
    s.close()
    sys.exit()

def ServerGet(g):
    print("Komut Gönderme Onaylandı.")
    msg = "Geçerli Alma Komutu. Devam Et."
    msgEn = msg.encode('utf-8')
    s.sendto(msgEn, clientAddr)
    print("Mesaj Gönderildi.")

    print("Suncuda, Alma Fonksiyonu")

    if os.path.isfile(g):
        msg = "Dosya Var. Devam Et"
        msgEn = msg.encode('utf-8')
        s.sendto(msgEn, clientAddr)
        print("Dosyanın Varlığı Hakkında Gönderilen Mesaj.")

        c = 0
        sizeS = os.stat(g)
        sizeSS = sizeS.st_size  
        print("Bayt Cinsinden Dosya Boyutu:" + str(sizeSS))
        NumS = int(sizeSS / 4096)
        NumS = NumS + 1
        tillSS = str(NumS)
        tillSSS = tillSS.encode('utf8')
        s.sendto(tillSSS, clientAddr)

        check = int(NumS)
        GetRunS = open(g, "rb")
        while check != 0:
            RunS = GetRunS.read(4096)
            s.sendto(RunS, clientAddr)
            c += 1
            check -= 1
            print("Paket Numarası:" + str(c))
            print("Veri Gönderme Devam Ediyor:")
        GetRunS.close()
        print("Sunucudan Gönderildi - Alma Fonksiyonu")

    else:
        msg = "HATA: Dosya, Sunucu Dizininde Mevcut Değil."
        msgEn = msg.encode('utf-8')
        s.sendto(msgEn, clientAddr)
        print("Mesaj Gönderildi.")

def ServerPut():
    print("Komut Gönderme Onaylandı.")
    msg = "Geçerli Verme Komutu. Devam Et."
    msgEn = msg.encode('utf-8')
    s.sendto(msgEn, clientAddr)
    print("Mesaj Gönderildi.")

    print("Sunucuda, Verme Fonksiyonu")
    if t2[0] == "Verme":

        BigSAgain = open(t2[1], "wb")
        d = 0
        print("Dosya Varsa Paketlerin Alınması Şimdi Başlayacaktır.")
        #print("Timeout is 15 seconds so please wait for timeout at the end.")
        try:
            Count, countaddress = s.recvfrom(4096)  
        except ConnectionResetError:
            print("HATA. Port Numarası Eşleşmiyor. Çıkılıyor. Bir Dahaki Sefere Aynı Port Numarasını Giriniz.")
            sys.exit()
        except:
            print("Zaman Aşımı Veya Başka Bir Hata")
            sys.exit()

        tillI = Count.decode('utf8')
        tillI = int(tillI)

        #tillI = 100
        #tillI = tillI - 2
        # s.settimeout(2)

        while tillI != 0:
            ServerData, serverAddr = s.recvfrom(4096)
            # s.settimeout(2)

            #BigS = open("tmp.txt", "wb")
            dataS = BigSAgain.write(ServerData)
            #BigS2 = open("tmp.txt", "r")
            #Add = BigS2.read()
            # print(Add)
            #Big = Big + Add
            # BigS2.close()
            #dataF = tmp.write(ServerData)
            # Big.append(ServerData)
            d += 1
            tillI = tillI - 1
            print("Alınan Paket Numarası:" + str(d))

            # tmp.close()
            
        #Bigstr = ''.join(map(str, Big))
        BigSAgain.close()
        print("Yeni Dosya Kapatıldı. Dizininizdeki İçeriği Kontrol Edin.")

        #Bigstr = str(Big)
        # print(Big)

        #BigSAgain = open(t2[1], "w")
        # BigSAgain.write(Big)
        # BigSAgain.close()
        
def ServerElse():
    msg = "HATA: Sorun " + \
        t2[0] + "Sunucu Tarafından Anlaşılamamıştır."
    msgEn = msg.encode('utf-8')
    s.sendto(msgEn, clientAddr)
    print("Mesaj Gönderildi.")


host = ""
checkArg()
try:
    port = int(sys.argv[1])
except ValueError:
    print("HATA. Çıkılıyor. Bir Dahaki Sefere Aynı Port Numarasını Giriniz.")
    sys.exit()
except IndexError:
    print("HATA. Çıkılıyor. Bir Dahaki Sefere Aynı Port Numarasını Giriniz.")
    sys.exit()
checkPort()

#port = 6000

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Sunucu Soketi Başlatıldı")
    s.bind((host, port))
    print("Başarılı Dinleme. Şimdi Alıcı Bekleniyor.")
    # s.setblocking(0)
    # s.settimeout(15)
except socket.error:
    print("Soket Oluşturulamadı")
    sys.exit()

# time.sleep(1)
while True:
    try:
        data, clientAddr = s.recvfrom(4096)
    except ConnectionResetError:
        print("HATA. Port Numarası Eşleşmiyor. Çıkılıyor. Bir Dahaki Sefere Aynı Port Numarasını Giriniz.")
        sys.exit()
    text = data.decode('utf8')
    t2 = text.split()
   #print("data print: " + t2[0] + t2[1] + t2[2])
    if t2[0] == "Alma":
        print("Alma Fonksiyonuna Git")
        ServerGet(t2[1])
    elif t2[0] == "Verme":
        print("Verme Fonksiyonuna Git")
        ServerPut()
    elif t2[0] == "liste":
        print("Liste Fonksiyonuna Git")
        ServerList()
    elif t2[0] == "Çıkış":
        print("Çıkış Fonksiyonuna Git")
        ServerExit()
    else:
        ServerElse()

print("Program Sona Erecek.")
quit()
