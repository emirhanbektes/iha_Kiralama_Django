# iha_Kiralama_Django
İHA kiralamak için admin ve müşteriler için arayüzler oluşturulmuştur. Admin yeni ürün ve Kategorileri ekler, günceller ve siler, Müşteri kiralama tarihine göre kiralar, kiralanan envanteri gösterir ve tarihini güncelleyerek kiralamayı uzatır, veya kiralanan ihayı siler. 

1- python 3.12 kurulumlarını gerçekleştiriniz.

2- postgrasql 12.18.1 kurulumunu gerçekleştiriniz. ( username: postgres Port:5432 password:postgres host: localhost ) 

3- iha dosyasını indiriniz.

4- cmd ile öncelikle pip install pip paket yöneticisini kurunuz.

5- CMD ile iha klasörünün içerisinde pip install django kurulumunu  ardından pip install psycopg2 kurulumunu yapınız. 

6- Kurulumu gerçekleştirdiğiniz Postgresql serverında iha adında veritabanı oluşturunuz. 

7- CMD ile iha klasörünün içerisinde python manage.py migrate yi çalıştırınız. ( Not: manage.py dosyasının bulunduğu yerde çalışır.)

8- CMD ile iha klasörünün içerisinde python manage.py createsuperuser çalıştırarak user: admin email: boş kalabilir password: admin againPassword: admin ( Not: CMD üzerinde kullanıcı adı ve şifre tanımları yapılırken gözükmeyebilir fakat her tanımlamadan sonra enter kullanınız ve işleme devam ediniz. )

9- CMD ile iha klasörünün içerisinde python manage.py makemigrations çalıştırınız. Ardından python manage.py migrate yi çalıştırınız. Böylece veritabanına otomatik tablolar oluşturulmuştur. 

10- CMD ile iha klasörünün içerisinde python manage.py runserver çalıştıradak uygulama URL ine http://127.0.0.1:8000/ geçiş yapabilirsiniz. 

Anasayfa 
![image](https://github.com/emirhanbektes/iha_Kiralama_Django/assets/112666438/4c8e24c5-b1a6-4aef-ba54-3bbe00a2fe0a)


Menü = Anasayfa kiralanan envanter iha kirala hakkımızda ve kullanıcı giriş butonu bulunmaktadır. Kiralanan envanter ve İha kirala butonları üyelik girişi yapmadan açılmamaktadır. 


![image](https://github.com/emirhanbektes/iha_Kiralama_Django/assets/112666438/d5805696-0ee7-4c0a-95dd-cc043fedf09d)

![image](https://github.com/emirhanbektes/iha_Kiralama_Django/assets/112666438/caf5d8c0-3c2f-4c75-bff5-fc35579c0a10)

![image](https://github.com/emirhanbektes/iha_Kiralama_Django/assets/112666438/6716dfa3-d514-4e08-becf-ba11e39aa86f)

Eğer üyelik girişi yönetici (admin ) ise ürün ekle /sil arayüzü gelmektedir. Böylece yeni kiralanacak kategorideki ürünü ve yeni kategori ekleme/silme ve güncelleme işlemleri yapabilmektedir. 
![image](https://github.com/emirhanbektes/iha_Kiralama_Django/assets/112666438/0e492265-66ef-4f1d-a4d0-c603ad62569f)
![image](https://github.com/emirhanbektes/iha_Kiralama_Django/assets/112666438/756c7ce8-902e-43f8-9874-acafa457e5f9)

![image](https://github.com/emirhanbektes/iha_Kiralama_Django/assets/112666438/7a954e18-4e5b-404a-bde7-5cbe207bbe5b)
![image](https://github.com/emirhanbektes/iha_Kiralama_Django/assets/112666438/fedd55b5-036a-4721-b54c-5c9365c22cb3)


![image](https://github.com/emirhanbektes/iha_Kiralama_Django/assets/112666438/6e0fb867-6a62-40aa-b379-bb8b0cfb7cc9)


İha Kirala Ekranına bakıldığında kiralik olan İHALAR ve model bilgileri yer almaktadır. Ve kategorisine göre listelenmektedir. 

![image](https://github.com/emirhanbektes/iha_Kiralama_Django/assets/112666438/3edb2702-7156-4b29-87bf-3f79acd5bd56)

![image](https://github.com/emirhanbektes/iha_Kiralama_Django/assets/112666438/c6d59a51-118e-4b7a-b4f7-ccad1a2149a1)

![image](https://github.com/emirhanbektes/iha_Kiralama_Django/assets/112666438/1b2c9051-489a-4815-875b-184f9a4c75a2)

Müşteri kiralayacağı tarihleri seçerek kiralar ve Müşteri Envanter takibi için Kiralanan Envanter ekranına düşer. Eğer Giriş yapan veya üye olan kişinin kiralık ihası yok ise ekranda listelenmez. 
![image](https://github.com/emirhanbektes/iha_Kiralama_Django/assets/112666438/c648616c-2aab-452e-b27a-4d51ed6fc4d0)
![image](https://github.com/emirhanbektes/iha_Kiralama_Django/assets/112666438/53d0dcee-9ec5-4c22-a870-4a8ae6db060a) kullanıcı kiralam işlemini silebilir. veya tarihleri değiştirebilmektedir. 


tarih güncelleme işlemi zaman yetmediği için yapılamamıştır. 
