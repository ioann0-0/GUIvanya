import tkinter as tk 
from tkinter import messagebox, scrolledtext 
import requests 
import json 
import os 
 
class FetchDataApp: 
    def __init__(self, root): 
        self.root = root 
        self.root.title("Fetch Data by Vanekkk") 
        self.root.geometry("600x500")   
 
        self.main_frame = tk.Frame(self.root, padx=10, pady=10) 
        self.main_frame.pack(fill=tk.BOTH, expand=True) 
 
        self.create_widgets() 
 
    def create_widgets(self): 
        self.label_id = tk.Label(self.main_frame, text="Введите ID поста:", font=('Arial', 12)) 
        self.label_id.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W) 
 
        self.entry_id = tk.Entry(self.main_frame, font=('Arial', 12)) 
        self.entry_id.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW) 
 
        self.button_fetch = tk.Button(self.main_frame, text="Запрос", command=self.fetch_data, font=('Arial', 12), bg='#4CAF50', fg='white') 
        self.button_fetch.grid(row=0, column=2, padx=5, pady=5) 
 
        self.text_area = scrolledtext.ScrolledText(self.main_frame, wrap=tk.WORD, width=70, height=20, font=('Arial', 12)) 
        self.text_area.grid(row=1, column=0, columnspan=3, padx=5, pady=5) 
 
        self.button_save = tk.Button(self.main_frame, text="Сохранить", command=self.save_data, font=('Arial', 12), bg='#2196F3', fg='white') 
        self.button_save.grid(row=2, column=0, columnspan=3, pady=10) 
 
        self.main_frame.grid_columnconfigure(1, weight=1) 
 
    def fetch_data(self): 
        try: 
            user_id = self.entry_id.get().strip() 
 
            if not user_id: 
                messagebox.showwarning("Предупреждение", "Введите ID") 
                return 
 
            response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{user_id}') 
            response.raise_for_status()   
 
            data = response.json() 
 
            self.text_area.delete('1.0', tk.END)   
            self.text_area.insert(tk.END, json.dumps(data, indent=4)) 
 
        except requests.exceptions.RequestException as e: 
            messagebox.showerror("Ошибка", f"Не удалось получить данные: {e}") 
 
    def save_data(self): 
        data = self.text_area.get('1.0', tk.END).strip() 
 
        if not data: 
            messagebox.showwarning("Предупреждение", "Нет данных для сохранения") 
            return 
 
        try: 
            file_path = os.path.join('saved_data', 'data.json') 
            os.makedirs('saved_data', exist_ok=True)   
 
            with open(file_path, 'w') as file: 
                file.write(data) 
 
            messagebox.showinfo("Информация", "Данные успешно сохранены") 
        except IOError as e: 
            messagebox.showerror("Ошибка", f"Не удалось сохранить данные: {e}") 
 
root = tk.Tk() 
app = FetchDataApp(root) 
root.mainloop()
