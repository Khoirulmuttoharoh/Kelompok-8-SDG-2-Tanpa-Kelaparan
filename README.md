# 📊 Food Loss Analytics Pipeline

### Implementasi Medallion Architecture untuk Analisis Food Loss Database FAO

Repositori ini berisi implementasi Data Engineering Pipeline yang dirancang untuk mengelola, membersihkan, dan menganalisis data Food Loss Database dari Food and Agriculture Organization (FAO).

Proyek ini berfokus pada pembangunan pipeline data menggunakan pendekatan Medallion Architecture (Bronze, Silver, Gold) untuk menghasilkan data yang terstruktur, berkualitas, dan siap digunakan dalam proses analisis maupun visualisasi.

---

# 🌍 Latar Belakang

Food loss merupakan salah satu tantangan utama dalam rantai pasok pangan global. Kehilangan pangan yang terjadi sejak tahap produksi hingga distribusi berdampak pada:

- Ketahanan pangan global
- Efisiensi ekonomi sektor pangan
- Keberlanjutan lingkungan
- Pencapaian SDG 2: Zero Hunger

Melalui proyek ini, data food loss dari berbagai negara dianalisis untuk mengidentifikasi pola kehilangan pangan berdasarkan wilayah, komoditas, tahapan rantai pasok, penyebab kehilangan, dan tren waktu.

---

# 🏗️ Arsitektur Sistem (Medallion Architecture)

```text
Food Loss Database (FAO)
            │
            ▼
     🥉 Bronze Layer
       (Raw Data)
            │
            ▼
     🥈 Silver Layer
     (Cleaned Data)
            │
            ▼
      🥇 Gold Layer
   (Analytical Data)
            │
            ▼
     📊 Dashboard & Insight
```

---
---

# 📁 Struktur Repository

```text
Kelompok-8-SDG-2-Tanpa-Kelaparan
│
├── data
│   └── food_loss.csv
│
├── src
│   ├── spark_session.py
│   ├── read_data.py
│   ├── bronze_layer.py
│   ├── silver_layer.py
│   ├── gold_layer.py
│   └── test_write.py
│
├── lakehouse
│   ├── bronze
│   │   ├── bronze_food_loss.parquet
│   │   └── food_loss/
│   │
│   ├── silver
│   │   ├── silver_food_loss.parquet
│   │   └── food_loss/
│   │
│   └── gold
│       ├── csv
│       │   ├── food_loss_by_country.csv
│       │   ├── food_loss_by_region.csv
│       │   ├── food_loss_by_commodity.csv
│       │   ├── food_loss_by_stage.csv
│       │   ├── food_loss_by_cause.csv
│       │   └── food_loss_trend.csv
│       │
│       ├── food_loss_by_country
│       ├── food_loss_by_region
│       ├── food_loss_by_commodity
│       ├── food_loss_by_stage
│       ├── food_loss_by_cause
│       ├── food_loss_summary
│       └── food_loss_trend
│
└── README.md
```

### Keterangan Folder

| Folder | Fungsi |
|----------|----------|
| data | Dataset mentah Food Loss Database FAO |
| src | Source code pipeline ETL |
| lakehouse/bronze | Data mentah hasil ingest |
| lakehouse/silver | Data hasil cleaning dan validasi |
| lakehouse/gold | Data agregasi siap analisis |
| lakehouse/gold/csv | Output CSV untuk dashboard dan visualisasi |

# 🥉 Bronze Layer (Raw Data)

Bronze Layer berfungsi sebagai penyimpanan data mentah hasil ingest dari sumber data FAO.

### Aktivitas

- Membaca dataset CSV
- Menambahkan metadata ingest
- Menyimpan data dalam format Parquet
- Menjaga integritas data asli

### Output

```text
bronze_food_loss.parquet
```

---

# 🥈 Silver Layer (Cleaned Data)

Silver Layer berfungsi meningkatkan kualitas data melalui proses pembersihan dan validasi.

### Aktivitas

- Menghapus data duplikat
- Menangani missing values
- Memvalidasi nilai loss percentage
- Standarisasi atribut
- Menyiapkan data untuk analisis

### Output

```text
silver_food_loss.parquet
```

---

# 🥇 Gold Layer (Analytical Data)

Gold Layer menghasilkan dataset analitik yang siap digunakan untuk eksplorasi data dan dashboard.

### Output

```text
food_loss_by_country.csv
food_loss_by_region.csv
food_loss_by_commodity.csv
food_loss_by_stage.csv
food_loss_by_cause.csv
food_loss_trend.csv
```

---

# 🎯 Tujuan Analitik & KPI

Pipeline ini dibangun untuk mendukung beberapa analisis utama terkait food loss global.

| Analisis | Tujuan | KPI |
|-----------|-----------|-----------|
| Food Loss by Country | Membandingkan tingkat food loss antar negara | Average Loss Percentage |
| Food Loss by Region | Membandingkan food loss antar wilayah | Average Loss Percentage |
| Food Loss by Commodity | Mengidentifikasi komoditas paling rentan | Average Loss Percentage |
| Supply Chain Analysis | Menentukan titik kritis kehilangan pangan | Average Loss Percentage |
| Cause Analysis | Mengidentifikasi penyebab utama food loss | Average Loss Percentage |
| Trend Analysis | Menganalisis perubahan food loss tahunan | Annual Average Loss |

---

# 📈 Hasil Analisis Utama

## 🌎 Negara dengan Food Loss Tertinggi

| Country | Avg Loss (%) |
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

| Commodity | Avg Loss (%) |
|----------|----------|
| Snails, Fresh, Chilled | 50.00 |
| Grapefruit Juice | 41.89 |
| Meat of Pig | 40.91 |
| Orange Juice | 40.30 |
| Pineapple Juice | 40.02 |

### Insight

Produk olahan dan produk hewani memiliki tingkat kehilangan pangan yang relatif tinggi dibanding komoditas lainnya.

---

## 🚚 Tahapan Rantai Pasok dengan Food Loss Tertinggi

| Supply Stage | Avg Loss (%) |
|----------|----------|
| Post-Harvest | 19.76 |
| Households | 15.40 |
| Retail | 11.79 |
| Export | 10.88 |
| Food Services | 10.13 |

### Insight

Tahap Post-Harvest menjadi titik kritis utama kehilangan pangan.

---

## ⚠️ Penyebab Utama Food Loss

| Cause | Avg Loss (%) |
|----------|----------|
| Losses in Marine Shipment | 55.00 |
| Rejected Fruits | 50.00 |
| Over-ripeness & Rotting | 50.00 |

### Insight

Transportasi dan penyimpanan menjadi faktor dominan penyebab kehilangan pangan.

---

# ✨ Fitur Utama Arsitektur

### Automated Data Cleaning

Pembersihan data dilakukan secara otomatis melalui Silver Layer untuk menghasilkan dataset yang konsisten dan siap dianalisis.

### Medallion Architecture

Pemisahan data ke dalam Bronze, Silver, dan Gold Layer untuk meningkatkan kualitas dan keterlacakan data.

### Parquet-Based Storage

Format penyimpanan yang efisien untuk proses ETL dan analitik.

### Dashboard Ready Dataset

Output Gold Layer dapat langsung digunakan pada Power BI maupun dashboard analitik lainnya.

### Dockerized Environment

Pipeline dijalankan dalam container Docker untuk memastikan reproducibility dan konsistensi lingkungan eksekusi.

---

# ⚙️ Teknologi yang Digunakan

| Komponen | Teknologi |
|-----------|-----------|
| Data Processing | Python |
| Data Manipulation | Pandas |
| Containerization | Docker |
| Storage Format | Parquet |
| Version Control | Git & GitHub |
| Visualization | Power BI |

---

# 🚀 Cara Menjalankan Pipeline

### Menjalankan Docker

```bash
docker compose up -d
```

### Bronze Layer

```bash
python /app/bronze.py
```

### Silver Layer

```bash
python /app/silver.py
```

### Gold Layer

```bash
python /app/gold.py
```

---

# 👥 Tim Pengembang

### Kelompok 8 – SDG 2 Tanpa Kelaparan
Program Studi Sains Data – Institut Teknologi Sumatera (ITERA)

- Khoirul Muttoharoh — Lead Data Engineer
- Nadya Ratu Anjani — Data Engineer
- Erma Daniar Safitri — Data Engineer
- Zahra Putri Salsabilla — Data Analyst
- Vita Anggraini — Data Analyst

---

# 🎯 Luaran Proyek

- Pipeline Medallion Architecture
- Bronze Dataset
- Silver Dataset
- 6 Gold Analytical Tables
- Dashboard Visualisasi Food Loss
- Insight untuk mendukung SDG 2 Zero Hunger
