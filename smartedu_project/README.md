# Django Eğitim Sitesi

## Proje Açıklaması

Bu proje, kullanıcıların kayıt olup derslere katılabildiği bir Django tabanlı eğitim sitesidir. Admin paneli üzerinden dersler yüklenebilir ve yönetilebilir. Kullanıcılar ise mevcut dersleri görüntüleyebilir ve istedikleri derslere kayıt olabilirler.

## Özellikler

- **Admin Paneli**: Ders ekleme, düzenleme ve silme
- **Kullanıcı Yönetimi**: Kayıt olma, giriş yapma ve derslere kayıt olma
- **Çoklu HTML Şablonu**: Her sayfanın kendine özgü tasarımı ve özellikleri bulunur
- **Ders Takibi**: Kullanıcılar kayıt oldukları dersleri görebilir
- **Dinamik İçerik**: Django template sistemi kullanılarak dinamik sayfalar oluşturulmuştur
- **Ek Bilgi**:Projede template kısmı şablon olarak free template alındı projede yogun olarak django ve backend tarafında duruldu
## Kurulum

### 1. Gereksinimler

Proje çalıştırılmadan önce aşağıdaki bağımlılıkların yüklü olması gerekmektedir:

- Python (3.x)
- Django
- SQLite (veya tercih edilen başka bir veritabanı)

### 2. Kurulum Adımları

1. Depoyu klonlayın:
   ```sh
   git clone <repo-link>
   cd <proje-dizini>
   ```
2. Sanal ortamı oluşturun ve etkinleştirin:
   ```sh
   python -m venv env
   source env/bin/activate  # MacOS/Linux
   env\Scripts\activate  # Windows
   ```
3. Gerekli paketleri yükleyin:
   ```sh
   pip install -r requirements.txt
   ```
4. Veritabanını oluşturun ve migrate işlemlerini gerçekleştirin:
   ```sh
   python manage.py migrate
   ```
5. Admin kullanıcısı oluşturun:
   ```sh
   python manage.py createsuperuser
   ```
6. Sunucuyu başlatın:
   ```sh
   python manage.py runserver
   ```

## Kullanım

- **Admin Paneli**: `http://127.0.0.1:8000/admin/` adresinden giriş yapılabilir.
- **Ana Sayfa**: Kullanıcılar dersleri görebilir ve kayıt olabilir.
- **Ders Detay Sayfası**: Her dersin içeriği görüntülenebilir.
- **Kullanıcı Paneli**: Kullanıcılar kayıt oldukları dersleri buradan takip edebilir.

## Geliştirme

Yeni özellikler eklemek için projeyi forklayabilir ve geliştirmeler yapabilirsiniz. Değişiklikleri test etmek için aşağıdaki komutu kullanabilirsiniz:

```sh
python manage.py test
```

##
