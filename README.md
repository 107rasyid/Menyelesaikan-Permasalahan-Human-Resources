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
└── <username>-dashboard.png # Screenshot dashboard (belum dibuat)

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
