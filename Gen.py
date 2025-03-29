import tkinter as tk
from tkinter import ttk, messagebox, filedialog  
import random
import string
import pyperclip
from tkinter.font import Font

class CozyDarkPasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("500x620")
        
        # Color 
        self.bg_color = '#2D3741'  
        self.main_color = '#E67E22'  
        self.accent_color = '#3498DB'  
        self.text_color = '#ECF0F1'  
        self.widget_bg = '#3D4A54'  
        
        # Fonts
        self.title_font = Font(family="Georgia", size=20, weight="bold")
        self.label_font = Font(family="Verdana", size=10)
        self.button_font = Font(family="Verdana", size=10, weight="bold")
        self.password_font = Font(family="Courier New", size=12, weight="bold")
        
        # Configure window
        self.root.configure(bg=self.bg_color)
        self.setup_ui()

    def setup_ui(self):
        # Main 
        main_frame = tk.Frame(self.root, bg=self.bg_color, padx=25, pady=25)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title 
        title_frame = tk.Frame(main_frame, bg=self.bg_color)
        title_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(
            title_frame,
            text="Password gerator",
            font=self.title_font,
            fg=self.main_color,
            bg=self.bg_color
        ).pack()
        
        # Subtitle
        tk.Label(
            title_frame,
            text="Secure passwords",
            font=self.label_font,
            fg=self.accent_color,
            bg=self.bg_color
        ).pack()
        
        # Slider
        length_frame = tk.Frame(main_frame, bg=self.bg_color)
        length_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(
            length_frame,
            text="Password Length:",
            font=self.label_font,
            fg=self.text_color,
            bg=self.bg_color
        ).pack(anchor='w')
        
        self.length_var = tk.IntVar(value=14)
        ttk.Scale(
            length_frame,
            from_=8,
            to=32,
            variable=self.length_var,
            command=lambda v: self.length_display.config(text=f"{int(float(v))}")
        ).pack(fill=tk.X, pady=5)
        
        self.length_display = tk.Label(
            length_frame,
            text="14",
            font=self.label_font,
            fg=self.main_color,
            bg=self.bg_color
        )
        self.length_display.pack(anchor='e')
        
        # Character Types
        char_frame = tk.LabelFrame(
            main_frame,
            text=" Ingredients ",
            font=self.label_font,
            fg=self.text_color,
            bg=self.widget_bg,
            bd=0,
            relief=tk.GROOVE,
            padx=10,
            pady=10
        )
        char_frame.pack(fill=tk.X, pady=10)
        
        # Checkboxes
        self.uppercase_var = tk.BooleanVar(value=True)
        tk.Checkbutton(
            char_frame,
            text="Uppercase (A-Z)",
            variable=self.uppercase_var,
            font=self.label_font,
            fg=self.text_color,
            bg=self.widget_bg,
            selectcolor=self.main_color,
            activebackground=self.widget_bg,
            activeforeground=self.text_color,
            bd=0
        ).pack(anchor='w', pady=3)
        
        self.lowercase_var = tk.BooleanVar(value=True)
        tk.Checkbutton(
            char_frame,
            text="Lowercase (a-z)",
            variable=self.lowercase_var,
            font=self.label_font,
            fg=self.text_color,
            bg=self.widget_bg,
            selectcolor=self.main_color,
            activebackground=self.widget_bg,
            activeforeground=self.text_color,
            bd=0
        ).pack(anchor='w', pady=3)
        
        self.digits_var = tk.BooleanVar(value=True)
        tk.Checkbutton(
            char_frame,
            text="Digits (0-9)",
            variable=self.digits_var,
            font=self.label_font,
            fg=self.text_color,
            bg=self.widget_bg,
            selectcolor=self.main_color,
            activebackground=self.widget_bg,
            activeforeground=self.text_color,
            bd=0
        ).pack(anchor='w', pady=3)
        
        self.symbols_var = tk.BooleanVar(value=True)
        tk.Checkbutton(
            char_frame,
            text="Symbols (!@#$%^&*)",
            variable=self.symbols_var,
            font=self.label_font,
            fg=self.text_color,
            bg=self.widget_bg,
            selectcolor=self.main_color,
            activebackground=self.widget_bg,
            activeforeground=self.text_color,
            bd=0
        ).pack(anchor='w', pady=3)
        
        # Generate Button
        generate_btn = tk.Button(
            main_frame,
            text="Generate Password",
            command=self.generate_password,
            font=self.button_font,
            bg=self.main_color,
            fg='white',
            activebackground='#D35400',
            bd=0,
            padx=20,
            pady=10,
            relief=tk.FLAT,
            cursor='hand2'
        )
        generate_btn.pack(fill=tk.X, pady=15)
        
        # Password Display
        password_frame = tk.Frame(main_frame, bg=self.widget_bg, bd=0)
        password_frame.pack(fill=tk.X, pady=10)
        
        self.password_var = tk.StringVar()
        tk.Entry(
            password_frame,
            textvariable=self.password_var,
            font=self.password_font,
            state='readonly',
            readonlybackground=self.widget_bg,
            fg=self.accent_color,
            justify=tk.CENTER,
            bd=0,
            relief=tk.FLAT
        ).pack(fill=tk.BOTH, padx=5, pady=5)
        
        # Action Buttons
        btn_frame = tk.Frame(main_frame, bg=self.bg_color)
        btn_frame.pack(fill=tk.X, pady=5)
        
        tk.Button(
            btn_frame,
            text="Copy",
            command=self.copy_to_clipboard,
            font=self.button_font,
            bg=self.accent_color,
            fg='white',
            activebackground='#2980B9',
            bd=0,
            padx=10,
            pady=8,
            relief=tk.FLAT
        ).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        
        tk.Button(
            btn_frame,
            text="Save",
            command=self.save_to_file,
            font=self.button_font,
            bg=self.widget_bg,
            fg=self.text_color,
            activebackground='#4A5C6A',
            bd=0,
            padx=10,
            pady=8,
            relief=tk.FLAT
        ).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        
        # Footer
        tk.Label(
            main_frame,
            text="✨ Best feeling is to being safe",
            font=self.label_font,
            fg=self.accent_color,
            bg=self.bg_color
        ).pack(pady=(20, 0))

    def generate_password(self):
        if not any([self.uppercase_var.get(), self.lowercase_var.get(), 
                   self.digits_var.get(), self.symbols_var.get()]):
            messagebox.showerror("Oops!", "Please select at least one ingredient!")
            return
        
        char_sets = []
        if self.uppercase_var.get():
            char_sets.append(string.ascii_uppercase)
        if self.lowercase_var.get():
            char_sets.append(string.ascii_lowercase)
        if self.digits_var.get():
            char_sets.append(string.digits)
        if self.symbols_var.get():
            char_sets.append(string.punctuation)
        
        all_chars = ''.join(char_sets)
        length = self.length_var.get()
        
        password = []
        for char_set in char_sets:
            password.append(random.choice(char_set))
        
        for _ in range(length - len(password)):
            password.append(random.choice(all_chars))
        
        random.shuffle(password)
        password = ''.join(password)
        
        self.password_var.set(password)
        self.password_entry.config(fg=self.accent_color)
    
    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied!", "Password copied to clipboard!")
        else:
            messagebox.showerror("Oh dear!", "No password generated yet!")
    
    def save_to_file(self):
        password = self.password_var.get()
        if not password:
            messagebox.showerror("Oh dear!", "No password generated yet!")
            return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            title="Save Your Password",
            initialfile="cozypass.txt"
        )
        
        if file_path:
            try:
                with open(file_path, 'w') as f:
                    f.write("╔══════════════════════════════╗\n")
                    f.write("║        Passwords File        ║\n")
                    f.write("╠══════════════════════════════╣\n")
                    f.write(f"║ Password: {password:<19}║\n")
                    f.write(f"║ Length: {len(password):<21}║\n")
                    f.write("║ Generated: Just now         ║\n")
                    f.write("╚══════════════════════════════╝\n")
                messagebox.showinfo("Saved!", "Password stored")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CozyDarkPasswordGenerator(root)
    root.mainloop()