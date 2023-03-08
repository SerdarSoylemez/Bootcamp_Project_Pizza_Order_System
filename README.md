# Bootcamp_Project_Pizza_Order_System

Sistem, kullanıcıların menüdeki pizzayı ve istedikleri sosu seçmesiyle başlar. İkinci aşama olarak seçtikleri sos ve pizzayı seçtikten sonra ödemeye kısmına geçiş yaparlar. Kullanıcılar ödemelerini kredi kartı ile yapacaktır. Her pizzanın bir açıklaması ve fiyatı vardır.

Pizza sınıfını ve bu sınıfın içindeki encapsulation(kapsülleme) için get_description() ve get_cost() methodları tanımlayın.

Klasik, Margherita, Türk Pizzası, Dominos Pizza vb. pizza sınıfları oluşturun. Bu pizza türlerinin her biri bir pizza türü olduğu için bu sınıflar alt sınıflar olarak tanımlanacaktır.
Her pizzanın kendine ait bir fiyatı ve sahip olduğu değişkenin içinde pizzaların açıklamasının yer alması gerektiğini unutmayın.

Bir Decorator sınıfı oluşturun. Decorator, burada tüm sos sınıflarının süper sınıfı olarak adlandırılır.
Decorator sınıfı, pizza sınıfının özelliklerini kullanarak get_description() ve get_cost() yöntemlerini kullanacaktır. 

Sos olarak Zeytin, Mantar, Keçi Peyniri, Et, Soğan ve Mısır'ı belirleyin ve belirlediğiniz sosların her birini bir sınıf olarak tanımlayın.
Unutmayın ki her sosun kendine ait bir fiyatı ve değişken olarak her bir pizzanın açıklaması olması gerekir.

Bir main fonksiyonu oluşturun. Bu fonksiyon önce menüyü ekrana yazdıracaktır. Ardından kullanıcının menüden bir pizza ve sos seçmesine imkan tanıyacaktır. 

Seçilen ürünlerin toplam fiyatını hesapladıktan sonra kullanıcıdan isim, TC kimlik numarası, kredi kartı numarası ve kredi kartı şifresi istemektedir. 

Veritabanı olarak adlandırdığımız "Orders_Database.csv" dosyasında pizzasını seçen ve kullanıcı adını, kullanıcı kimliğini, kredi kartı bilgilerini, sipariş açıklamasını, sipariş zamanını ve kredi kartı şifresini tutan bir tablo oluşturunuz.

