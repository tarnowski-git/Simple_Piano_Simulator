from tkinter import Tk, Frame


class Main_Application(Frame):
    """Main class of application."""

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Virtual Piano")
        # +0+0 starts window from the upper left corner
        self.master.geometry("352x70+0+0")
        self.master.configure(background="white")



# Start program
if __name__ == '__main__':
    root = Tk()
    application = Main_Application(root)
    application.mainloop()
