import tkinter as tk
from tkinter import filedialog
import pandas as pd

class ExcelCreator:
    def __init__(self, root):
        self.root = root
        self.root.title("Creador de Excel")
        self.root.geometry("400x200")

        self.name_label = tk.Label(root, text="Nombre del archivo:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.next_button = tk.Button(root, text="Siguiente", command=self.open_data_entry_window)
        self.next_button.pack()

    def open_data_entry_window(self):
        name = self.name_entry.get()

        if not name:
            tk.messagebox.showwarning("Advertencia", "Por favor, ingrese un nombre de archivo.")
            return

        self.root.withdraw()

        data_entry_window = tk.Tk()
        data_entry_window.title("Ingreso de Datos")
        data_entry_window.geometry("400x200")

        self.num_data_label = tk.Label(data_entry_window, text="Cantidad de datos:")
        self.num_data_label.pack()
        self.num_data_entry = tk.Entry(data_entry_window)
        self.num_data_entry.pack()

        self.save_button = tk.Button(data_entry_window, text="Guardar datos", command=self.save_data)
        self.save_button.pack()

        data_entry_window.protocol("WM_DELETE_WINDOW", self.show_main_window)

    def show_main_window(self):
        self.root.deiconify()
        self.root.focus_set()

    def save_data(self):
        num_data = self.num_data_entry.get()

        if not num_data:
            tk.messagebox.showwarning("Advertencia", "Por favor, ingrese la cantidad de datos.")
            return

        try:
            num_data = int(num_data)
        except ValueError:
            tk.messagebox.showwarning("Advertencia", "La cantidad de datos debe ser un número entero.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Archivos Excel", "*.xlsx")], initialfile=f"{self.name_entry.get()}.xlsx")

        if not file_path:
            return

        data = {"Nombre": [], "Apellido": []}

        for i in range(num_data):
            data["Nombre"].append(f"Nombre {i+1}")
            data["Apellido"].append(f"Apellido {i+1}")

        df = pd.DataFrame(data)

        try:
            df.to_excel(file_path, index=False)
            tk.messagebox.showinfo("Éxito", "El archivo Excel se ha creado correctamente.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"No se pudo crear el archivo Excel. Error: {str(e)}")

root = tk.Tk()
excel_creator = ExcelCreator(root)
root.mainloop()
