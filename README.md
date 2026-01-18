# Abi_X_Yap_Ama_HEPSI

<p align="center">
  <img src="https://img.shields.io/badge/status-stable-brightgreen">
  <img src="https://img.shields.io/badge/type-dataset-blue">
  <img src="https://img.shields.io/badge/format-SQLite-lightgrey">
  <img src="https://img.shields.io/badge/records-1.8M+-purple">
</p>

**Abi_X_Yap_Ama_HEPSI**,  
Goblinhan’ın yaptığı **“AbiXYap”** sitesindeki **tüm kelimelerin**,  
tüm olası kombinasyonlarıyla oluşturulmuş **eksiksiz bir cümle veri setidir**.

---

## 📦 İçerik

- **Dosya:** `Abi_X_Yap_TUMHEPSI.db`
- **Format:** SQLite
- **Toplam kayıt:** **1.809.996**
- **Cümle yapısı:** Abi {kelime 1} kullanarak {kelime 2} yap.

---

## ⚡ Neden SQLite?

- ✔ Milyonlarca satırda **yüksek performans**
- ✔ Düşük disk alanı kullanımı
- ✔ RAM dostu
- ✔ Kolay filtreleme ve arama
- ✔ Fine-tune / analiz için ideal

---

## 🔍 Örnek Sorgular

```sql
-- İlk 10 kayıt
SELECT text FROM sentences LIMIT 10;

-- Rastgele 10 kayıt
SELECT text FROM sentences ORDER BY RANDOM() LIMIT 10;

-- Belirli kelime içerenler
SELECT text FROM sentences WHERE text LIKE '%kalem%';
```

---

## 🤝 Katkıda Bulunma (Pull Request)

Bu proje basit bir dataset projesidir ancak **iyileştirme ve düzenlemelere açıktır**.  
Katkı yapmak isteyenler için adımlar:

1. Bu repoyu **fork**’la
2. Kendi fork’unda yeni bir branch oluştur:
   ```bash
   git checkout -b my-feature

---

<p align="center">
  <img src="https://img.shields.io/github/stars/KaganAk71/Abi_X_Yap_Ama_HEPSI?style=flat-square" alt="Stars">
  <img src="https://img.shields.io/github/forks/KaganAk71/Abi_X_Yap_Ama_HEPSI?style=flat-square" alt="Forks">
  <img src="https://img.shields.io/github/watchers/KaganAk71/Abi_X_Yap_Ama_HEPSI?style=flat-square" alt="Watchers">
  <img src="https://img.shields.io/github/repo-size/KaganAk71/Abi_X_Yap_Ama_HEPSI?style=flat-square" alt="Repo Size">
</p>
