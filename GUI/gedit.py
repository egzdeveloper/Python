import tkinter as tk
from tkinter import filedialog, messagebox

class SimpleTextEditor:
    def __init__(self, root):
        self.root = root
        self.text_area = tk.Text(self.root)
        self.text_area.pack(fill=tk.BOTH, expand=1)
        self.current_file = ''

    def new_file(self):
        self.current_file = ''
        self.text_area.delete("1.0", tk.END)

    def open_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            with open(filename, "r") as file:
                self.text_area.delete("1.0", tk.END)
                file.read(self.text_area.insert("1.0", file.read()))

            self.current_file = filename

    def save_file(self):
        if not self.current_file:
            file_path = filedialog.asksaveasfilename()
            if file_path:
                self.current_file = file_path
            else:
                return

            with open(self.current_file, "w") as file:
                file.write(self.text_area.get("1.0", tk.END))


    def quit_confirm(self):
        if messagebox.askokcancel("Salir", "¿Estas seguro de que deseas salir?"):
            self.root.destroy()

root = tk.Tk()
root.geometry("700x500")

editor = SimpleTextEditor(root)

menu_bar = tk.Menu(root)
menu_options = tk.Menu(menu_bar, tearoff=False)
menu_options.add_command(label="Nuevo", command=editor.new_file)
menu_options.add_command(label="Abrir", command=editor.open_file)
menu_options.add_command(label="Guardar", command=editor.save_file)
menu_options.add_command(label="Salir", command=editor.quit_confirm)

root.config(menu=menu_bar)
menu_bar.add_cascade(label="Archivo", menu=menu_options)

root.mainloop()