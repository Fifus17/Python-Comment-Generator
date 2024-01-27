import tkinter as tk

from Model import Model

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.model = Model()

    def create_widgets(self):
        self.text_areas = tk.Frame(self)
        self.text_areas.pack(pady=10, padx=10, side="top")

        self.text_area_input = tk.Text(self.text_areas, undo=True, font=("Consolas", 14), height=50)
        self.text_area_input.pack(side="left")

        self.text_area_output = tk.Text(self.text_areas, state="disabled", font=("Consolas", 14), height=50)
        self.text_area_output.pack(side="right")

        self.buttons = tk.Frame(self)
        self.buttons.pack(pady=10, side="bottom")

        self.generate = tk.Button(self.buttons, text="  Generate  ", command=self.generate)
        self.generate.pack(side="left", expand=True)

        self.copy = tk.Button(self.buttons, text="  Copy  ", command=self.copy,)
        self.copy.pack(side="right", expand=True)

    def generate(self):
        overall_comment = self.model.process(self.text_area_input.get("1.0", "end-1c"))
        commented_code = f"# {overall_comment}\n{self.text_area_input.get('1.0', 'end-1c')}"
        self.text_area_output.configure(state="normal")
        self.text_area_output.delete("1.0", tk.END)
        self.text_area_output.insert("1.0", commented_code)
        self.text_area_output.configure(state="disabled")
        

    def copy(self):
        self.clipboard_clear()
        self.clipboard_append(self.text_area_output.get("1.0", "end-1c"))


def main():
    root = tk.Tk()
    root.title("Python Code Comment Generator")
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()