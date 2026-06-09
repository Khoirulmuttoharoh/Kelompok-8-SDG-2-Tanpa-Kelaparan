# 📊 Food Loss Lakehouse Pipeline
## Analisis Tren Food Loss Lintas Negara Berdasarkan Komoditas dan Tahapan Rantai Pasok Pangan Menggunakan Medallion Architecture Berbasis Apache Spark

Repositori ini berisi implementasi pipeline Data Engineering berbasis **Apache Spark** dan **Medallion Architecture** untuk mengelola, membersihkan, dan menganalisis data **Food Loss Database FAO**.

Proyek ini bertujuan membangun arsitektur data yang terstruktur melalui Bronze Layer, Silver Layer, dan Gold Layer sehingga menghasilkan data analitik yang siap digunakan untuk eksplorasi data, visualisasi dashboard, dan pengambilan keputusan berbasis data.

---

# 🌍 Latar Belakang

Food loss merupakan salah satu tantangan utama dalam rantai pasok pangan global. Kehilangan pangan yang terjadi sejak tahap produksi hingga distribusi berdampak pada:

- Ketahanan pangan global
- Efisiensi ekonomi sektor pangan
- Keberlanjutan lingkungan
- Pencapaian Sustainable Development Goals (SDGs), khususnya SDG 2: Zero Hunger

Melalui proyek ini dilakukan analisis food loss lintas negara menggunakan Food Loss Database FAO untuk mengidentifikasi pola kehilangan pangan berdasarkan negara, wilayah, komoditas, tahapan rantai pasok, penyebab kehilangan, dan tren tahunan.

---

# 🏗️ Arsitektur Lakehouse (Medallion Architecture)

Pipeline dibangun menggunakan pendekatan Medallion Architecture yang terdiri atas tiga lapisan utama.

```text
Food Loss Database (FAO)
            │
            ▼
      🥉 Bronze Layer
        Raw Data
            │
            ▼
      🥈 Silver Layer
      Cleaned Data
            │
            ▼
       🥇 Gold Layer
     Analytical Data
            │
            ▼
      📊 Dashboard &
          Insight
```

---

# 🥉 Bronze Layer (Raw Data)

Bronze Layer berfungsi sebagai lapisan penyimpanan data mentah hasil ingest dari sumber data.

### Aktivitas

- Membaca dataset Food Loss FAO
- Menyimpan data mentah tanpa transformasi
- Menjaga integritas data sumber
- Menyimpan data dalam format Parquet

### Output

```text
lakehouse/bronze/
├── food_loss/
└── bronze_food_loss.parquet
```

---

# 🥈 Silver Layer (Cleaned Data)

Silver Layer bertanggung jawab terhadap peningkatan kualitas data sebelum dilakukan analisis.

### Aktivitas

- Menghapus data duplikat
- Menangani missing values
- Validasi atribut numerik
- Standarisasi atribut
- Menyiapkan data untuk kebutuhan analitik

### Output

```text
lakehouse/silver/
├── food_loss/
└── silver_food_loss.parquet
```

---

# 🥇 Gold Layer (Analytical Data)

Gold Layer menghasilkan berbagai data produk analitik yang siap digunakan untuk eksplorasi data dan dashboard.

### Output Analitik

```text
lakehouse/gold/

├── food_loss_by_country
├── food_loss_by_region
├── food_loss_by_commodity
├── food_loss_by_stage
├── food_loss_by_cause
├── food_loss_summary
├── food_loss_trend
└── csv
```

### Analisis yang Dihasilkan

- Food Loss by Country
- Food Loss by Region
- Food Loss by Commodity
- Food Loss by Supply Chain Stage
- Food Loss by Cause
- Food Loss Trend
- Food Loss Summary

---

# 🎯 Tujuan Analitik

| Analisis | Tujuan |
|-----------|-----------|
| Food Loss by Country | Membandingkan tingkat kehilangan pangan antar negara |
| Food Loss by Region | Membandingkan tingkat kehilangan pangan antar wilayah |
| Food Loss by Commodity | Mengidentifikasi komoditas paling rentan terhadap kehilangan pangan |
| Supply Chain Stage Analysis | Menentukan titik kritis kehilangan pangan pada rantai pasok |
| Cause Analysis | Mengidentifikasi penyebab utama food loss |
| Trend Analysis | Menganalisis perubahan food loss dari waktu ke waktu |
| Summary Analysis | Menyajikan ringkasan statistik food loss global |

---

# 📈 Hasil Analisis Utama

## 🌎 Negara dengan Food Loss Tertinggi

| Country | Average Loss (%) |
|----------|----------|
| Australia and New Zealand | 44.00 |
| Haiti | 39.50 |
| Gabon | 35.00 |
| Oman | 35.00 |
| Saint Kitts and Nevis | 30.00 |

### Insight

Australia and New Zealand menunjukkan rata-rata food loss tertinggi sebesar 44%, diikuti Haiti sebesar 39,5%.

---

## 🌾 Komoditas dengan Food Loss Tertinggi

| Commodity | Average Loss (%) |
|----------|----------|
| Snails, Fresh, Chilled | 50.00 |
| Grapefruit Juice | 41.89 |
| Meat of Pig | 40.91 |
| Orange Juice | 40.30 |
| Pineapple Juice | 40.02 |

### Insight

Produk olahan dan produk hewani memiliki tingkat kehilangan pangan yang relatif tinggi dibandingkan komoditas lainnya.

---

## 🚚 Tahapan Rantai Pasok dengan Food Loss Tertinggi

| Stage | Average Loss (%) |
|----------|----------|
| Post-Harvest | 19.76 |
| Households | 15.40 |
| Retail | 11.79 |
| Export | 10.88 |
| Food Services | 10.13 |

### Insight

Tahap Post-Harvest merupakan titik kritis utama kehilangan pangan dalam rantai pasok.

---

## ⚠️ Penyebab Utama Food Loss

| Cause | Average Loss (%) |
|----------|----------|
| Losses in Marine Shipment | 55.00 |
| Rejected Fruits | 50.00 |
| Over-ripeness and Rotting | 50.00 |

### Insight

Transportasi, penyimpanan, dan penanganan pascapanen menjadi faktor dominan penyebab kehilangan pangan.

---

# ✨ Fitur Utama Arsitektur

### Apache Spark Processing

Pipeline dibangun menggunakan Apache Spark untuk mendukung pemrosesan data secara efisien.

### Medallion Architecture

Implementasi Bronze Layer, Silver Layer, dan Gold Layer untuk meningkatkan kualitas serta keterlacakan data.

### Lakehouse Storage

Penyimpanan data bertingkat yang memisahkan data mentah, data bersih, dan data analitik.

### Automated Data Processing

Seluruh proses transformasi dilakukan secara otomatis melalui script PySpark.

### Analytical Data Products

Gold Layer menghasilkan berbagai data produk analitik yang siap digunakan untuk visualisasi dan dashboard.

### Reproducible Pipeline

Pipeline dapat dijalankan ulang secara konsisten menggunakan source code yang tersedia pada repository.

---

# ⚙️ Teknologi yang Digunakan

| Komponen | Teknologi |
|-----------|-----------|
| Programming Language | Python |
| Big Data Processing | Apache Spark |
| Framework | PySpark |
| Storage Format | Parquet |
| Data Architecture | Medallion Architecture |
| Version Control | Git & GitHub |
| Visualization | Power BI |

---

# 📂 Struktur Repository

```text
Kelompok-8-SDG-2-Tanpa-Kelaparan

├── README.md
│
├── proposal
│   └── Proposal_Tubes_ABD.pdf
│
├── data
│   └── food_loss.csv
│
├── lakehouse
│   ├── bronze
│   │   ├── food_loss
│   │   └── bronze_food_loss.parquet
│   │
│   ├── silver
│   │   ├── food_loss
│   │   └── silver_food_loss.parquet
│   │
│   └── gold
│       ├── csv
│       ├── food_loss_by_country
│       ├── food_loss_by_region
│       ├── food_loss_by_commodity
│       ├── food_loss_by_stage
│       ├── food_loss_by_cause
│       ├── food_loss_summary
│       └── food_loss_trend
│
└── src
    ├── read_data.py
    ├── spark_session.py
    ├── bronze_layer.py
    ├── silver_layer.py
    └── gold_layer.py
```

---

# 🚀 Cara Menjalankan Pipeline

### 1. Bronze Layer

```bash
python src/bronze_layer.py
```

### 2. Silver Layer

```bash
python src/silver_layer.py
```

### 3. Gold Layer

```bash
python src/gold_layer.py
```

---

# 👥 Tim Pengembang

### Kelompok 8 – SDG 2 Tanpa Kelaparan
Program Studi Sains Data  
Institut Teknologi Sumatera (ITERA)

- Khoirul Muttoharoh
- Nadya Ratu Anjani
- Erma Daniar Safitri
- Zahra Putri Salsabilla
- Vita Anggraini

---

# 🎯 Luaran Proyek

- Implementasi Medallion Architecture Berbasis Apache Spark
- Bronze Layer Dataset
- Silver Layer Dataset
- Gold Layer Analytical Dataset
- Analisis Food Loss Global
- Dashboard Visualisasi Food Loss
- Insight Pendukung SDG 2: Zero Hunger
- 
