import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO


def show_pic_day(pic_day):
    window = tk.Tk()
    window.title("Picture of the Day")
    window.geometry("800x600")

    if pic_day and pic_day.get("media_type") == "image":
        image_url = pic_day["hdurl"]

        response = requests.get(image_url)
        response.raise_for_status()

        image = Image.open(BytesIO(response.content))
        image = image.resize((800, 600), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(window, image=photo)
        label.image = photo
        label.pack()
    else:
        label = tk.Label(
            window,
            text = "No image available for today's APOD."
        )
        label.pack()

    window.mainloop()