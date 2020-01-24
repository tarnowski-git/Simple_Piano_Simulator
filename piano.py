from tkinter import Tk, Frame, Label, Entry, Button, StringVar, CENTER, DISABLED, FLAT


class Main_Application(Frame):
    """Main class of application."""

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Virtual Piano")
        # +0+0 starts window from the upper left corner
        # self.master.geometry("552x70+0+0")
        self.master.configure(background="white")

        var_text = StringVar()

        # self.title_label = Label(self.master, text="Piano Musical Keys", font=(
        #     "Arial", 25, "bold"), padx=8, pady=8, bd=4, bg="powder blue", fg="white", justify=CENTER)
        # self.title_label.grid(row=0, column=0, columnspan=11)

        self.black_keys = Frame(self.master)
        self.black_keys.grid(row=1)

        self.text_box = Entry(self.master, textvariable=var_text, font=(
            "Arial", 18, "bold"), bd=4, bg="powder blue", fg="white", justify=CENTER)
        self.text_box.grid(row=0, column=0, columnspan=11)

        self.btn_Cs = Button(self.black_keys, height=6, width=6, bd=4, text="C#", font=(
            "Arial", 18, "bold"), bg="black", fg="white")
        self.btn_Cs.grid(row=0, column=0, padx=5, pady=5)

        self.btn_Ds = Button(self.black_keys, height=6, width=6, bd=4, text="D#", font=(
            "Arial", 18, "bold"), bg="black", fg="white")
        self.btn_Ds.grid(row=0, column=2, padx=5, pady=5)

        self.btn_Space_1 = Button(self.black_keys, state=DISABLED, width=2, height=6, bd=4, font=(
            "Arial", 18, "bold"), bg="powder blue", relief=FLAT)
        self.btn_Space_1.grid(row=0, column=3, padx=0, pady=0)

        self.btn_Fs = Button(self.black_keys, height=6, width=6, bd=4, text="F#", font=(
            "Arial", 18, "bold"), bg="black", fg="white")
        self.btn_Fs.grid(row=0, column=4, padx=5, pady=5)

        self.btn_Gs = Button(self.black_keys, height=6, width=6, bd=4, text="G#", font=(
            "Arial", 18, "bold"), bg="black", fg="white")
        self.btn_Gs.grid(row=0, column=6, padx=5, pady=5)

        self.btn_Bb = Button(self.black_keys, height=6, width=6, bd=4, text="Bb", font=(
            "Arial", 18, "bold"), bg="black", fg="white")
        self.btn_Bb.grid(row=0, column=8, padx=5, pady=5)

        self.btn_Space_2 = Button(self.black_keys, state=DISABLED, width=2, height=6, bd=4, font=(
            "Arial", 18, "bold"), bg="powder blue", relief=FLAT)
        self.btn_Space_2.grid(row=0, column=9, padx=5, pady=5)

        self.btn_Cs1 = Button(self.black_keys, height=6, width=6, bd=4, text="C#1", font=(
            "Arial", 18, "bold"), bg="black", fg="white")
        self.btn_Cs1.grid(row=0, column=10, padx=5, pady=5)

        self.btn_Ds1 = Button(self.black_keys, height=6, width=6, bd=4, text="D#1", font=(
            "Arial", 18, "bold"), bg="black", fg="white")
        self.btn_Ds1.grid(row=0, column=12, padx=5, pady=5)

        # ===============

        self.white_keys = Frame(self.master)
        self.white_keys.grid(row=2)

        self.btn_C = Button(self.white_keys, width=6, height=8, bd=4, text="C", font=(
            "Arial", 18, "bold"), bg="white", fg="black")
        self.btn_C.grid(row=0, column=0, padx=5, pady=5)

        self.btn_D = Button(self.white_keys, width=6, height=8, bd=4, text="D", font=(
            "Arial", 18, "bold"), bg="white", fg="black")
        self.btn_D.grid(row=0, column=1, padx=5, pady=5)

        self.btn_E = Button(self.white_keys, width=6, height=8, bd=4, text="E", font=(
            "Arial", 18, "bold"), bg="white", fg="black")
        self.btn_E.grid(row=0, column=2, padx=5, pady=5)

        self.btn_F = Button(self.white_keys, width=6, height=8, bd=4, text="F", font=(
            "Arial", 18, "bold"), bg="white", fg="black")
        self.btn_F.grid(row=0, column=3, padx=5, pady=5)

        self.btn_G = Button(self.white_keys, width=6, height=8, bd=4, text="G", font=(
            "Arial", 18, "bold"), bg="white", fg="black")
        self.btn_G.grid(row=0, column=4, padx=5, pady=5)

        self.btn_A = Button(self.white_keys, width=6, height=8, bd=4, text="A", font=(
            "Arial", 18, "bold"), bg="white", fg="black")
        self.btn_A.grid(row=0, column=5, padx=5, pady=5)

        self.btn_B = Button(self.white_keys, width=6, height=8, bd=4, text="B", font=(
            "Arial", 18, "bold"), bg="white", fg="black")
        self.btn_B.grid(row=0, column=6, padx=5, pady=5)

        self.btn_C1 = Button(self.white_keys, width=6, height=8, bd=4, text="C1", font=(
            "Arial", 18, "bold"), bg="white", fg="black")
        self.btn_C1.grid(row=0, column=7, padx=5, pady=5)

        self.btn_D1 = Button(self.white_keys, width=6, height=8, bd=4, text="D1", font=(
            "Arial", 18, "bold"), bg="white", fg="black")
        self.btn_D1.grid(row=0, column=8, padx=5, pady=5)

        self.btn_E1 = Button(self.white_keys, width=6, height=8, bd=4, text="E1", font=(
            "Arial", 18, "bold"), bg="white", fg="black")
        self.btn_E1.grid(row=0, column=9, padx=5, pady=5)

        self.btn_F1 = Button(self.white_keys, width=6, height=8, bd=4, text="F1", font=(
            "Arial", 18, "bold"), bg="white", fg="black")
        self.btn_F1.grid(row=0, column=10, padx=5, pady=5)


# Start program
if __name__ == '__main__':
    root = Tk()
    application = Main_Application(root)
    application.mainloop()
