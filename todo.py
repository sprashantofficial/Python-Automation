import tkinter as tk
from ast import Index
from tkinter import messagebox
from tkinter import ttk

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title('ToDo App')
        self.root.geometry('450x500')

        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Helvetica', 18, 'bold'), background="#ffffff", foreground="#333333")
        self.style.configure('TButton', font=('Helvetica', 12), padding=5, background="#4CAF50", foreground="black")

        self.label = ttk.Label(root, text='ToDo App', style='TLabel')
        self.label.pack(pady=20)

        self.task_entry_frame = ttk.Frame(root)
        self.task_entry_frame.pack(pady=10)
        self.task_entry = ttk.Entry(self.task_entry_frame, width=35, font=('Helvetica', 12))
        self.task_entry.pack(side=tk.LEFT, padx=10)
        self.add_button = ttk.Button(self.task_entry_frame, text='Add Task', command=self.add_task, style='TButton')
        self.add_button.pack(side=tk.LEFT)

        self.listbox_frame = ttk.Frame(root)
        self.listbox_frame.pack(pady=10)
        self.scrollbar = ttk.Scrollbar(self.listbox_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox = tk.Listbox(self.listbox_frame, height=10, width=40, font=('Helvetica', 12),
                                       yscrollcommand=self.scrollbar.set, activestyle='dotbox', bg='#f9f9f9',
                                       highlightthickness=1, highlightbackground="#cccccc",
                                       selectbackground='#6db3f2', selectforeground='white')
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.action_frame = ttk.Frame(root)
        self.action_frame.pack(pady=10)

        self.complete_button = ttk.Button(self.action_frame, text='Mark as Completed', command=self.mark_completed, style='TButton')
        self.complete_button.pack(side=tk.LEFT, padx=10)

        self.remove_button = ttk.Button(self.action_frame, text='Remove Task', command=self.remove_task, style='TButton')
        self.remove_button.pack(side=tk.LEFT)

        self.tasks = []

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning('Input Error', 'Please enter a task.')

    def mark_completed(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            completed_task = self.tasks[selected_task_index]
            self.tasks[selected_task_index] = f'✔ {completed_task} (Completed)'
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning('Selection Error', 'Please select a task to mark as completed.')

    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning('Selection Error', 'Please select a task to remove.')

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == '__main__':
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()