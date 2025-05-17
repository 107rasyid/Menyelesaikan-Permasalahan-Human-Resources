# Proyek Pertama: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju

## Business Understanding
Perusahaan **Jaya Jaya Maju**, yang bergerak di bidang edutech dan pengembangan sumber daya manusia, menghadapi masalah tingginya tingkat employee attrition atau pengunduran diri karyawan secara sukarela. Angka attrition melebihi 10% dan dikhawatirkan akan memengaruhi produktivitas serta efisiensi perusahaan secara keseluruhan.

## Permasalahan Bisnis
Perusahaan Jaya Jaya Maju mengalami tingkat employee attrition yang tinggi, melebihi 10% dalam setahun terakhir. Tingginya tingkat attrition ini menyebabkan berbagai dampak negatif terhadap keberlangsungan bisnis, seperti:
- Peningkatan biaya rekrutmen dan pelatihan karyawan baru
- Penurunan produktivitas dan beban kerja yang meningkat pada tim yang ditinggalkan
- Hilangnya pengetahuan dan keahlian penting dalam organisasi

Namun, perusahaan belum memiliki sistem yang mampu:
- Mengidentifikasi secara dini karyawan dengan risiko attrition tinggi
- Menganalisis faktor-faktor utama yang menyebabkan attrition
- Menyediakan alat bantu pengambilan keputusan berbasis data bagi tim HR

Oleh karena itu, diperlukan sebuah solusi berbasis data untuk memahami akar masalah dan mendukung strategi retensi karyawan secara proaktif.

## Cakupan Proyek
- Eksplorasi dan analisis data karyawan.
- Pembuatan model prediktif untuk attrition.
- Visualisasi data dan hasil prediksi dalam bentuk dashboard Tableau.
- Deployment model prediktif menggunakan Streamlit.

## Persiapan
Sumber data: Data yang digunakan dalam proyek ini berasal dari Employee Data yang memuat berbagai informasi terkait karyawan, seperti usia, departemen, tingkat pendidikan, pendapatan bulanan, serta apakah karyawan tersebut mengalami attrition (keluar dari perusahaan) atau tidak. Sebelum digunakan untuk analisis, data ini terlebih dahulu dibersihkan menggunakan Notebook. Setelah proses ini, diperoleh Cleaned Employee Data yang siap digunakan dalam proses eksplorasi data, pemodelan prediktif, serta pembuatan visualisasi interaktif untuk mendukung pengambilan keputusan oleh tim HR.

Setup environment:
```
# Clone repositori
git clone https://github.com/107rasyid/Menyelesaikan-Permasalahan-Human-Resources

# Membuat virtual environment
python -m venv venv

# Mengaktifkan virtual environment
# Untuk Linux/MacOS
source venv/bin/activate
# Untuk Windows
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Business Dashboard
Dashboard ini dirancang untuk menampilkan visualisasi analisis faktor penyebab attrition, distribusi demografi karyawan, serta insight lainnya berdasarkan departemen, peran kerja, dan usia. Dashboard ini mempermudah tim HR dalam membuat keputusan berbasis data.

Anda dapat mengakses dashboard interaktif melalui tautan berikut:

[Jaya Jaya Maju Employees Attrition Dashboard](https://public.tableau.com/views/JayaJayaMajuEmployeesAttritionDashboard/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## Tampilan Dashboard

Berikut adalah tampilan *screenshot* dari *dashboard* yang telah dibuat:

![Tampilan Dashboard](dashboard-preview.png)

## Hasil Analisis
### Faktor Penentu *Attrition*

| Peringkat | Fitur            | Tingkat Pengaruh |
| --------- | ---------------- | ---------------- |
| 1         | `OverTime`       | 11.9%            |
| 2         | `MonthlyIncome`  | 9.65%            |
| 3         | `Age`            | 8.54%            |
| 4         | `DailyRate`      | 8.01%            |
| 5         | `StockOptionLevel` | 7.96%            |

### Performa Model Prediksi *Attrition*
Model *Gradient Boosting Classifier* dimanfaatkan untuk memprediksi risiko seorang karyawan meninggalkan perusahaan (*attrition*). Proses pelatihan model ini melibatkan analisis data karyawan yang ada, dengan mengandalkan serangkaian **fitur utama sebagai input prediksi**. Melalui pembelajaran dari pola data historis, model ini mampu mengidentifikasi karyawan dengan karakteristik serupa dengan mereka yang telah mengalami *attrition* sebelumnya.

### Performa Model
| Metric    | Training | Testing |
| --------- | -------- | ------- |
| Accuracy  | 0.97     | 0.88    |
| Precision | 0.96     | 0.85    |
| Recall    | 0.98     | 0.89    |
| F1-Score  | 0.97     | 0.87    |

## Conclusion
Berdasarkan analisis data karyawan, beberapa faktor signifikan berkontribusi terhadap tingkat *attrition* di perusahaan Jaya Jaya Maju.

* **Faktor Pengaruh Utama:** *OverTime* menjadi faktor dengan tingkat kepentingan tertinggi dalam memprediksi *attrition* (0.119), diikuti oleh *MonthlyIncome* (0.097), *Age* (0.085), *DailyRate* (0.081), dan *StockOptionLevel* (0.080).
* **Demografi Karyawan:** Mayoritas pekerja adalah laki-laki dan sebagian besar telah menikah dengan tingkat pendidikan sarjana sebagai yang dominan.
* **Attrition Rate Berdasarkan Departemen:** Departemen *Sales* menunjukkan tingkat *attrition* tertinggi (20.69%), diikuti oleh *Human Resources* (15.79%) dan *Research & Development* (15.26%).
* **Attrition Berdasarkan Peran:** Posisi *Sales Representative* memiliki tingkat *attrition* tertinggi (43.10%), diikuti oleh *Laboratory Technician* (26.06%) dan *Human Resources* (20.00%).
* **Attrition Rate Berdasarkan Usia:** Pekerja dengan usia muda (terutama rentang 15-24 tahun) memiliki tingkat *attrition* yang lebih tinggi (60.00% untuk 15-19 dan 36.36% untuk 20-24). Tingkat *attrition* cenderung menurun seiring bertambahnya usia, namun kembali meningkat pada kelompok usia 55-59 tahun (17.65%).
* **Keterlibatan Kerja:** Karyawan dengan tingkat keterlibatan kerja rendah memiliki kecenderungan *attrition* yang lebih tinggi.
* **Work-Life Balance:** Karyawan dengan *work-life balance* rendah memiliki tingkat *attrition* tertinggi.
* **Kepuasan Kerja:** Tingkat kepuasan kerja yang rendah berkorelasi dengan tingkat *attrition* yang lebih tinggi.
* **OverTime:** Karyawan yang sering bekerja lembur memiliki tingkat *attrition* yang jauh lebih tinggi (31.92%) dibandingkan dengan mereka yang tidak (10.79%).
* **StockOptionLevel:** Tingkat opsi saham 0 memiliki tingkat *attrition* tertinggi (25.69%).

## Rekomendasi Action Items (Optional)

Berdasarkan kesimpulan di atas, perusahaan Jaya Jaya Maju dapat mempertimbangkan tindakan berikut:

1.  **Intervensi Terkait OverTime:** Evaluasi beban kerja dan kebijakan lembur, pertimbangkan kompensasi atau insentif tambahan untuk lembur, atau cari cara untuk mengurangi kebutuhan lembur.
2.  **Strategi Retensi untuk Departemen dan Peran dengan Attrition Tinggi:** Kembangkan strategi retensi yang ditargetkan untuk departemen *Sales* dan posisi *Sales Representative*, *Laboratory Technician*, dan *Human Resources*.
3.  **Program untuk Karyawan Usia Muda:** Implementasikan program yang mendukung karyawan di awal karir mereka, seperti mentoring, peluang pengembangan, dan peningkatan keterlibatan.
4.  **Fokus pada Keterlibatan dan Kepuasan Kerja:** Investasikan dalam inisiatif untuk meningkatkan keterlibatan kerja dan kepuasan kerja karyawan secara keseluruhan, dengan perhatian khusus pada mereka yang melaporkan tingkat keterlibatan dan kepuasan yang rendah.
5.  **Promosikan Work-Life Balance:** Tinjau dan tingkatkan kebijakan dan budaya kerja untuk mendukung *work-life balance* karyawan.
6.  **Evaluasi Kebijakan Opsi Saham:** Pertimbangkan kembali kebijakan opsi saham untuk membuatnya lebih menarik, terutama bagi karyawan yang belum memiliki opsi saham.
7.  **Analisis Lebih Lanjut:** Lakukan analisis lebih mendalam untuk memahami alasan spesifik di balik tingkat *attrition* yang tinggi di departemen, peran, dan kelompok usia tertentu.

## Menjalankan Aplikasi Predict
```bash
`streamlit run src/prediction.py`
```
Buka *browser* di `http://localhost:8501`\
Isi *form input* sesuai data karyawan\
Klik tombol **Predict Attrition**

## Kontak

- Nama: Rasyid Alfiansyah
- Email: `rasyidalfiansyh@gmail.com`
- Dicoding ID: rasyidalfiansyh
