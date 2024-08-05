import tkinter as tk
from tkinter import messagebox

class Inventario:
    def __init__(self, tablas, trajes):
        self.tablas = tablas
        self.trajes = trajes
        self.historial_pedidos = []

    def añadir_tablas(self, cantidad):
        self.tablas += cantidad

    def añadir_trajes(self, cantidad):
        self.trajes += cantidad

    def restar_tablas(self, cantidad):
        if self.tablas >= cantidad:
            self.tablas -= cantidad
        else:
            raise ValueError("No hay suficientes tablas en inventario.")

    def restar_trajes(self, cantidad):
        if self.trajes >= cantidad:
            self.trajes -= cantidad
        else:
            raise ValueError("No hay suficientes trajes en inventario.")
            
    def puede_realizar_pedido(self, tablas, trajes):
        return self.tablas >= tablas and self.trajes >= trajes

class InterfazInventario:
    def __init__(self, master, inventario):
        self.master = master
        self.inventario = inventario
        self.master.title("Gestión de Inventario")
        self.master.configure(bg='slategray')

        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        
        window_width = 500
        window_height = 400
        
        position_top = int(screen_height/2 - window_height/2)
        position_right = int(screen_width/2 - window_width/2)
        
        self.master.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        
        # Columnas de inventario y pedidos
        self.frame_inventario = tk.Frame(master, bg='slategray')
        self.frame_inventario.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.label_tablas = tk.Label(self.frame_inventario, text="Tablas disponibles:", bg='turquoise4')
        self.label_tablas.pack(pady=(0, 10))
        
        self.label_trajes = tk.Label(self.frame_inventario, text="Trajes disponibles:", bg='turquoise4')
        self.label_trajes.pack(pady=(0, 30))

        self.label_pedido = tk.Label(self.frame_inventario, text="Ingrese pedido (Tablas, Trajes):", bg='dark turquoise')
        self.label_pedido.pack(pady=(0, 5))

        self.entry_pedido = tk.Entry(self.frame_inventario, bg='lavender')
        self.entry_pedido.pack(pady=(0, 10))

        self.boton_procesar = tk.Button(self.frame_inventario, text="Procesar Pedido", command=self.procesar_pedido)
        self.boton_procesar.pack(pady=(0, 20))
        
        self.label_añadir_tablas = tk.Label(self.frame_inventario, text="Añadir Tablas:", bg='dark turquoise')
        self.label_añadir_tablas.pack(pady=(0, 5))

        self.entry_añadir_tablas = tk.Entry(self.frame_inventario, bg='lavender')
        self.entry_añadir_tablas.pack(pady=(0, 10))

        self.boton_añadir_tablas = tk.Button(self.frame_inventario, text="Añadir Tablas", command=self.añadir_tablas)
        self.boton_añadir_tablas.pack(pady=(0, 20))
        
        self.label_añadir_trajes = tk.Label(self.frame_inventario, text="Añadir Trajes:", bg='dark turquoise')
        self.label_añadir_trajes.pack(pady=(0, 5))

        self.entry_añadir_trajes = tk.Entry(self.frame_inventario, bg='lavender')
        self.entry_añadir_trajes.pack(pady=(0, 10))

        self.boton_añadir_trajes = tk.Button(self.frame_inventario, text="Añadir Trajes", command=self.añadir_trajes)
        self.boton_añadir_trajes.pack(pady=(0, 20))
        
        # Columna de historial de pedidos
        self.frame_historial = tk.Frame(master, bg='slategray')
        self.frame_historial.pack(side=tk.RIGHT, padx=10, pady=10)
        
        self.label_historial = tk.Label(self.frame_historial, text="Historial de Pedidos:", bg='dark turquoise')
        self.label_historial.pack()
        
        self.text_historial = tk.Text(self.frame_historial, width=40, height=20, bg='lavender')
        self.text_historial.pack()
        
        self.actualizar_labels()
        
    def actualizar_labels(self):
        self.label_tablas.config(text=f"Tablas disponibles: {self.inventario.tablas}")
        self.label_trajes.config(text=f"Trajes disponibles: {self.inventario.trajes}")
        
    def procesar_pedido(self):
        try:
            pedido = self.entry_pedido.get()
            tablas, trajes = map(int, pedido.split(','))
            if self.inventario.puede_realizar_pedido(tablas, trajes):
                self.inventario.restar_tablas(tablas)
                self.inventario.restar_trajes(trajes)
                resultado = "Entregado"
            else:
                resultado = "No entregado"
                
            self.inventario.historial_pedidos.append((tablas, trajes, resultado))
            self.actualizar_historial()
            
            if resultado == "Entregado":
                messagebox.showinfo("Éxito", "Pedido procesado con éxito.")
            else:
                messagebox.showwarning("Fallo", "No hay suficiente inventario para este pedido.")
                
            self.actualizar_labels()
            self.entry_pedido.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def añadir_tablas(self):
        try:
            cantidad = int(self.entry_añadir_tablas.get())
            self.inventario.añadir_tablas(cantidad)
            self.actualizar_labels()
            messagebox.showinfo("Éxito", f"Se han añadido {cantidad} tablas.")
            self.entry_añadir_tablas.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def añadir_trajes(self):
        try:
            cantidad = int(self.entry_añadir_trajes.get())
            self.inventario.añadir_trajes(cantidad)
            self.actualizar_labels()
            messagebox.showinfo("Éxito", f"Se han añadido {cantidad} trajes.")
            self.entry_añadir_trajes.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
    def actualizar_historial(self):
        self.text_historial.delete(1.0, tk.END)
        for pedido in self.inventario.historial_pedidos:
            tablas, trajes, resultado = pedido
            self.text_historial.insert(tk.END, f"Tablas: {tablas}, Trajes: {trajes} - {resultado}\n")

if __name__ == "__main__":
    inventario = Inventario(5, 5)  
    root = tk.Tk()
    app = InterfazInventario(root, inventario)
    root.mainloop()
