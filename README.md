# Proyek Pertama: Menyelesaikan Permasalahan Human Resources

## Ringkasan Proyek
Jaya Jaya Maju mengalami attrition rate tinggi (>10%). Tujuan proyek ini:
1. Eksplorasi data karyawan.  
2. Memetakan faktor penyebab keluar (attrition).  
3. Membangun model **Gradient Boosting** untuk prediksi risiko attrition.  
4. Menyediakan script (`prediction.py`) untuk memprediksi lewat antarmuka Streamlit.  

## Struktur Direktori
submission/
├── employee_data_cleaned.csv # Dataset sudah dibersihkan
├── prediction.py # Streamlit app untuk prediksi
├── best_model_gb.joblib # Model terlatih (Gradient Boosting)
├── requirements.txt # Daftar dependensi dengan versi
├── notebook.ipynb # Analisis data & model training
├── README.md # Dokumen ini
└── <username>-dashboard.png

## Cara Menjalankan Notebook
1. Pastikan lingkungan Python terpasang dependensi (lihat `requirements.txt`).  
2. Buka `notebook.ipynb` di Jupyter/Colab.  
3. Jalankan cell secara berurutan untuk EDA, training, dan evaluasi.  

## Cara Menjalankan Streamlit App
1. Install library:
   ```bash
   pip install -r requirements.txt
Pastikan file employee_data_cleaned.csv dan best_model_gb.joblib ada di folder yang sama.

Jalankan:
streamlit run prediction.py

Buka browser di http://localhost:8501.

Isi form, klik Predict Attrition, hasil akan ditampilkan.

Hasil dan Insight (Sementara)
Model Gradient Boosting memiliki performa terbaik pada data testing.

Fitur paling berpengaruh: JobLevel, MonthlyIncome, OverTime.

Contoh Tampilan Aplikasi

Troubleshooting
File tidak ditemukan: Pastikan employee_data_cleaned.csv dan best_model_gb.joblib berada di direktori yang sama dengan prediction.py.

Error encoding/scaling: Jika muncul NaN pada saat prediksi, pastikan file CSV bersih dan kolom input form lengkap sesuai fitur model.

Rencana Selanjutnya
Buat Business Dashboard interaktif (Metabase / Tableau / Looker Studio) dengan data yang sama.

Tulis Kesimpulan & Rekomendasi berbasis insight EDA & model.

Kontak
Nama : Rasyid Alfiansyah

Email: rasyidalfiansyh@gmail.com

Dicoding ID: rasyidalfiansyh
