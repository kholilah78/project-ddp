import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def hitung_waktu_dan_jarak():
    try:
        kecepatan = float(entry_kecepatan.get())
        jarak = float(entry_jarak.get())

        waktu_tempuh = jarak / kecepatan
        jarak_tempuh = kecepatan * waktu_tempuh

        label_hasil_waktu["text"] = f"Waktu Tempuh: {waktu_tempuh:.2f} jam"
        label_hasil_jarak["text"] = f"Jarak Tempuh: {jarak_tempuh:.2f} km"
    except ValueError:
        label_hasil_waktu["text"] = "Masukkan angka yang valid untuk kecepatan dan jarak."
        label_hasil_jarak["text"] = ""

# window
root = tk.Tk()
style = ttk.Style('solar')
root.title("Hitung Waktu dan Jarak Tempuh")
lebar = 300
tinggi = 300  # Lebih tinggi untuk menampung hasil jarak tempuh

screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()

newx = int((screenwidth/2) - (lebar/2))
newy = int((screenheight/2) - (tinggi/2))
root.geometry(f"{lebar}x{tinggi}+{newx}+{newy}")
root.resizable(0,0)

# Label Say No To Late
label_say_no = ttk.Label(root,text="Say No To Late",style="TLabel")
label_say_no.pack(pady=5)

# Increase the font size
label_say_no.configure(style="TLabel.TLabel", font=("Helvetica", 20,"bold"))

# input kecepatan
label_kecepatan = ttk.Label(root, text="Kecepatan (km/jam):")
label_kecepatan.pack(padx=10, pady=5, anchor="center")

entry_kecepatan = ttk.Entry(root)
entry_kecepatan.pack(padx=10, pady=5, fill="x")

# input jarak
label_jarak = ttk.Label(root, text="Jarak (km):")
label_jarak.pack(padx=10, pady=5, anchor="center")

entry_jarak = ttk.Entry(root)
entry_jarak.pack(padx=10, pady=5, fill="x")

# tombol
tombol_hitung = ttk.Button(root, text="Hitung", command=hitung_waktu_dan_jarak)
tombol_hitung.pack(pady=10)

# label hasil waktu
label_hasil_waktu = ttk.Label(root, text="")
label_hasil_waktu.pack(pady=5)

# label hasil jarak
label_hasil_jarak = ttk.Label(root, text="")
label_hasil_jarak.pack(pady=5)

root.mainloop()