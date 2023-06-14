import pickle
import streamlit as st

# membaca model
sleep_model = pickle.load(open('sleep_model.sav', 'rb'))

#judul web
st.title('Prediksi Kualitas Tidur')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    Gender = st.number_input ('Jenis kelamin orang tersebut (Pria 0 & Wanita = 1).')
    Age = st.number_input ('Input Umur')
    SD = st.number_input ('Input Jumlah jam tidur per hari')
    QOS = st.number_input ('Input penilaian subjektif dari kualitas tidur (Skala 1 - 10)')
    PAL = st.number_input ('Input Jumlah aktivitas fisik setiap hari (menit/hari)')
    Systolic = st.number_input ('Input Nilai Tekanan Darah (Systolic)')

with col2:
    Diastolic = st.number_input ('Input Nilai Tekanan Darah (Diastolic)')
    SL = st.number_input ('Input Penilaian subjektif tingkat stres (Skala 1 - 10)')
    BMI = st.number_input ('Input Kategori BMI (Normal = 0, Berat Badan Berlebih = 1, Obesitas = 2)')
    HR = st.number_input ('Input Denyut jantung istirahat (denyut/menit)')
    DS = st.number_input ('Input Jumlah langkah per hari')

# code untuk prediksi
sleep_kualitas = ''
sleep_kualitas2 = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi sleep'):
    sleep_predict = sleep_model.predict([[Gender, Age, SD, QOS, PAL, Systolic,
                                          Diastolic, SL, BMI, HR, DS]])

    if sleep_predict == 0:
        sleep_kualitas = 'Kualitas Tidur Termasuk Kedalam Kategori Normal'
    elif sleep_predict == 1:
        sleep_kualitas = 'Kualitas Tidur Termasuk Kedalam Kategori Sleep Apnea'
    else:
        sleep_kualitas = 'Kualitas Tidur Termasuk Kedalam Kategori Insomnia'

    if sleep_predict == 0:
        sleep_kualitas2 = 'Kualitas tidur mu sudah normal, pertahankan yaa!'
    elif sleep_predict == 1:
        sleep_kualitas2 = 'Sepertinya kamu perlu latihan fisik dan penurunan berat badan nih'
    else:
        sleep_kualitas2 = 'Perbanyak olahraga dan jaga pola hidup untuk kualitas tidur yang lebih baik yap!'

st.write(sleep_kualitas)
st.write("Saran: " + sleep_kualitas2)
