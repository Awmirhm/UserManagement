from ttkbootstrap import Window


class Page(Window):
    def __init__(self, weight=1000, height=700):
        super().__init__(themename="cyborg")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.geometry(f"{weight}x{height}")
        self.minsize(width=800,height=500)
        self.title("User Management")

    def show(self):
        self.mainloop()
