python generador_contraseñas.py
import tkinter as tk
from tkinter import messagebox
import random
import string

# --- Función principal ---
def generar_contraseña():
    try:
        longitud = int(entry_longitud.get())
        if longitud < 4 or longitud > 40:
            messagebox.showwarning("Advertencia", "La longitud debe estar entre 4 y 40 caracteres.")
            return
        
        incluir_mayus = var_mayus.get()
        incluir_minus = var_minus.get()
        incluir_nums = var_nums.get()
        incluir_simb = var_simb.get()

        caracteres = ""
        if incluir_mayus:
            caracteres += string.ascii_uppercase
        if incluir_minus:
            caracteres += string.ascii_lowercase
        if incluir_nums:
            caracteres += string.digits
        if incluir_simb:
            caracteres += string.punctuation

        if not caracteres:
            messagebox.showerror("Error", "Debe seleccionar al menos una opción de caracteres.")
            return

        contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, contraseña)
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido para la longitud.")

# --- Función para copiar la contraseña ---
def copiar_contraseña():
    contraseña = entry_resultado.get()
    if contraseña:
        ventana.clipboard_clear()
        ventana.clipboard_append(contraseña)
        messagebox.showinfo("Copiado", "Contraseña copiada al portapapeles.")
    else:
        messagebox.showwarning("Atención", "No hay contraseña generada para copiar.")

# --- Interfaz Gráfica ---
ventana = tk.Tk()
ventana.title("Generador de Contraseñas Seguras")
ventana.geometry("400x400")
ventana.config(bg="#0d1b2a")

# --- Título ---
titulo = tk.Label(ventana, text="🔐 Generador de Contraseñas", font=("Arial", 16, "bold"), bg="#0d1b2a", fg="white")
titulo.pack(pady=10)

# --- Entrada de longitud ---
tk.Label(ventana, text="Longitud de la contraseña:", bg="#0d1b2a", fg="white").pack(pady=5)
entry_longitud = tk.Entry(ventana, width=10, justify="center")
entry_longitud.pack(pady=5)

# --- Opciones ---
var_mayus = tk.BooleanVar()
var_minus = tk.BooleanVar()
var_nums = tk.BooleanVar()
var_simb = tk.BooleanVar()

tk.Checkbutton(ventana, text="Incluir mayúsculas", variable=var_mayus, bg="#0d1b2a", fg="white").pack(anchor="w", padx=80)
tk.Checkbutton(ventana, text="Incluir minúsculas", variable=var_minus, bg="#0d1b2a", fg="white").pack(anchor="w", padx=80)
tk.Checkbutton(ventana, text="Incluir números", variable=var_nums, bg="#0d1b2a", fg="white").pack(anchor="w", padx=80)
tk.Checkbutton(ventana, text="Incluir símbolos", variable=var_simb, bg="#0d1b2a", fg="white").pack(anchor="w", padx=80)

# --- Botón de generar ---
btn_generar = tk.Button(ventana, text="Generar Contraseña", command=generar_contraseña, bg="#1b263b", fg="white", width=20)
btn_generar.pack(pady=15)

# --- Resultado ---
tk.Label(ventana, text="Contraseña generada:", bg="#0d1b2a", fg="white").pack()
entry_resultado = tk.Entry(ventana, width=40, justify="center")
entry_resultado.pack(pady=5)

# --- Botón copiar ---
btn_copiar = tk.Button(ventana, text="Copiar Contraseña", command=copiar_contraseña, bg="#1b263b", fg="white", width=20)
btn_copiar.pack(pady=10)

# --- Footer ---
footer = tk.Label(ventana, text="Proyecto Integrador - Ciberseguridad 2025", bg="#0d1b2a", fg="#778da9", font=("Arial", 8))
footer.pack(side="bottom", pady=5)

ventana.mainloop() 
