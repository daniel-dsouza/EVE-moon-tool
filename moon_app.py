import tkinter as tk
from tkinter import scrolledtext, filedialog

import moons

VERSION = 0.1


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.master.title(f'Moon Data App v{VERSION}')
        self.raw_input = scrolledtext.ScrolledText(self)
        self.f_commands = tk.Frame(self, padx='2')
        self.b_import_raw = tk.Button(self.f_commands, text='Import Raw', width='10', command=self.read_raw)
        self.b_export_csv = tk.Button(self.f_commands, text='Export CSV', width='10', command=self.write_csv)
        self.b_reset_data = tk.Button(self.f_commands, text='Reset Data', width='10', command=self.reset_data)

        self.create_widgets()
        self.moondata = moons.MoonData()

    def create_widgets(self):
        self.raw_input.insert(tk.END, 'Paste moon analysis here')
        self.raw_input.pack(side='left')

        self.f_commands.pack(side='left', fill='y')
        self.b_import_raw.pack(side='top')
        self.b_export_csv.pack(side='top')
        self.b_reset_data.pack(side='top')

    def read_raw(self):
        raw = self.raw_input.get('1.0', tk.END)
        self.moondata.import_raw(raw)

        self.raw_input.delete('1.0', tk.END)
        self.raw_input.insert('1.0', 'Paste moon analysis here')

    def write_csv(self):
        print('writing csv')
        filename = filedialog.asksaveasfilename(initialfile='output.csv', filetypes=[('CSV', '.csv')], defaultextension='.csv')
        if filename is None:
            return
        self.moondata.export_csv(filename)

    def reset_data(self):
        self.moondata.empty()


root = tk.Tk()
app = Application(master=root)
app.mainloop()