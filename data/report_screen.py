import tkinter as tk


def show_flare_report(report):
    window = tk.Tk()
    window.title("Solar Flare Report")
    window.geometry("800x600")

    text = tk.Text(window, wrap="word")
    text.pack(fill="both", expand=True)

    text.insert("1.0", report)

    window.mainloop()



