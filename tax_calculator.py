import customtkinter as ctk

class TaxCalculator:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title('Tax Calculator')
        self.window.geometry('280x200')
        self.window.resizable(False, False)
            
        padding = {'padx': 20, 'pady': 10}
            
        income_label = ctk.CTkLabel(self.window, text='Income:')
        income_label.grid(row=0, column=0, **padding)
            
        global income_entry
        income_entry = ctk.CTkEntry(self.window)
        income_entry.grid(row=0, column=1, **padding)
            
        percent_label = ctk.CTkLabel(self.window, text='Percent:')
        percent_label.grid(row=1, column=0, **padding)
            
        global percent_entry
        percent_entry = ctk.CTkEntry(self.window)
        percent_entry.grid(row=1, column=1, **padding)
            
        result_label = ctk.CTkLabel(self.window, text='Tax:')
        result_label.grid(row=2, column=0, **padding)
            
        self.result_entry = ctk.CTkEntry(self.window)
        self.result_entry.insert(0, '0')
        self.result_entry.grid(row=2, column=1, **padding)
            
        calculate_button = ctk.CTkButton(self.window, text='Calculate', command=self.calculate_tax)
        calculate_button.grid(row=3, column=1, **padding)
            
    def update_result(self, text):
        self.result_entry.delete(0, ctk.END)
        self.result_entry.insert(0, text)

    def calculate_tax(self):
        try:
            income = float(income_entry.get())
            percent = float(percent_entry.get())
            self.update_result(f'${income * (percent/100):,.2f}')
        except ValueError:
            self.update_result('Invalid input')
            
    def run(self):
        self.window.mainloop()
        
if __name__ == '__main__':
    obj = TaxCalculator()
    obj.run()