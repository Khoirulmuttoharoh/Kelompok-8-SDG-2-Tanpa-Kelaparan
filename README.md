# 📊 Food Loss Lakehouse Pipeline
### Analisis Tren Food Loss Lintas Negara Berdasarkan Komoditas dan Tahapan Rantai Pasok Pangan Menggunakan Medallion Architecture Berbasis Apache Spark

Repositori ini berisi implementasi pipeline Data Engineering berbasis **Medallion Architecture** untuk mengelola dan menganalisis **Food Loss Database FAO**. Proyek bertujuan membangun arsitektur data yang terstruktur melalui Bronze Layer, Silver Layer, dan Gold Layer sehingga menghasilkan data analitik yang siap digunakan untuk eksplorasi dan visualisasi.

---

# 🌍 Latar Belakang

Food loss merupakan salah satu tantangan utama dalam rantai pasok pangan global. Kehilangan pangan yang terjadi sejak tahap produksi hingga distribusi berdampak pada:

- Ketahanan pangan global
- Efisiensi ekonomi sektor pangan
- Keberlanjutan lingkungan
- Pencapaian SDG 2: Zero Hunger

Melalui proyek ini dilakukan analisis food loss berdasarkan negara, wilayah, komoditas, tahapan rantai pasok, penyebab kehilangan, dan tren tahunan menggunakan pendekatan Data Lakehouse.

---

# 🏗️ Arsitektur Lakehouse (Medallion Architecture)

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

# 🥉 Bronze Layer

Bronze Layer berfungsi sebagai lapisan penyimpanan data mentah hasil ingest dari sumber data.

### Aktivitas

- Membaca dataset Food Loss FAO
- Menyimpan data mentah tanpa transformasi
- Menjaga integritas data sumber

### Output

```text
lakehouse/bronze/
```

---

# 🥈 Silver Layer

Silver Layer bertanggung jawab terhadap peningkatan kualitas data.

### Aktivitas

- Menghapus duplikasi
- Menangani missing values
- Memvalidasi atribut numerik
- Standarisasi atribut

### Output

```text
lakehouse/silver/
```

---

# 🥇 Gold Layer

Gold Layer menghasilkan dataset analitik yang siap digunakan untuk eksplorasi data dan dashboard.

### Analisis yang Dihasilkan

- Food Loss by Country
- Food Loss by Region
- Food Loss by Commodity
- Food Loss by Supply Chain Stage
- Food Loss by Cause
- Food Loss Trend

### Output

```text
lakehouse/gold/
```

---

# 🎯 Tujuan Analitik

| Analisis | Tujuan |
|-----------|-----------|
| Food Loss by Country | Membandingkan tingkat kehilangan pangan antar negara |
| Food Loss by Region | Membandingkan tingkat kehilangan pangan antar wilayah |
| Food Loss by Commodity | Mengidentifikasi komoditas paling rentan |
| Supply Chain Stage Analysis | Menentukan titik kritis kehilangan pangan |
| Cause Analysis | Mengidentifikasi penyebab utama food loss |
| Trend Analysis | Menganalisis tren food loss dari waktu ke waktu |

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

---

## 🌾 Komoditas dengan Food Loss Tertinggi

| Commodity | Average Loss (%) |
|----------|----------|
| Snails, Fresh, Chilled | 50.00 |
| Grapefruit Juice | 41.89 |
| Meat of Pig | 40.91 |
| Orange Juice | 40.30 |
| Pineapple Juice | 40.02 |

---

## 🚚 Tahapan Rantai Pasok dengan Food Loss Tertinggi

| Stage | Average Loss (%) |
|----------|----------|
| Post-Harvest | 19.76 |
| Households | 15.40 |
| Retail | 11.79 |
| Export | 10.88 |
| Food Services | 10.13 |

---

## ⚠️ Penyebab Utama Food Loss

| Cause | Average Loss (%) |
|----------|----------|
| Losses in Marine Shipment | 55.00 |
| Rejected Fruits | 50.00 |
| Over-ripeness and Rotting | 50.00 |

---

# ⚙️ Teknologi yang Digunakan

| Komponen | Teknologi |
|-----------|-----------|
| Data Processing | PySpark |
| Big Data Framework | Apache Spark |
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
│   ├── silver
│   └── gold
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

### Bronze Layer

```bash
python src/bronze_layer.py
```

### Silver Layer

```bash
python src/silver_layer.py
```

### Gold Layer

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

- Implementasi Medallion Architecture
- Bronze Layer Dataset
- Silver Layer Dataset
- Gold Layer Dataset
- Analisis Food Loss Global
- Dashboard Visualisasi Food Loss
- Insight untuk mendukung SDG 2 Zero Hunger
