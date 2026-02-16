# 🫁 Lung Cancer Risk Prediction System

**Lung Cancer Risk** adalah aplikasi berbasis web yang dirancang untuk memprediksi tingkat risiko kanker paru-paru menggunakan algoritma Machine Learning (**Logistic Regression**). Aplikasi ini bertujuan untuk membantu pengambilan keputusan medis secara lebih cepat dan akurat melalui analisis data pasien.

<img width="704" height="512" alt="Screenshot 2026-02-16 143625" src="https://github.com/user-attachments/assets/a3e33802-1064-46f5-96ac-2d262efd5daa" />


## ✨ Fitur Utama

### 1. 🏠 Halaman Utama (Home)
Menampilkan ringkasan sistem, tujuan proyek, dan statistik model (seperti jumlah data yang diproses dan fitur yang dianalisis).

<img width="840" height="497" alt="Screenshot 2026-02-16 143728" src="https://github.com/user-attachments/assets/d71f76a1-7af7-44c2-a187-0914df10f326" />

### 2. 📊 Dashboard Analitik
Visualisasi data interaktif untuk memahami distribusi data latih:
* Total Record Data (1,000 data).
* Rata-rata Usia Pasien.
* **Donut Chart:** Distribusi Tingkat Risiko (High, Medium, Low).
* **Bar Chart:** Hubungan antara kelompok umur dengan tingkat risiko.

<img width="700" height="495" alt="Screenshot 2026-02-16 143801" src="https://github.com/user-attachments/assets/ecc6ad71-6b14-4bac-a493-ef9b540f15f0" />

### 3. 🔍 Sistem Prediksi (Prediction)
Formulir interaktif dimana pengguna dapat memasukkan parameter kesehatan untuk mendapatkan prediksi risiko kanker paru-paru secara langsung.
* **Input Features (11 Parameter):**
    * Age (Usia)
    * Coughing of Blood (Batuk Berdarah)
    * Dust Allergy (Alergi Debu)
    * Passive Smoker (Perokok Pasif)
    * Occupational Hazards (Bahaya Pekerjaan)
    * Air Pollution (Polusi Udara)
    * Chronic Lung Disease (Penyakit Paru Kronis)
    * Shortness of Breath (Sesak Napas)
    * Dry Cough (Batuk Kering)
    * Snoring (Mendengkur)
    * Swallowing Difficulty (Kesulitan Menelan)

## 🛠️ Teknologi yang Digunakan

Proyek ini dibangun menggunakan teknologi berikut:

* **Bahasa Pemrograman:** Python 3.x
* **Web Framework:** [Flask](https://flask.palletsprojects.com/)
* **Machine Learning:** Scikit-Learn (Logistic Regression)
* **Frontend:** HTML5, CSS3, JavaScript
* **Deployment & Containerization:** Docker, Vercel
* **Model Format:** Pickle (`.pkl`)
