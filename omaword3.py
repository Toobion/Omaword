from tkinter import Tk, scrolledtext, filedialog, messagebox, ttk
import tkinter as tk
from docx import Document

class TextProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Processor")

        # Notebook (Tabs)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both")

        # Tab 1: Main Document
        self.tab_document = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_document, text="Document")

        # Text widget for main document
        self.text_widget = scrolledtext.ScrolledText(self.tab_document, wrap="word", undo=True)
        self.text_widget.pack(expand=True, fill="both")

        # Tab 2: Phrases
        self.tab_phrases = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_phrases, text="Phrases")

        # Text widget for phrases
        self.phrases_widget = scrolledtext.ScrolledText(self.tab_phrases, wrap="word", undo=True)
        self.phrases_widget.pack(expand=True, fill="both")

        # Tab 3: Formatting Options
        self.tab_formatting = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_formatting, text="Formatting")

        # Formatting buttons
        bold_button = ttk.Button(self.tab_formatting, text="Bold", command=self.apply_bold)
        italic_button = ttk.Button(self.tab_formatting, text="Italic", command=self.apply_italic)
        underline_button = ttk.Button(self.tab_formatting, text="Underline", command=self.apply_underline)

        bold_button.grid(row=0, column=0, padx=5, pady=5)
        italic_button.grid(row=0, column=1, padx=5, pady=5)
        underline_button.grid(row=0, column=2, padx=5, pady=5)

        # Menu bar
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Export to DOCX", command=self.export_to_docx)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.destroy)

    def new_file(self):
        self.text_widget.delete(1.0, tk.END)
        self.phrases_widget.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, content)

    def save_file(self):
        if hasattr(self, "current_file"):
            with open(self.current_file, "w") as file:
                file.write(self.text_widget.get(1.0, tk.END))
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_widget.get(1.0, tk.END))
            self.current_file = file_path

    def export_to_docx(self):
        content = self.text_widget.get(1.0, tk.END)
        document = Document()
        document.add_paragraph(content)
        docx_file = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word files", "*.docx")])
        if docx_file:
            document.save(docx_file)

    def apply_bold(self):
        self.text_widget.tag_add("bold", self.text_widget.index(tk.SEL_FIRST), self.text_widget.index(tk.SEL_LAST))
        self.text_widget.tag_configure("bold", font=("Helvetica", 12, "bold"))

    def apply_italic(self):
        self.text_widget.tag_add("italic", self.text_widget.index(tk.SEL_FIRST), self.text_widget.index(tk.SEL_LAST))
        self.text_widget.tag_configure("italic", font=("Helvetica", 12, "italic"))

    def apply_underline(self):
        self.text_widget.tag_add("underline", self.text_widget.index(tk.SEL_FIRST), self.text_widget.index(tk.SEL_LAST))
        self.text_widget.tag_configure("underline", underline=True)

if __name__ == "__main__":
    root = Tk()
    app = TextProcessorApp(root)
    root.mainloop()

