#Import Library
import streamlit as st
import numpy as np

#Configurate the page
st.set_page_config(layout='centered',
                   page_title="Mini Coding",
                   initial_sidebar_state='expanded'
)
st.sidebar.title("Navigation")
add_sidebar_selectbox = st.sidebar.selectbox("Go to", ('Home','Quadratic Solutions','Contact'))


def home():
    st.header('Quadratic Equation')
    # Explanations
    st.image(
        "https://d1e4pidl3fu268.cloudfront.net/d17c0f85-b9f4-4dc7-bbcf-baeae73d0469/QuadraticEquations.crop_963x721_0,1.preview.png",width=700)
    st.write(
        'Quadratic Equation is an equation that contains the highest power, which is two. '
        'Quadratic equations are used to find the values of the roots of the equation. The roots of quadratic equations are referred to as solutions of quadratic equations.'
        'The standar a quadratic equation is: ')
    st.latex('ax^2+bx+c = 0')
    st.write(
        'where a, b, and c are real numbers and a not equal to 0.')
    st.write(
        'There are several methods in finding solutions to quadratic equations, including the ABC formula.'
    )
    st.image("https://1.bp.blogspot.com/-vDKBiz_c7Lg/Vzf7rpz6oGI/AAAAAAAACYk/1LUhE4o8hoAFTjsfCUjZQemuGWjOrfsFQCLcB/w1200-h630-p-k-no-nu/Untitled.png", width=300)


def rumus_abc():
    #Title
    st.write("# Solution")
    st.write("The solutions of this quadratic equation is given by:")
    #Siderbar
    st.sidebar.header("Manual Input")
    a = st.sidebar.number_input("Coefficient a", min_value=-100.0, max_value=100.0, value=1.0, step=0.01)
    b = st.sidebar.number_input("Coefficient b", min_value=-100.0, max_value=100.0, value=1.0, step=0.01)
    c = st.sidebar.number_input("Coefficient c", min_value=-100.0, max_value=100.0, value=1.0, step=0.01)
    if st.sidebar.button('Calculate!'):
        discriminant = b**2 - 4*a*c
        st.write(f"Discriminant is {discriminant}")
        if discriminant > 0:  # two real roots
            root1 = (-b + np.sqrt(discriminant)) / (2 * a)
            root2 = (-b - np.sqrt(discriminant)) / (2 * a)
            st.write("Discriminant is greater then 0 , we have two real roots:")
            st.write(f"Root 1: {root1}")
            st.write(f"Root 2: {root2}")
        elif discriminant == 0:  # one real root
            root = -b / (2 * a)
            st.write("Discriminant is zero, we have one real root (repeated):")
            st.write(f"Root: {root}")
        else:  # complex number roots
            real_part = -b / (2 * a)
            imaginary_part = np.sqrt(abs(discriminant)) / (2 * a)
            st.write("Discriminant is less then 0, we have a Complex Number roots:")
            st.write(f"Root 1: {real_part} + {imaginary_part}i")
            st.write(f"Root 2: {real_part} - {imaginary_part}i")
def contact():
    st.header('About Me')
    st.image('foto_profil.jpeg', width=500)
    st.write('''
    Saya adalah Mahasiswa yang sedang berkuliah di Universitas Hasanuddin Jurusan Teknik Pertambangan. Semasa kuliah, saya sangat tertarik di bidang data, lebih tepatnya Data Scientist/ AI Engineer.
    Ini adalah Mini Coding sebagai bentuk mini portofolio saya. Terima kasih atas kunjungannya dan jangan sungkan untuk menghubungi saya jika Anda tertarik Mini Coding ini.
    ''')
    st.write('''
    **Contact Me**

    - [LinkedIn]("www.linkedin.com/in/ahmadalfianfaisal")
    - [Instagram]("https://instagram.com/ahmad.alfian.faisal?igshid=NzZlODBkYWE4Ng==")
    - [Github](https://github.com/ahmadalfianfaisal)
    - [Medium](https://medium.com/@ahmadalfianfaisal04)
    ''')

if add_sidebar_selectbox == 'Quadratic Solutions':
    rumus_abc()
elif add_sidebar_selectbox == 'Contact':
    contact()
else:
    home()
