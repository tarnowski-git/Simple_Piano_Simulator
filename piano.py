from tkinter import Tk, Frame, Entry, Button, StringVar, CENTER, DISABLED, FLAT
from functools import partial
import pygame


class Main_Application(Frame):
    """Main class of application."""

    BLACK = [
        "C#", "D#", "Space", "F#", "G#", "Bb", "Space", "C#1", "D#1",
    ]

    WHITE = [
        'C', 'D', 'E', 'F', 'G', 'A', 'B', "C1", "D1", "E1", "F1"
    ]

    FONT = ("Arial", 18, "bold")

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        # inital pygame for using sounds
        pygame.init()
        self.black_buttons = list(range(len(self.BLACK)))
        self.white_buttons = list(range(len(self.WHITE)))
        # variable to show pressed button in text_box
        self.var_text = StringVar()
        self.configure_gui()
        self.create_widgets()
        self.setup_layout()

    def configure_gui(self):
        """Setting general configurations of the application"""
        self.master.title("Virtual Piano")
        self.master.resizable(0, 0)
        self.master.configure(background="white")

    def create_widgets(self):
        """Creating the widgets of the application
        """
        self.text_box = Entry(self.master, textvariable=self.var_text, font=self.FONT,
                              bd=4, bg="powder blue", fg="white", justify=CENTER)
        # set frames which we relate with buttons
        self.black_keys = Frame(self.master)
        self.white_keys = Frame(self.master)

        index = 0
        for key in self.BLACK:
            # if every key which is Space
            if key == "Space":
                # create a empty button
                self.black_buttons[index] = Button(
                    self.black_keys, height=6, width=2, bd=4, bg="white", state=DISABLED, relief=FLAT)
            else:
                # partial takes care of function and argument instead of 'lambda'
                cmd = partial(self.button_command, key)

                # otherwise create a normal button
                self.black_buttons[index] = Button(
                    self.black_keys, command=cmd, height=6, width=6, bd=4, text=key, font=self.FONT, bg="black", fg="white")
            # go to the next button
            index += 1

        index = 0
        for key in self.WHITE:
            # partial takes care of function and argument instead of 'lambda'
            cmd = partial(self.button_command, key)

            self.white_buttons[index] = Button(
                self.white_keys, command=cmd, width=6, height=8, bd=4, text=key, font=self.FONT, bg="white", fg="black")
            # go to the next button
            index += 1

    def setup_layout(self):
        """Setup grid system
        """
        self.text_box.grid(row=0, column=0, columnspan=11, padx=10, pady=10)
        # frames grid are related with the window
        self.black_keys.grid(row=1)
        self.white_keys.grid(row=2)

        # set local grids in frames widgets
        var_col = 0
        for button in self.black_buttons:
            # if is a Space, make 1 col space between buttons
            if button["state"] == DISABLED:
                button.grid(row=0, column=2 * var_col + 1, padx=0, pady=0)
            else:
                button.grid(row=0, column=2 * var_col, padx=5, pady=5)
            # go to the next column
            var_col += 1

        var_col = 0
        for button in self.white_buttons:
            button.grid(row=0, column=var_col, padx=5, pady=5)
            # go to the next column
            var_col += 1

    def button_command(self, button):
        """Function for detecting pressed buttons."""
        if button == "C#":
            self.play_sound("C_s.wav")
        elif button == "D#":
            self.play_sound("D_s.wav")
        elif button == "F#":
            self.play_sound("F_s.wav")
        elif button == "G#":
            self.play_sound("G_s.wav")
        elif button == "C#1":
            self.play_sound("C_s1.wav")
        elif button == "D#1":
            self.play_sound("D_s1.wav")
        else:
            self.play_sound("{}.wav".format(button))
        # display info to the Text Box
        self.var_text.set(button)

    def play_sound(self, filename):
        """Function working only for Windows"""
        pygame.mixer.Sound("assets\\music_notes\\{}".format(
            filename)).play()


# Start program
if __name__ == '__main__':
    root = Tk()
    application = Main_Application(root)
    application.mainloop()
