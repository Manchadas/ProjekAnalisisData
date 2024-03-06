import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
df_day = pd.read_csv('data/day.csv')

# Sidebar
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Home', 'Data Summary', 'Conclusion'])

if page == 'Home':
    st.title('Bike Sharing System Data Analysis')
    st.header('Final Project Immanuel Samosir')
    st.image('pitcures/bikerent.jpg', use_column_width=True)

    st.write('Dashboard ini dibuat untuk menganalisis data sistem peminjaman sepeda berdasarkan dataset Bike Sharing. Melalui dashboard ini, Anda dapat menjawab dua pertanyaan utama:')

    st.write('1. Bagaimana pola penggunaan sepeda pada sistem peminjaman sepeda berdasarkan musim dan hari kerja? Anda akan melihat bagaimana pola peminjaman sepeda berubah sepanjang tahun tergantung pada musim dan apakah itu hari kerja atau hari libur.')
    st.write('2. Apakah faktor cuaca mempengaruhi jumlah peminjaman sepeda? Dashboard ini juga akan membantu Anda memahami bagaimana kondisi cuaca memengaruhi keputusan orang untuk meminjam sepeda.')

    st.write('Dashboard ini menggunakan data dari [Kaggle dataset](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset) oleh Lakshmi N Pathi. Dengan dashboard ini, Anda akan mendapatkan wawasan yang mendalam tentang bagaimana musim, hari kerja, dan cuaca memengaruhi pola penggunaan sepeda dalam sistem peminjaman sepeda.')


elif page == 'Data Summary':
    st.title('Data Summary')


    st.write("Distribusi jumlah peminjaman sepeda berdasarkan musim:")
    fig, ax = plt.subplots()
    sns.barplot(x='season', y='cnt', data=df_day, ax=ax)
    ax.set_xlabel('Musim')
    ax.set_ylabel('Jumlah Peminjaman')
    st.pyplot(fig)

    st.write("Pola penggunaan sepeda berdasarkan musim dan hari kerja:")
    fig, ax = plt.subplots()
    sns.barplot(x='season', y='cnt', hue='workingday', data=df_day, ax=ax)
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Peminjaman')
    plt.legend(title='Hari Kerja', loc='upper right')
    st.pyplot(fig)

    st.write("Pengaruh faktor cuaca terhadap jumlah peminjaman sepeda:")
    weather_counts = df_day['weathersit'].value_counts().reset_index()
    weather_counts.columns = ['Faktor Cuaca', 'Jumlah Peminjaman']
    st.write(weather_counts)

    st.write("Korelasi antara faktor cuaca dan jumlah peminjaman sepeda:")
    correlation = df_day[['weathersit', 'cnt']].corr()
    st.write(correlation)

    st.write("Visualisasi korelasi:")
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Korelasi antara faktor cuaca dan jumlah peminjaman sepeda')
    st.pyplot()

elif page == 'Conclusion':
    st.header('Kesimpulan Analisis')
    
    st.subheader('Kesimpulan Pertanyaan 1')
    st.markdown("""
    Berdasarkan analisis data, dapat disimpulkan bahwa pola penggunaan sepeda pada sistem peminjaman sepeda dipengaruhi oleh musim dan hari kerja. Secara khusus, pola tersebut dapat dijelaskan sebagai berikut:

    **Pola Penggunaan Sepeda Berdasarkan Musim:**
    - Musim ketiga (fall) memiliki jumlah peminjaman sepeda tertinggi.
    - Musim kedua (summer) memiliki jumlah peminjaman sepeda tertinggi kedua.
    - Musim keempat (winter) memiliki jumlah peminjaman sepeda tertinggi ketiga.
    - Musim pertama (spring) memiliki jumlah peminjaman sepeda paling sedikit.

    **Pola Penggunaan Sepeda Berdasarkan Musim dan Hari Kerja:**
    - Pada musim pertama (spring), peminjaman sepeda cenderung lebih tinggi pada hari kerja dibandingkan dengan hari libur.
    - Untuk musim-musim lainnya, pola peminjaman sepeda cenderung serupa antara hari kerja dan hari libur.

    Dengan demikian, dapat dikatakan bahwa faktor musim memengaruhi pola penggunaan sepeda pada sistem peminjaman sepeda.
    """)

    st.subheader('Kesimpulan Pertanyaan 2')
    st.markdown("""
    Berdasarkan hasil analisis, faktor cuaca memiliki pengaruh terhadap jumlah peminjaman sepeda. Dapat dilihat dari distribusi jumlah peminjaman sepeda berdasarkan faktor cuaca, di mana cuaca dengan kode 1 (Clear, Few clouds, Partly cloudy, Partly cloudy) memiliki jumlah peminjaman sepeda tertinggi, diikuti oleh cuaca dengan kode 2 (Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist), dan cuaca dengan kode 3 (Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds) memiliki jumlah peminjaman sepeda yang paling sedikit.

    Selain itu, korelasi antara faktor cuaca dan jumlah peminjaman sepeda menunjukkan adanya korelasi negatif yang lemah, yaitu sebesar -0.30. Hal ini menunjukkan bahwa semakin buruk cuaca (dengan nilai weathersit yang lebih tinggi), jumlah peminjaman sepeda cenderung lebih rendah. Meskipun korelasinya lemah, namun secara statistik ada hubungan antara faktor cuaca dengan jumlah peminjaman sepeda.

    Kesimpulannya, faktor cuaca memiliki pengaruh terhadap jumlah peminjaman sepeda, di mana cuaca yang lebih baik cenderung meningkatkan jumlah peminjaman sepeda, sedangkan cuaca yang buruk cenderung mengurangi jumlah peminjaman sepeda. Namun, pengaruh ini tidak bersifat kuat, sehingga terdapat faktor lain yang juga memengaruhi jumlah peminjaman sepeda.
    """)