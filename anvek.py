import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# -------------------------------
# KONFIGURASI HALAMAN
# -------------------------------
st.set_page_config(page_title="Transformasi Koordinat 3D", layout="wide")
st.title("🧭 Transformasi Koordinat dalam Ruang 3D")
st.markdown("""
Proyek ini memvisualisasikan transformasi antara sistem koordinat **Kartesian**, **Silinder**, dan **Sferis**.  
Masukkan koordinat Kartesian (x, y, z) di sebelah kiri untuk melihat hasil transformasi dan visualisasinya secara interaktif.
""")

# -------------------------------
# INPUT KOORDINAT
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    st.header("🧮 Input Koordinat Kartesian")
    x = st.number_input("x", value=1.0, step=0.1, format="%.2f")
    y = st.number_input("y", value=1.0, step=0.1, format="%.2f")
    z = st.number_input("z", value=1.0, step=0.1, format="%.2f")

# -------------------------------
# FUNGSI TRANSFORMASI
# -------------------------------
def kartesian_ke_silinder(x, y, z):
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return r, theta, z

def silinder_ke_kartesian(r, theta, z):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y, z

def kartesian_ke_sferis(x, y, z):
    rho = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arctan2(y, x)
    phi = np.arccos(z / rho)
    return rho, theta, phi

def sferis_ke_kartesian(rho, theta, phi):
    x = rho * np.sin(phi) * np.cos(theta)
    y = rho * np.sin(phi) * np.sin(theta)
    z = rho * np.cos(phi)
    return x, y, z

# -------------------------------
# TRANSFORMASI KOORDINAT
# -------------------------------
r, theta_sil, z_sil = kartesian_ke_silinder(x, y, z)
rho, theta_sfer, phi = kartesian_ke_sferis(x, y, z)

x_sil, y_sil, z_sil = silinder_ke_kartesian(r, theta_sil, z_sil)
x_sfer, y_sfer, z_sfer = sferis_ke_kartesian(rho, theta_sfer, phi)

# -------------------------------
# HASIL TRANSFORMASI
# -------------------------------
with col2:
    st.header("📊 Hasil Transformasi")
    st.subheader("Koordinat Silinder")
    st.write(f"r = {r:.3f}, θ = {np.degrees(theta_sil):.2f}°, z = {z:.3f}")
    
    st.subheader("Koordinat Sferis")
    st.write(f"ρ = {rho:.3f}, θ = {np.degrees(theta_sfer):.2f}°, φ = {np.degrees(phi):.2f}°")

    st.caption("Nilai sudut ditampilkan dalam derajat untuk kemudahan interpretasi.")

# -------------------------------
# VISUALISASI 3D
# -------------------------------
st.markdown("---")
st.header("📌 Visualisasi 3D Transformasi Koordinat")

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, color='blue', s=40, label='Kartesian (input)')
ax.scatter(x_sil, y_sil, z_sil, color='green', s=40, label='Silinder → Kartesian')
ax.scatter(x_sfer, y_sfer, z_sfer, color='red', s=40, label='Sferis → Kartesian')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Hasil Visualisasi Titik dalam Ruang 3D")
ax.legend()
ax.grid(True)

#Agar tumpukan lebih kelihatan beri transparansi
ax.scatter(x, y, z, color='blue', s=40, alpha=0.8, label='Kartesian (input)')
ax.scatter(x_sil, y_sil, z_sil, color='green', s=40, alpha=0.8, label='Silinder → Kartesian')
ax.scatter(x_sfer, y_sfer, z_sfer, color='red', s=40, alpha=0.8, label='Sferis → Kartesian')

st.pyplot(fig)

# -------------------------------
# CATATAN TAMBAHAN
# -------------------------------
with st.expander("📘 Penjelasan"):
    st.write("""
    - Program ini mengubah satu titik dari sistem koordinat Kartesian ke sistem Silinder dan Sferis.
    - Hasil transformasi ditampilkan baik secara **numerik** maupun **visual**.
    - **Titik biru** adalah input awal, **titik hijau** adalah hasil dari konversi Silinder→Kartesian, dan **titik merah** adalah hasil dari Sferis→Kartesian.
    """)

