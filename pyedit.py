import tkinter as tk
from tkinter import filedialog as f

class PyEdit:
    def __init__(self, root):
        self.root = root
        self.root.title("PyEdit")
        self.text_area = tk.Text(self.root, wrap="word")
        self.text_area.pack(expand=1, fill="both")
        self.create_menu()
    def create_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        save = tk.Button(root, text="Save File", command=self.save_file)
        save.pack(pady=5)
    
    def save_file(self):
        file_path = f.asksaveasfilename(defaultextension=".py",
        filetypes=[("Python Files", "*.py"),
        ("Text Files", "*.txt")])
        
        
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_area.get("1.0", tk.END))
if __name__ == "__main__":
    root = tk.Tk()
    editor = PyEdit(root)
    root.mainloop()
