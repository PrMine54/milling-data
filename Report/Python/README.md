### Python Proje Template ve Temel Olarak Dikkat Edilmesi Gerekenler

Bu repo'da optimizasyon problemlerinde kullanacağımız python dili için temel yapı bulunmaktadır. 
Bir python projesi geliştirirken bulunması gereken temel dosya ve dizinler bu yapıda verilmiştir.

```
    proje_ismi/
    │
    ├── data/ # bu dizinde çalışmada kullanılan veriler tanımlanacaktır
    ├── src/ # bu dizinde temel olarak problem çözümünde kullanılan algoritmalar, matematiksel modelleme, sonuçların alınması için gerekli olan methodlar bulunmaktadır
    │   ├── __init__.py
    │   ├── algorithms/ # çözümde kullanılan algoritmalar bu dizinde her biri için ayrı dosya olacak şekilde verilecek
    │   ├── evaluation/ # çözümün kalitesinin gösterilmesi için uygulanan metrikler ve görselleştirmeler burada verilecek: hesaplanan metrikler ayrı dosya görseller ayrı dosya
    │   ├── objectives/ # amaç fonksiyonları, modellemeler burada konularına göre ayrı dosyalar verilecek mesela: iki objective olsun enerji ve zaman -> energy.py & time.py 
    │   └── utils/
    ├── tests/ # geliştirdiğimiz fonksiyonlarının birim testlerinin bulunduğu dizin
    ├── .gitignore # bu dosyaya gitle versiyonlanmasını istemediğimiz, proje dizinindeki deneme dosyalarımızı, env gibi dosyaları ekleriz
    ├── requirements.txt # projenin çalıştırılması için gereken kütüphaneler buraya eklenecek
    ├── CHANGELOG.md # kodda büyük değişiklikler olduğunda neleri değiştirdik burada tarih atılarak yazılacak
    ├── README.md # temel olarak problemden projede ne nerde, nasıl çalıştırılır bunlar burada açıklanmalı ve kaynaklar belirtilmeli
    ├── setup.py # projeyi çalıştırmak için ayarlamanın yapıldığı dosya
    └── main.py # burada kontrol edilebilir parametreler ile problem çözümüne imkan sağlanmalı
```
#### Geliştirmeleri yaparken dikkat edilmesi gerekenler:
* Kullanılan parametre isimler ve fonksiyon isimleri amacına yönelik olmalıdır
* Fonksiyon açıklamaları ve parametrelerin açıklamalarını eklemeliyiz
* Hata dönebilecek durumlar için kontrol veya exception ekleyelim (bir değerin hiç sıfır gelmesi beklenmiyor mesela assert deger !=0 kontrolü ekleyelim olması durumunda exception basalım)
* Fonksiyonlar için birim testler yazılabilir çıktıların ara adımlarda kontrol edilebilmesi için