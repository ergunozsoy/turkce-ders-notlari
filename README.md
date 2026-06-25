# Türkçe Ders Notları — Dijital Öğrenme Platformu

**Türkisch 1–4 · Dr. Ergun Özsoy · LMU München**

Dr. Ergun Özsoy'un Türkisch 1–4 ders notlarından derlenen, tarayıcıda çalışan interaktif Türkçe dilbilgisi çalışma kitabı. Sunucu gerektirmez — tek bir HTML dosyasıyla her yerde açılır.

## İçerik

- **50 dilbilgisi konusu** (4 bölüm): her konuda **Almanca açıklama (Erklärung)**, Türkçe açıklama, **"Unterschied zum Deutschen"** (Türkçenin Almancadan farkı) kutusu, kural tablosu, örnekler, iki interaktif alıştırma ve cevap anahtarı
- **7 Grammar in Use incelemesi**: zaman ve kiplerin senaryolu, kullanım odaklı anlatımı
- **4 seviye pratik diyalog**: tanışmadan ileri anlatıma günlük konuşma kalıpları

> **Hangi dosyayı açmalıyım?** Yayın ve kullanım için **`index.html`**. `app_template.html` yalnızca derleme şablonudur (içeriği gömülü değildir) ve tek başına açıldığında bir uyarı gösterir.

## Özellikler

- Boşluk doldurma alıştırmaları — anında, renkli geri bildirim (Türkçe karakter duyarlı kontrol)
- Tıkla-eşleştir alıştırmaları
- Bölüm/konu kenar çubuğu navigasyonu ve arama
- İlerleme takibi (tarayıcıda saklanır)
- Mobil uyumlu, klavye erişilebilir

## GitHub Pages ile yayınlama (5 dakika)

1. GitHub'da yeni bir depo (repository) oluşturun, örn. `turkce-ders-notlari`.
2. `index.html` dosyasını depoya yükleyin (sürükle-bırak yeterli).
3. Depoda **Settings → Pages** bölümüne gidin.
4. **Source** olarak `Deploy from a branch` → `main` / `root` seçin, kaydedin.
5. Birkaç dakika sonra siteniz şu adreste yayında olur:
   `https://KULLANICI-ADINIZ.github.io/turkce-ders-notlari/`
6. Bu bağlantıyı öğrencilerinizle paylaşın.

> Yalnızca `index.html` yüklemeniz yeterlidir — içerik dosyanın içine gömülüdür.

## İçeriği güncelleme

İçerik, tasarımdan ayrı tutulur. Düzenleme akışı:

1. `content.json` dosyasını düzenleyin (konu, alıştırma, cevap ekleyin/değiştirin).
2. Yeniden derleyin:
   ```bash
   python3 build.py
   ```
   Bu komut `content.json` içeriğini `app_template.html` şablonuna gömerek yeni `index.html` üretir.
3. Güncellenen `index.html`'i GitHub'a tekrar yükleyin.

## Dosya yapısı

| Dosya | Açıklama |
|---|---|
| `index.html` | Yayına hazır, kendi kendine yeten uygulama (içerik gömülü) |
| `content.json` | Düzenlenebilir içerik verisi (50 konu + GIU + diyaloglar) |
| `app_template.html` | Tasarım/uygulama iskeleti (`/*__DATA__*/` yer tutucu) |
| `build.py` | `content.json` → `index.html` derleme betiği |

## Sonraki adımlar (yol haritası)

- **Tasarım turu**: kart düzenleri, ünlü uyumu hafıza kartları, görseller
- **PWA / mobil uygulama**: çevrimdışı kullanım ve "ana ekrana ekle"
- **Çoklu sayfa / arama indeksi**: içerik büyüdükçe ayrı sayfa yapısı
- **Sesli telaffuz** ve **kullanıcı hesapları / ilerleme senkronu**

---
*Tasarım paleti: petrol mavisi #1F3864 · turuncu #ED7D31 (ekler/vurgu) · açık yeşil #E2EFDA (kural kutuları) · açık bej #FBF2E4 (alıştırma alanları).*
