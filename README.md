# Proyek Pertama: Analisis dan Prediksi *Employee Attrition*

## Latar Belakang

Perusahaan **Jaya Jaya Maju** mengalami masalah tingkat *attrition* karyawan \>10%. Proyek ini bertujuan untuk:

1.  Menganalisis faktor-faktor yang mempengaruhi *employee attrition*
2.  Membangun model prediktif untuk mengidentifikasi risiko *attrition*
3.  Membuat *dashboard* prediksi interaktif untuk HR

## Struktur Direktori

├──`employee_data_cleaned.csv`\
├──`model.joblib`\
├──`prediction.py`\
├──`notebook.ipynb`\
├──`metabase.db.mv.db`\
├──`requirements.txt`\
├──`README.md`\
├──`dashboard-preview.png`

## Link ke Dashboard Tableau Public

Anda dapat mengakses dashboard interaktif melalui tautan berikut:

[Jaya Jaya Maju Employees Attrition Dashboard](https://public.tableau.com/views/JayaJayaMajuEmployeesAttritionDashboard/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## Tampilan Dashboard

Berikut adalah tampilan *screenshot* dari *dashboard* yang telah dibuat:

![Tampilan Dashboard](dashboard-preview.png)

## Cara Menjalankan Proyek

### Instalasi

```bash
# Clone repositori
git clone https://github.com/107rasyid/Menyelesaikan-Permasalahan-Human-Resources
```

### Buat virtual environment
```bash
python -m venv venv
```

### Aktifkan virtual environment
### Untuk Linux/MacOS:
```bash
source venv/bin/activate
```

### Untuk Windows:
```bash
.\venv\Scripts\activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

## Menjalankan Aplikasi Predict
```bash
`streamlit run src/prediction.py`
```
Buka *browser* di `http://localhost:8501`\
Isi *form input* sesuai data karyawan\
Klik tombol **Predict Attrition**

## Hasil Analisis

### Faktor Penentu *Attrition*

| Peringkat | Fitur            | Tingkat Pengaruh |
| --------- | ---------------- | ---------------- |
| 1         | `OverTime`       | 11.9%            |
| 2         | `MonthlyIncome`  | 9.65%            |
| 3         | `Age`            | 8.54%            |
| 4         | `DailyRate`      | 8.01%            |
| 5         | `StockOptionLevel` | 7.96%            |

### Performa Model

| Metric    | Training | Testing |
| --------- | -------- | ------- |
| Accuracy  | 0.97     | 0.88    |
| Precision | 0.96     | 0.85    |
| Recall    | 0.98     | 0.89    |
| F1-Score  | 0.97     | 0.87    |

## Kontak

- Nama: Rasyid Alfiansyah
- Email: `rasyidalfiansyh@gmail.com`
- Dicoding ID: rasyidalfiansyh
