import tkinter

# Create Main Window
screen = tkinter.Tk()
screen.title("Advanced Time Converter")
screen.minsize(600, 400)
screen.config(padx=50, pady=50, bg="#1e3d59")

# Header Label
header_label = tkinter.Label(screen, text="Time Converter", font=("Arial", 28, "bold"), bg="#1e3d59", fg="#f5f5f5")
header_label.grid(row=0, column=0, columnspan=3, pady=(0, 30))

# Input Section
tkinter.Label(screen, text="Enter Seconds:", font=("Arial", 18), bg="#1e3d59", fg="#f5f5f5").grid(row=1, column=0, pady=10)
seconds_entry = tkinter.Entry(screen, width=15, font=("Arial", 18))
seconds_entry.grid(row=1, column=1, pady=10, padx=20)

# Output Label
time_label = tkinter.Label(screen, text="00 Hours : 00 Minutes : 00 Seconds : 000 ms", font=("Arial", 20), bg="#1e3d59", fg="#f5f5f5")
time_label.grid(row=3, column=0, columnspan=3, pady=30)

# Convert Function
def convert_time():
    try:
        total_seconds = float(seconds_entry.get())

        if total_seconds < 0:
            time_label.config(text="Invalid Input: Must be positive!")
            return

        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        milliseconds = int((total_seconds - int(total_seconds)) * 1000)

        time_label.config(text=f"{hours:02} Hours : {minutes:02} Minutes : {seconds:02} Seconds : {milliseconds:03} ms")

    except ValueError:
        time_label.config(text="Invalid Input: Enter a valid number!")

# Clear Function
def clear_all():
    seconds_entry.delete(0, tkinter.END)
    time_label.config(text="00 Hours : 00 Minutes : 00 Seconds : 000 ms")

# Buttons
convert_button = tkinter.Button(screen, text="Convert", command=convert_time, font=("Arial", 18), bg="#ff6f61", fg="white")
convert_button.grid(row=2, column=0, pady=20)

clear_button = tkinter.Button(screen, text="Clear", command=clear_all, font=("Arial", 18), bg="#00bcd4", fg="white")
clear_button.grid(row=2, column=1, pady=20)

# Footer Label
footer_label = tkinter.Label(screen, text="Built with ❤️ using Python & Tkinter", font=("Arial", 12), bg="#1e3d59", fg="#c1c1c1")
footer_label.grid(row=4, column=0, columnspan=3, pady=10)

# Run the main loop
screen.mainloop()
