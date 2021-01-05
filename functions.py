from gui import *

def new(self):
    if len(self.txt_input.get("1.0", tk.END)) > 1:
        choice = messagebox.askyesno(title="Warning", message="Close this file without saving ?")
        if not choice:
            pass
        else:
            self.txt_input.delete("1.0", tk.END)
            self.file_select = None
            self.master.title(f"Text Editor")

def open(self):
    self.file_select = filedialog.askopenfile(filetypes=[("Python Files", '*.py'), ("Text Files", "*.txt")])
    if self.file_select != None:
        self.file_select_name = os.path.basename(self.file_select.name)
        content = self.file_select.read()
        self.master.title(f"{self.file_select_name} - Text Editor")
        self.txt_input.delete("1.0", tk.END)
        self.txt_input.insert(tk.END, content)

def open_alert(self):
    try:
        if len(self.txt_input.get("1.0", tk.END)) > 1:
            if self.file_select.read() != self.txt_input.get("1.0", tk.END):
                choice = messagebox.askyesno(title="Warning", message="Close this file without saving ?")
                if not choice:
                    pass
                else:
                    self.open()
            else:
                self.open()
        else:
            self.open()
    except AttributeError:
        self.open()

def close_alert(self):
    try:
        if len(self.txt_input.get("1.0", tk.END)) > 1:
            if self.file_select.read() != self.txt_input.get("1.0", tk.END):
                choice = messagebox.askyesno(title="Warning", message="Close this file without saving ?")
                if not choice:
                    pass
                else:
                    self.master.destroy()
            else:
                self.master.destroy()
        else:
            self.master.destroy()
            
    except AttributeError:
        if self.file_select == None and len(self.txt_input.get("1.0", tk.END)) > 1:
            choice = messagebox.askyesno(title="Warning", message="Close this draft without saving ?")
            if not choice:
                pass
            else:
                self.master.destroy()
        else:
            self.master.destroy()

def delete_window(self):
    try:
        if len(self.txt_input.get("1.0", tk.END)) > 1:
            if self.file_select.read() != self.txt_input.get("1.0", tk.END):
                choice = messagebox.askyesno(title="Warning", message="Close this file without saving ?")
                if not choice:
                    pass
                else:
                    self.master.destroy()
            else:
                self.master.destroy()
        else:
            self.master.destroy()

    except AttributeError:
        if self.file_select == None and len(self.txt_input.get("1.0", tk.END)) > 1:
            choice = messagebox.askyesno(title="Warning", message="Close this draft without saving ?")
            if not choice:
                pass
            else:
                self.master.destroy()
        else:
            self.master.destroy()
    
def save(self):
    save_content = self.txt_input.get("1.0", tk.END)
    if self.file_select != None:
        with open(self.file_select.name, "r+") as f:
            self.file_select = f
            f.write(save_content)
            f.close()
    else:
        self.save_as()

def save_as(self):
    self.file_select2 = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("All Files", "*"), ("Python Files", '*.py'), ("Text Files", "*.txt")])
    if self.file_select != None:
        self.file_selectname = os.path.basename(self.file_select2.name)
        save_content = self.txt_input.get("1.0", tk.END)
        self.file_select2.write(save_content)
        self.file_select = open(self.file_select.name, "r+")
        self.file_select2.close()
        self.master.title(f"{self.file_selectname} - Text Editor")
    else:
        pass
    
def word_count(self):
    txt = self.txt_input.get("1.0", tk.END)
    txt = " ".join(txt.split())
    txt_split = txt.split(" ")

    if len(txt_split) <= 1:
        txt_split_msg = str(len(txt_split)) + " word in this file."
    if len(txt_split) <= 1 and txt_split[0] == "":
        txt_split_msg = "No word in this file."
    else:
        txt_split_msg = str(len(txt_split)) + " words in this file."

    messagebox.showinfo("Word count",txt_split_msg)