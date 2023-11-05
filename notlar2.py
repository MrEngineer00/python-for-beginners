"""tam sayı bölmesi => ( // ) kalan 120/9= 13.33 120//9 ise 13ü alır
 kalan bulma (%) => 13 % 4 => 13/4 ten kalan 1 dir
 üs bulma (**) => 4**3 4*4*4 dür yani 64 ayrıca: karekok = 64**0.5 ve kupkok= 64**(1/3)
"""
"""STRİNGLER:
a = "hello"
a[0] => h
a[4] => o  pythonda string içerisinde ki harf 0 dan başlar yani 0=h... eder harfı bulmak için a[] kullanılır.
ayıca: a[-1] => o dur ters gider - olursa
string parçalama:
[başlama:bitiş:atlama] örn: a ="python python python" print(a[4:12:2]) burda demek istenen 4ten başla 12 ye kadar 2şer atla
a[:] yaparsan hepsi gelir.
strinlerin uzunluğu => len() ile bulunur kaç tane olduğunu söyler.
NOT: stringler değiştirilemez


a = 'python python python'
print(a[4:12:2])
print((len(a)))
"""

"""
VERİ TİP DÖNÜŞÜMLERİ:
float() ondalıklıları temsil eder. 41.2 
int() tam sayıyı temsişl eder 41
str() fonksiyonu bir girdiyi stringe çevirir a=43 str(a) '43' olur

"""
"""
PRİNT() FONK VE FORMATLAMA:
\n karakteri: altta atar print('merhaba\nnasılsın\niyimiisn') yapılırsa alt altta yazar.
\t karakteri: stringler arasında 4 tane noşluk bırakır print('merhaba\tnasılsın\tiyimiisn')
type() fonksiyonu: içine gönderilen değerin hangi veri tipinde olduğunu gösteririr. type(34) int der tam sayı olduğu için.
sep parametresi: yazdırmak istediğimiz karakterin arasına istediğimiz şeyi yazdırabiliyoruz print(34,35,36, sep= "/") denir ve virgül yerine / gelir.
yıldız parametresi: stringin harflerinin arasına boşluk bırakır. print(*'TBMM') yada print(*'TBMM', sep = ".")

format() fonksiyonu: daha önce tanımlanan değerlerin yerine konmasında yardımcı olur. print("{} + {} ' nin toplamı {}'dır.".format(a,b,a+b)) eşleşme yani. 

"""
"""
pythonda liste veri tipleri: list()
listeler toplanabilir ve stringlerin özellileine sahipler. list3 = list2+list1
listeler ve stringlerin temel farkı listeler değiştirilebilir ancak stringler değiştirilemez.
list.sort() parametresi: sayıları büyükten küçüğe sıralar veya alfabetik sıralar. tersi ise list.sort(reverse=true) denir.
"""

"""
DEMETLER(TUPLELAR]:
demetler listeler gibidir ama en önemli farkı demetler değiştirilemezler.
listeler ve stringlerde bulunan tüm özellikleri kullanabilir demet[:4] gibi.

demetlerin metodları:
count() fonk: forksiyonun içine bir değer verilir ve bu değerin demetin içinde kaç defa geçtini söyler. 
örn: demet = (1, 2, 2, 2, 4, 5, 6) print(demet.count(2)) dersek bize 3 cevabını verir çünkü 3 kez 2 geçiyor.

index() fonk: içine verilen herhangi değer veya stringin nerde olduğunu söyler. 
örn: demet=("python","php","c","java") print(demet.index("c")) dersek c nin konumunun 2 de olduğunu söyler. olmayan bir şey denirse hata verir.

"""
"""
DİCTİONARY: dict()
sözlükler süslü {} parantez ile yapılır.
örn: sozluk1 = {"bir":1, "iki":2, "üç":3,"dört":4} bir sözlük tipidir. sozluk["iki"] dersek bize 2 yi verir. eğer olmayan bir değer yazılırsa hata verir.

sözlüklere eleman eklenebilir.
sozluk["beş"]=5 denirse sözlüğe eklenir.
sözlüklerin elemanı değiştirilebilir hemde artırabilir falan filan.

sözlüklerin metodları:
keys() metodu: sözcüğün değerlerini bir liste olarak gönderir.
sozluk1.keys() dersek sadece bir iki ... gönderir.

values() metodu: sözcüğün değerlerini gönderir.
sozluk1.values() dersek 1 2 3 ... gönderir.

items() metodu. hem keys hem de values değerlerini demet olarak göderebiliriz.
sozluk1.items() dersek dict_items([('bir', 1), ('iki', 2), ('üç', 3), ('dört', 4), ('beş', 5)]) böyle.
"""
"""
İNPUT() FONK:
a =input("bir sayı giriniz") print(a*3) örneğin 5 değerini girdiğimizde bize 555 değerini verir çünkü input ilk tanımlama string olarak tanımlar bu nedenle
int(input()) dennmelidir ki 5 değerini sayı olarak tanımalsın print(a*3) dersek bu sefer bize 15 değerini verir. yada float demeliyiz.
ayrıca 100/10 dediğimiz de python bize float olarak 10.0 değerini verir yani float olarak ancak 100//10 dersek 10 olarak int verir.

"""
"""
KOŞULLU DURUMLAR(İF ELİF ELSE):
boolen verin tipi sadece 2 duruma sahip olabilir bunlar true ve false tur. false=0 true =!0 dır ayrıca. bool() ... bool(0) false ...

Karşılaştırma operatörleri: == eşit midir. != eşit değil midir. > ,<, <=, >= ...
bu operatorler sadece sayılar için değil stringler ve listleri karşılaştırmak içinde kullanılabilir. alfabetik sıra önemli zula < mehmet false verir.

Mantıksal bağlaçlar: and, or, not  
and operatörü: true olması için her işlemin true olması lazım 1<2 and "mehmet"="mehmet" dersek true olur. tek farkta false olur.
or operatörü: genel sonucun true çıkması için tek bir işlemin true olması yeterli. 1>2 or "ajdar" < "hakkı" dersek true olur çünkü ajdarın a sı  daha önce gelir.
not operatörü: bu operatör bir işlemi true ise false false ise true yapar. not 2==2 false olur. değiştirdi.

koşulllu durumlar:
if bloğu: eğer koşul sağlanırsa anlamı taşır yani true olması gerekir.
else bloğu: yanına koşul yazmaya gerek yok. diğer nalamı taşır. istenirse yazılmaz. 
elif bloğu: yada anlamı taşır başka bir koşul yani. istenilen sayısada yazılabilir. else ve elif bloğu tek başına kullanılamaz if olmalı.

"""

"""
DÖNGÜ YAPILARI: for, while, range() fonk , break, continue
FOR döngüleri: 
    in operatörü: 5 in [1 2 3 4] dediğimizde false der . "a" in "merhaba" dediğimizde true der. olup olmadığını kontrol eder.
    örnek: liste = [....] for i in liste: ( demek istenen liste üsütünde gezinmek istiyorum. i listenin il elemanından başlar son elemanına kadar gider ve dögü biter.

While döngüleri:
    döngü false olana kadar devam eder. mutlaka döngüden çıkması için bir tane false eklenmelidir. i +=1 gibi. + solda olamlı 
    eğer başta i = 0 dersek ve dögüde i +=1 tarzı bişey yani false licak bişey yapılmazsa i her zaman 0 olarak kendini tanımalar ve sonsuz dögüye girer.
    NOT: while True ifade: while döngüsünde eğer hiç false ile karşılaşmazsa sonsuza kadar gider der. ancak break ifadesi varsa durur. ( t büyük olmalıdır.)
    
range() fonk:
    bu fonksiyon print(*range(0,20)) gibi kullanılır mutlaka * kullanılmalıdır ve 0 dan 19a kadar yazar.yazılmazsa içinde yazanı yansıtır. 
    atlama değeri print(*range(0,200,5)) 0dan 200e kadar 5 er atlar. ayrıca range(200) demek 0dan 200e kadar demektir illa 0 yazılmasına gerek yok.
    range fonksiyonu her zaman yukaru yönlü hareket eder. azalması için -1 etc kullanılmalıdır. print(*range(20,0,-4)) 
    range fonk listeler gibi hareket edebilir. yani dögüler için liste tanımlamadan for i in range(0,20): print(i) dediğimizde liste gibi hareket edip yazdırır.
    
break ifadesi:
    Döngü herhangi bir yerde ve herhangi bir zamanda break ifadesiyle karşılaştığı zaman çalışmasını bir anda durdurur.
    Böylelikle döngü hiçbir koşula bağlı kalmadan sonlanmış olur. örn: i =0 while i<10: if i ==5: break print(i) i+=1 dersek i 0dan 5e kadar gelir ve i=4 olduğunda
    yani 5.değerinde dögüyü sonlandırır ve yazar i=0,1,3,4 ... diye
    break ifadeleri sadece bulunduğu döngüyü sonlandırır.
    break ifadesi continue ya göre daha çok tercih edilir.
    NOT: while True ifade: while döngüsünde eğer hiç false ile karşılaşmazsa sonsuza kadar gider der. ancak break ifadesi varsa durur. ( t büyük olmalıdır.)
    
continue ifadesi:
    az kullanılır.
    Dongü herhangi bir yerde ve herhangi bir zamanda continue ifadesiyle karsilastagi zaman geri kalan islemlerini yapmadan direk blogunun başına döner.
    yani 0dan 10e listeyi yazdırmak istersek ve eğer 3 u yazdırmak istemiyosak continue deriz ve 3 yazılmayıp 4ten devam eder.

List comprehension:
    listeleri üretmek ve oluşturmak için pythonda çok pratik bir yöntemdir. 
    list.append() metodu listeye eleman eklenmesi için kullanılır.
    orn: liste1 = [1 2 3] bu listeyi başka bir listede kullanmak için list comp. kullanılabilir. yani liste2 = [i for i in liste1] print(liste2) dersek liste2=[1 2 3] olur.
    ÖRNEK: liste1 = [[1,2,3],[5,6,7,8,9],[10,11,12,13,14,15]]
           liste2 = [ x for i in liste1 for x in i] 
           print(liste2) dersek parantezleri kaldırıp yeni bir liste verir. [ 1 2 3 ....15]  
           
DÖNGÜLER ÖRNEK: ATM ÖRNEĞİ
bakiye = 1000

while True:                                                                          # FAKTORİYEL BULMA
    islem = int(input("işlem giriniz"))                                               sayı = int(input("gir"))
    if (islem == "q"):                                                                faktoriyel = 1
       print("yine bekleriz")                                                         for i in range(1,sayı+1):
    elif islem == 1:                                                                       faktoriyel *=i
         print("bakiyeniz:", bakiye)                                                  print("faktoriyel:",faktoriyel)
    elif islem == 2:
         miktar = int(input("miktar giriniz"))
         bakiye += miktar
    elif islem == 3:
        miktar = int(input("miktar giriniz"))
        if (bakiye - miktar < 0 ):
            print("bakiye yetersiz")
            continue                    # ÖNEMLİ 
        bakiye -= miktar
    else:
        print("geçersiz işlem")


# kullanıcının girdiği sayıya kadar yazdırma:
s = int(input('Sayı Girin:'))
for i in range(1,s+1):
  print(i)
        
"""
"""
FONSİYONLAR:
Metodlar: obje.herhangi_bir_metod(değerler(opsiyonel))
    a liste olsun => a.append() listenin sonuna eleman ekler. a.pop en son eklenen elemanı siler mesela append(10) diyerek 10u ekleriz a.pop() dersek 10u siler içine bişey yazılmaz.
    eğer ki bir metodun ne işe yaradığını unuttuysanız help() metoduyla öğrenebilirsim. örn: help(a.append)

Fonksiyonlar:
    genel olarak print() tarzı bir fonksiyonu sıfırdan pythonda oluşturmamıza yardımcı olur. pythona tanımladıktan sonra print type gibi bir fonk olur.
    örn: def hello():
            print("hello")
         print(type(hello)) dersek bize 'hello nun' bir funksiyon olduğunu belirtir 
         def merhaba(isim):
            print("naber",isim)
         print(merhaba("hakkı")) 
         
Fonksiyonlarda Return (değer döndürme): 
    return ifadesi fonksiyonun islemi bittikten sonra çagridigi yere deger döndürmesi anlami tasir. Böylelikle, fonksiyonda aldigimiz değeri bir degiskende
    depolayabilir ve degeri programin baska yerlerinde kullanabiliriz. 
    örn : def toplama(a,b,c):
            return a+b+c
          def ikiylecarp(a):
             return a*2       # alt satıra print(....) yazılırsa python onu okumaz.
          toplam = toplama(3,4,5)
          print(ikiylecarp(toplam)) # en içten en dışa doğru çalışmaya başlar.  
          return genel olarak şöyle tanımlanabilir. bir fon belirsin ve başka yerlerde kullanmak için bir değer girildiğinde o aldığı değerde sabit kalıp başka fonklarda
          kullanılabilir.
          
          return yazıldıktan sonra ekrana hiç bişey yazılmaz sadece sonuç yazılır 

Fonksiyonlarda parametre türleri:
    def hello(name = "no name")
        print("selam",name)   ve hello() içi boş bir şekilde dersek selam no name der ancak hello(mehmet) dersek selam mehmet der.
    
    sep parametresi = > print("ahmet","ali", sep = "/") dersek  arasına / koyar. 
    
    def total(*a)  
        print(a)   total(a,b,c) dersek tupple şeklinde (a,b,c) verir.
        
Fonksiyonlarda global ve yerel değişkenler:
    bir fonksiyon içinde üretilen her değişken yerel değişkendir.
    fonksiyon dışında üretilen her değişken ise global değişkendir.
     
    yerel değişken örn:  a nın def in üzerinde dışında olmasın global oluyor. ancak a fonksiyondan sonra tanımlanırsa globalde hata verir.
    
    def fonksiyon():
        a = 10
        print(a)
    fonksiyon() 
    print(a) 
    
    global parametresi: global değerin yerine local değeri seçer. 

lambda ifadeleri:
    
    
    
    
    
    
    
    
"""
























