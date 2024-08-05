import tkinter as tk
from tkinter import ttk

def calcular_tendencia(temp_ayer, temp_anteayer):
    diferencia = temp_ayer - temp_anteayer
    if diferencia > 0:
        return "positiva"
    elif diferencia < 0:
        return "negativa"
    else:
        return "neutra"

def calcular_tendencias(semanas):
    resultados = []
    for semana in semanas:
        semana_resultado = []
        for i in range(1, len(semana)):
            tendencia = calcular_tendencia(semana[i], semana[i-1])
            semana_resultado.append(tendencia)
        resultados.append(semana_resultado)
    return resultados

def calcular_porcentaje_aciertos(semanas):
    tendencias = calcular_tendencias(semanas)
    aciertos = 0
    total_dias = 0

    for i, semana in enumerate(semanas):
        for j in range(1, len(semana)):
            if tendencias[i][j-1] == "positiva" and semana[j] > semana[j-1]:
                aciertos += 1
            elif tendencias[i][j-1] == "negativa" and semana[j] < semana[j-1]:
                aciertos += 1
            total_dias += 1

    return (aciertos / total_dias) * 100

def mostrar_tabla(semanas, tendencias, porcentaje_aciertos):
    root = tk.Tk()
    root.title("Tendencias de Temperatura")
    root.configure(background="slategray")

    cols = ["Día", "Temperatura", "Tendencia"]
    for i, semana in enumerate(semanas):
        frame = tk.Frame(root, padx=30, relief="solid", borderwidth=2, background="slate gray")
        frame.grid(row=0, column=i, sticky=(tk.W, tk.E))
        label = tk.Label(frame, text=f"Semana {i+1}", background="turquoise4", width=20, anchor="center")
        label.grid(row=0, column=0, columnspan=3)
        
        for col in range(3):
            header = ttk.Label(frame, text=cols[col], padding=(5, 5), background="dark turquoise", anchor="center")
            header.grid(row=1, column=col, padx=10, pady=5)

        for j in range(len(semana)):
            dia = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"][j]
            temps = semana[j]
            temp = f"{temps}°"
            tendencia = ""
            if j > 0:
                tendencia = tendencias[i][j-1]
            
            row_color = "lightgreen" if tendencia == "positiva" else "lightcoral" if tendencia == "negativa" else "white"
            
            ttk.Label(frame, text=dia, padding=(5,5), anchor="center", background="lavender").grid(row=j+2, column=0, sticky="ew")
            ttk.Label(frame, text=temp, padding=(5,5), anchor="center", background="lavender").grid(row=j+2, column=1, padx=5, pady=2)
            ttk.Label(frame, text=tendencia, padding=(5,5), anchor="center", background=row_color).grid(row=j+2, column=2, sticky="ew")

    ttk.Label(root, text=f"Porcentaje de aciertos: {porcentaje_aciertos:.2f}%", background="lavender").grid(row=1, columnspan=len(semanas), pady=10)

    root.update_idletasks()
    
    ancho_ventana = root.winfo_width()
    alto_ventana = root.winfo_height()
    
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()
    
    pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    pos_y = (alto_pantalla // 2) - (alto_ventana // 2)

    root.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

    root.mainloop()

semanas = [
    [19, 21, 20, 23, 25, 27, 29],
    [31, 30, 30, 33, 32, 30, 27],
    [23, 24, 22, 19, 18, 22, 22]
]

porcentaje_aciertos = calcular_porcentaje_aciertos(semanas)
tendencias = calcular_tendencias(semanas)
mostrar_tabla(semanas, tendencias, porcentaje_aciertos)
