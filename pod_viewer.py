# Import the required libraries
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import ImageTk, Image
import requests
from io import BytesIO
from pip._vendor.urllib3 import response

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

# Define a function to get the request from NASA APOD API


def get_request():
    global response
    # Set the parameter for request
    url = 'https://api.nasa.gov/planetary/apod'
    # api_key = os.environ['API_KEY']
    api_key = 'DEMO_KEY'
    date = calander.get_date()

    querystring = {'api_key': api_key, 'date': date}
    # Call the request
    response = requests.request("GET", url, params=querystring)
    response = response.json()
    # Update labels based on the response we get
    set_info()


# Set the Info
def set_info():
    # Update the Label based on JSON returned objects
    pic_date.config(text=response['date'])
    pic_explanation.config(text=response['explanation'])
    global img
    global thumbnail
    global full_img

    url = response['url']
    img_response = requests.get(url, stream=True)

    # Get the content of the response and use BytesIo to open it as image in the label
    img_data = img_response.content
    img = Image.open(BytesIO(img_data))
    full_img = ImageTk.PhotoImage(img)

    # Create a thumbnail
    thumb_data = img_response.content
    thumb = Image.open(BytesIO(thumb_data))
    thumb.thumbnail((200, 200))
    thumb = ImageTk.PhotoImage(thumb)

    # Set the image in the Label
    pic_label.config(image=thumb)


def exit_app():
    win.destroy()


# Define a frame
frame_input = Frame(win, bg=nasa_blue)
frame_output = Frame(win, bg="#ffffff")
frame_input.pack()
frame_output.pack(padx=50, pady=(0, 25))

calander = DateEntry(frame_input, width=10, font=font,
                     background=nasa_blue, foreground="#FFFFFF")

submit = Button(frame_input, text="Submit", font=font,
                bg=nasa_light_blue, command=get_request)
full_btn = Button(frame_input, text="View Photo",
                  font=font, bg=nasa_light_blue)
save_btn = Button(frame_input, text="Save Photo",
                  font=font, bg=nasa_light_blue)
quit_btn = Button(frame_input, text="Quit", font=font,
                  bg="red", command=exit_app)
calander.grid(row=0, column=0, padx=5, pady=10)
submit.grid(row=0, column=1, padx=5, pady=10, ipadx=10)
full_btn.grid(row=0, column=2, padx=5, pady=10, ipadx=10)
save_btn.grid(row=0, column=3, padx=5, pady=10, ipadx=10)
quit_btn.grid(row=0, column=4, padx=5, pady=10, ipadx=10)

# Layout for the output widget
pic_date = Label(frame_output, text="texting", font=font, bg="white")
pic_explanation = Label(frame_output, text="texting",
                        font=font, bg="white", wraplength=300)
pic_label = Label(frame_output, image="")

pic_date.grid(row=0, column=1, padx=10)
pic_explanation.grid(row=0, column=0, rowspan=1, padx=10, pady=10)
pic_label.grid(row=0, column=1, padx=10, pady=10)
win.mainloop()
