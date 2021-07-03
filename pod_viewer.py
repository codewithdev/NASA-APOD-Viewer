# Import the required libraries
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

# Create an instance of window object
win = Tk()
win.geometry("700x350")
win.title("NASA POD Viewer")
win.iconbitmap("planet.ico")

# Set the font for all the widgets
font = ('Calibri 11')
nasa_blue = "#043c93"
nasa_light_blue = "#7aa5d3"
win.config(background=nasa_blue)

# Define a frame
frame_input = Frame(win, bg=nasa_blue)
frame_output = Frame(win, bg="#ffffff")
frame_input.pack()
frame_output.pack(padx=50, pady=(0, 25))

calendar = DateEntry(frame_input, width=10, font=font,
                     background=nasa_blue, foreground="#FFFFFF")

submit = Button(frame_input, text="Submit", font=font, bg=nasa_light_blue)
full_btn = Button(frame_input, text="View Photo",
                  font=font, bg=nasa_light_blue)
save_btn = Button(frame_input, text="Save Photo",
                  font=font, bg=nasa_light_blue)
quit_btn = Button(frame_input, text="Quit", font=font, bg="red", command= win.destroy())
calendar.grid(row=0, column=0, padx=5, pady=10, ipadx=10)
submit.grid(row=0, column=1, padx=5, pady=10, ipadx=10)
full_btn.grid(row=0, column=2, padx=5, pady=10, ipadx=10)
save_btn.grid(row=0, column=3, padx=5, pady=10, ipadx=10)
quit_btn.grid(row=0, column=4, padx=5, pady=10, ipadx=10)

# Layout for the output widget
pic_date = Label(frame_output, text="texting")
pic_explanation = Label(frame_output, text="texting")
pic_label = Label(frame_output, text="texting")

pic_date.grid()
pic_explanation.grid()
pic_label.grid()
win.mainloop()
