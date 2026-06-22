# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

### Latar Belakang Bisnis

Jaya Jaya Institut merupakan salah satu institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan telah menghasilkan banyak lulusan dengan reputasi yang baik. Namun demikian, institusi ini masih menghadapi permasalahan tingginya jumlah mahasiswa yang tidak berhasil menyelesaikan studi atau mengalami dropout.

Tingginya angka dropout dapat memberikan dampak negatif bagi institusi, baik dari sisi reputasi, efektivitas proses pembelajaran, maupun keberhasilan akademik mahasiswa. Oleh karena itu, Jaya Jaya Institut ingin mengidentifikasi mahasiswa yang berpotensi mengalami dropout sedini mungkin agar dapat diberikan pendampingan dan intervensi yang sesuai.

Untuk membantu menyelesaikan permasalahan tersebut, dilakukan analisis data, pembangunan dashboard bisnis, serta pengembangan model machine learning yang mampu memprediksi status akademik mahasiswa berdasarkan data demografis, akademik, sosial, dan ekonomi.

---

## Permasalahan Bisnis

Permasalahan bisnis yang ingin diselesaikan pada proyek ini adalah:

1. Tingginya jumlah mahasiswa yang mengalami dropout.
2. Belum adanya sistem yang mampu mengidentifikasi mahasiswa berisiko dropout secara dini.
3. Sulitnya pihak institusi dalam memantau performa akademik mahasiswa secara menyeluruh.
4. Belum tersedianya dashboard yang dapat membantu pengambilan keputusan berbasis data.
5. Diperlukannya sistem prediksi yang dapat digunakan untuk mengklasifikasikan status akademik mahasiswa menjadi Dropout dan Graduate.

---

## Cakupan Proyek

Cakupan pekerjaan pada proyek ini meliputi:

1. Melakukan data understanding dan exploratory data analysis (EDA).
2. Melakukan data preprocessing dan persiapan data untuk pemodelan.
3. Membangun model machine learning untuk klasifikasi status mahasiswa.
4. Membandingkan beberapa algoritma machine learning:
   - Logistic Regression
   - Decision Tree
   - Random Forest
5. Mengevaluasi performa model menggunakan berbagai metrik klasifikasi.
6. Membuat business dashboard menggunakan Metabase.
7. Mengembangkan prototype sistem machine learning menggunakan Streamlit.
8. Menyediakan dokumentasi dan panduan penggunaan sistem.

---

## Persiapan

### Sumber Data

Dataset yang digunakan pada proyek ini adalah Students' Performance Dataset yang disediakan oleh Dicoding Academy.

Sumber dataset:

https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Dataset ini berisi informasi demografis, akademik, sosial, dan ekonomi mahasiswa yang digunakan untuk memprediksi kemungkinan mahasiswa mengalami dropout atau berhasil lulus (graduate).

### Setup Environment

1. Clone Repository
git clone https://github.com/aqsafirdaus/students-performance.git

    cd students-performance

2. Membuat Virtual Environment

    Windows:

    python -m venv venv

    Linux / MacOS:

    python3 -m venv venv

3. Mengaktifkan Virtual Environment

    Windows:

    venv\Scripts\activate

    Linux / MacOS:

    source venv/bin/activate

4. Install Dependencies
    pip install -r requirements.txt

5. Menjalankan Notebook
    jupyter notebook

    Buka file notebook proyek kemudian jalankan seluruh cell secara berurutan.

6. Menjalankan Prototype Machine Learning
    streamlit run app.py

---

## Business Dashboard

Dashboard bisnis dibuat menggunakan Metabase v0.46.4 untuk membantu institusi memantau performa akademik mahasiswa dan faktor-faktor yang berhubungan dengan risiko dropout.

Dashboard menampilkan beberapa informasi utama, yaitu:

### KPI Overview

- Total Students
- Total Dropout
- Dropout Rate
- Graduate Rate

### Students Performnace Analysis

- Distribution of Student Status
- Status by Average Grade
- Status by Tuition Fees
- Top 5 Dropout Course

### Machine Learning Insight

- Top 5 Dropout Risk Factors

### Filter Dropdown

- Filter Status (Dropout, Enrolled, Graduate)

Dashboard membantu pihak institusi untuk memahami distribusi status mahasiswa, faktor-faktor yang meningkatkan risiko dropout, serta hubungan antara performa akademik dan status mahasiswa.

### Link Dashboard

http://localhost:3000/public/dashboard/4ff2edd0-f3d0-48c9-a0ce-2dde067699e6

### Menjalankan Dashboard Metabase

1. Pull Image Metabase

docker pull metabase/metabase:v0.46.4

2. Jalankan Container Metabase

docker run -d 
-p 3000:3000 
--name metabase 
metabase/metabase:v0.46.4

Linux/MacOS:

docker run -d \
-p 3000:3000 \
--name metabase \
metabase/metabase:v0.46.4

3. Salin Database Dashboard ke Container

Pastikan file berikut tersedia pada folder proyek:

metabase.db.mv.db

Kemudian salin ke container:

docker cp metabase.db.mv.db metabase:/metabase.db.mv.db

4. Restart Container
docker restart metabase

5. Akses Dashboard

Buka browser:

http://localhost:3000

---

## Model Machine Learning

Pada proyek ini digunakan tiga algoritma klasifikasi:

1. Logistic Regression
2. Decision Tree
3. Random Forest

Berdasarkan hasil evaluasi, model Logistic Regression dipilih sebagai model terbaik karena memiliki kemampuan yang lebih baik dalam mendeteksi performa akademik mahasiswa yang berpotensi mengalami dropout.

Model yang telah dilatih disimpan dalam file:

```text
model.pkl
```

## Menjalankan Sistem Machine Learning

Prototype machine learning dibuat menggunakan Streamlit dan menggunakan model Logistic Regression yang telah dilatih menggunakan dataset Students' Performance. Berikut cara menjalankan aplikasi sreamlit:

1. Jalankan aplikasi Streamlit menggunakan perintah:

```bash
streamlit run app.py
```

2. Buka aplikasi melalui browser.

3. Lengkapi seluruh informasi mahasiswa pada form yang tersedia, meliputi:

   - Student Demographics
   - Academic Background
   - Family Information
   - Financial Information
   - Academic Performance Semester 1
   - Academic Performance Semester 2
   - Economic Indicators

4. Untuk fitur kategorikal, pilih kategori yang sesuai dari dropdown yang tersedia, seperti:

   - Marital Status
   - Gender
   - Course
   - Application Mode
   - Scholarship Holder
   - Debtor
   - Tuition Fees Up To Date
   - Daytime/Evening Attendance

5. Untuk fitur numerik, masukkan nilai sesuai kondisi mahasiswa, seperti:

   - Age at Enrollment
   - Admission Grade
   - Previous Qualification Grade
   - Semester Grades
   - GDP
   - Inflation Rate
   - Unemployment Rate

6. Setelah seluruh data terisi, klik tombol:

```text
🔍 Predict Student Status
```

### Hasil Prediksi

Setelah proses prediksi selesai, sistem akan menampilkan:

#### 1. Prediction Result

Status akademik mahasiswa yang diprediksi oleh model:

- ⚠️ High Risk of Dropout
- 🎓 Likely to Graduate

#### 2. Prediction Confidence

Progress bar yang menunjukkan tingkat keyakinan model terhadap hasil prediksi.

#### 3. Class Probabilities

Persentase probabilitas untuk setiap kelas:

- Dropout
- Graduate

Contoh:

| Status | Probability |
|----------|----------|
| Dropout  | 65.23% |
| Graduate | 22.32% |

#### 4. General Dropout Risk Factors

Sistem juga menampilkan faktor-faktor yang secara umum memiliki pengaruh terbesar terhadap risiko dropout berdasarkan analisis Logistic Regression, yaitu:

- 📚 Curricular Units 2nd Semester Approved
- 📖 Curricular Units 1st Semester Approved
- 💰 Tuition Fees Up to Date
- 📝 Curricular Units 2nd Semester Grade
- 🌍 International Student Status

Informasi ini dapat membantu pihak institusi memahami faktor-faktor utama yang perlu diperhatikan untuk mencegah mahasiswa mengalami dropout.

### Link Prototype Streamlit

https://students-performance-aqsafirdaus.streamlit.app/

---

## Conclusion

Berdasarkan hasil eksplorasi data diketahui bahwa sekitar 32% mahasiswa pada dataset mengalami dropout, sedangkan hampir 50% mahasiswa berhasil lulus (graduate). Hal ini menunjukkan bahwa dropout merupakan permasalahan yang cukup signifikan dan perlu mendapatkan perhatian khusus dari institusi.

Dari hasil pemodelan, Logistic Regression menghasilkan performa terbaik dengan accuracy sebesar 91,46%. Model ini mampu mengklasifikasikan kelas Graduate dan Dropout dengan baik, masing-masing memperoleh F1-score sebesar 0,93 dan 0,88. Random Forest menunjukkan performa yang kompetitif, sedangkan Decision Tree menghasilkan performa terendah.

Analisis feature importance menunjukkan bahwa faktor yang paling berpengaruh terhadap risiko dropout adalah:

- Curricular Units 2nd Semester Approved
- Curricular Units 1st Semester Approved
- Tuition Fees Up to Date
- Curricular Units 2nd Semester Grade
- International Student Status

Hasil tersebut menunjukkan bahwa performa akademik mahasiswa, pembayaran uang kuliah dan  status internasional mahasiswa merupakan faktor utama yang berkaitan dengan kemungkinan mahasiswa mengalami dropout.

Dengan demikian, model Logistic Regression dapat digunakan sebagai sistem pendukung keputusan untuk membantu institusi mengidentifikasi mahasiswa berisiko dropout lebih awal sehingga tindakan pencegahan dapat dilakukan secara tepat.

---

## Rekomendasi Action Items

### 1. Implementasi Early Warning System

Gunakan model machine learning yang telah dibangun untuk mengidentifikasi mahasiswa dengan risiko dropout tinggi sejak awal masa studi sehingga pihak akademik dapat melakukan intervensi lebih cepat.

### 2. Monitoring Performa Akademik Secara Berkala

Lakukan pemantauan rutin terhadap nilai akademik semester pertama dan kedua karena faktor tersebut terbukti menjadi indikator utama risiko dropout.

### 3. Program Pendampingan Akademik

Berikan mentoring, tutoring, atau konseling akademik kepada mahasiswa yang memiliki performa akademik rendah atau mengalami kesulitan menyelesaikan mata kuliah.

### 4. Monitoring Mahasiswa dengan Faktor Risiko Tinggi

Fokuskan perhatian pada mahasiswa yang memiliki karakteristik serupa dengan faktor risiko utama yang ditemukan oleh model, seperti performa akademik mahasiswa 

### 5. Integrasi Dashboard dan Sistem Prediksi

Integrasikan dashboard bisnis dan sistem machine learning ke dalam proses monitoring institusi agar pengambilan keputusan dapat dilakukan secara lebih cepat dan berbasis data.
