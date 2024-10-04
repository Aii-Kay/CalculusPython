import sympy as sp

def hitung_limit_kanan_kiri(fungsi_str, titik):
    """
    Menghitung limit kanan dan kiri dari sebuah fungsi bagian di titik tertentu.
    
    Parameters:
    fungsi_str (str): Fungsi-fungsi dengan kondisi, dipisahkan dengan koma (contoh: '(x-2)/(x+3) jika x<1, x**2 + 3*x jika x>=1')
    titik (float/int): Titik di mana limit akan dihitung.
    
    Returns:
    tuple: Limit kanan dan kiri dari fungsi pada titik yang diberikan.
    """
    # Mendefinisikan variabel
    x = sp.Symbol('x')
    
    # Memisahkan fungsi berdasarkan koma
    fungsi_kondisi_list = fungsi_str.split(',')
    
    # Daftar untuk menyimpan kondisi fungsi
    kondisi_pieces = []
    
    # Loop untuk setiap fungsi dengan kondisi
    for fungsi_kondisi in fungsi_kondisi_list:
        # Memisahkan fungsi dan kondisinya
        if "jika" in fungsi_kondisi:
            fungsi_part, kondisi_part = fungsi_kondisi.split("jika")
            fungsi = sp.sympify(fungsi_part.strip())  # Mengubah fungsi menjadi simbolik
            kondisi = sp.sympify(kondisi_part.strip())  # Mengubah kondisi menjadi simbolik
            kondisi_pieces.append((fungsi, kondisi))  # Menambahkan fungsi dan kondisinya ke daftar
        else:
            # Jika tidak ada kondisi, anggap fungsi berlaku secara umum
            fungsi = sp.sympify(fungsi_kondisi.strip())
            kondisi_pieces.append((fungsi, True))  # Kondisi 'True' berarti berlaku umum
    
    # Menggunakan Piecewise untuk mendefinisikan fungsi bagian
    fungsi_piecewise = sp.Piecewise(*kondisi_pieces)
    
    # Menghitung limit kanan (x mendekati titik dari kanan)
    limit_kanan = sp.limit(fungsi_piecewise, x, titik, dir='+')
    
    # Menghitung limit kiri (x mendekati titik dari kiri)
    limit_kiri = sp.limit(fungsi_piecewise, x, titik, dir='-')
    
    # Mengembalikan hasil limit kanan dan kiri
    return limit_kanan, limit_kiri

# Contoh penggunaan:

    # Fungsi dengan kondisi
fungsi_str = '(x-2)/(x+3) jika x<1, x**2 + 3*x jika x>=1'
    
    # Titik di mana limit akan dihitung
titik = 1
    
    # Menghitung limit kanan dan kiri
limit_kanan, limit_kiri = hitung_limit_kanan_kiri(fungsi_str, titik)
    
    # Menampilkan hasil
print(f"Limit kanan dari f(x) ketika x mendekati {titik} adalah {limit_kanan}")
print(f"Limit kiri dari f(x) ketika x mendekati {titik} adalah {limit_kiri}")