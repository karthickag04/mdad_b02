import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from tkinter import scrolledtext

class NotepadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.root.geometry("800x600")
        
        # Initialize variables
        self.file_path = None
        
        # Setup the GUI
        self.setup_menu()
        self.setup_text_widget()
        self.setup_text_undo_redo()

    def setup_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_separator()
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Close", command=self.close_file)
        
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Select All", command=self.select_all)
        file_menu.add_separator()
        edit_menu.add_command(label="Copy", command=self.copy_text)
        edit_menu.add_command(label="Cut", command=self.cut_text)
        edit_menu.add_command(label="Paste", command=self.paste_text)
        file_menu.add_separator()
        edit_menu.add_command(label="Undo", command=self.undo)
        edit_menu.add_command(label="Redo", command=self.redo)
        
        view_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="Word Wrap", command=self.toggle_word_wrap)
    
    def setup_text_widget(self):
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD)
        self.text_area.pack(expand=1, fill='both')
    
    def setup_text_undo_redo(self):
        # Enable undo and redo functionality
        self.text_area.config(undo=True)
        self.text_area.bind('<Control-z>', self.undo)
        self.text_area.bind('<Control-y>', self.redo)
    
    def new_file(self):
        if self.text_area.get("1.0", tk.END).strip():
            if messagebox.askyesno("Notepad", "Do you want to save changes?"):
                self.save_file()
        self.text_area.delete("1.0", tk.END)
        self.file_path = None
    
    def open_file(self):
        if self.text_area.get("1.0", tk.END).strip():
            if messagebox.askyesno("Notepad", "Do you want to save changes?"):
                self.save_file()
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text files", "*.txt"),
                                                          ("All files", "*.*")])
        if file_path:
            self.file_path = file_path
            with open(file_path, 'r') as file:
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, file.read())
    
    def save_file(self):
        if not self.file_path:
            self.file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                         filetypes=[("Text files", "*.txt"),
                                                                    ("All files", "*.*")])
        if self.file_path:
            with open(self.file_path, 'w') as file:
                file.write(self.text_area.get("1.0", tk.END))
    
    def close_file(self):
        if self.text_area.get("1.0", tk.END).strip():
            if messagebox.askyesno("Notepad", "Do you want to save changes?"):
                self.save_file()
        self.root.quit()
    
    def select_all(self):
        self.text_area.tag_add(tk.SEL, "1.0", tk.END)
        self.text_area.mark_set(tk.INSERT, "1.0")
        self.text_area.see(tk.INSERT)
    
    def copy_text(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST))
    
    def cut_text(self):
        self.copy_text()
        self.text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)
    
    def paste_text(self):
        self.text_area.insert(tk.INSERT, self.root.clipboard_get())
    
    def undo(self, event=None):
        self.text_area.edit_undo()
    
    def redo(self, event=None):
        self.text_area.edit_redo()
    
    def toggle_word_wrap(self):
        current_wrap = self.text_area.cget('wrap')
        new_wrap = tk.WORD if current_wrap == tk.NONE else tk.NONE
        self.text_area.config(wrap=new_wrap)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()
