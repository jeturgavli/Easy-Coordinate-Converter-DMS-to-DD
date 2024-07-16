import customtkinter as ctk
from PIL import Image
import pyperclip
import webbrowser

def dms_to_dd(degrees, minutes, seconds):
    dd = abs(degrees) + minutes / 60 + seconds / 3600
    return dd if degrees >= 0 else -dd

def convert_dms_to_dd():
    try:
        lat_degrees = int(lat_degrees_entry.get())
        lat_minutes = int(lat_minutes_entry.get())
        lat_seconds = float(lat_seconds_entry.get())
        
        lon_degrees = int(lon_degrees_entry.get())
        lon_minutes = int(lon_minutes_entry.get())
        lon_seconds = float(lon_seconds_entry.get())
        
        lat_decimal_degrees = dms_to_dd(lat_degrees, lat_minutes, lat_seconds)
        lon_decimal_degrees = dms_to_dd(lon_degrees, lon_minutes, lon_seconds)
        
        result_label.config(text=f"Latitude: {lat_decimal_degrees:.6f}, Longitude: {lon_decimal_degrees:.6f}")
    except ValueError:
        ctk.CTkMessageBox.show_error("Invalid input", "Please enter valid numbers for degrees, minutes, and seconds.")
    except Exception as e:
        ctk.CTkMessageBox.show_error("Error", str(e))

def copy_to_clipboard():
    result_text = result_label.cget("text")
    if result_text:
        lat_lon = result_text.split(", ")
        lat = lat_lon[0].split(": ")[1]
        lon = lat_lon[1].split(": ")[1]
        pyperclip.copy(f"Latitude: {lat}, Longitude: {lon}")
        ctk.CTkMessageBox.show_info("Copied", "Latitude and Longitude copied to clipboard.")

def open_profile(event):
    webbrowser.open("https://github.com/jeturgavli")

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("DMS to Decimal Degrees Converter - JETRock Version 1.0")

input_frame = ctk.CTkFrame(root)
input_frame.grid(row=0, column=0, padx=10, pady=10)

ctk.CTkLabel(input_frame, text="Latitude Degrees:").grid(row=0, column=0, padx=10, pady=5)
lat_degrees_entry = ctk.CTkEntry(input_frame)
lat_degrees_entry.grid(row=0, column=1, padx=10, pady=5)

ctk.CTkLabel(input_frame, text="Latitude Minutes:").grid(row=1, column=0, padx=10, pady=5)
lat_minutes_entry = ctk.CTkEntry(input_frame)
lat_minutes_entry.grid(row=1, column=1, padx=10, pady=5)

ctk.CTkLabel(input_frame, text="Latitude Seconds:").grid(row=2, column=0, padx=10, pady=5)
lat_seconds_entry = ctk.CTkEntry(input_frame)
lat_seconds_entry.grid(row=2, column=1, padx=10, pady=5)

ctk.CTkLabel(input_frame, text="Longitude Degrees:").grid(row=3, column=0, padx=10, pady=5)
lon_degrees_entry = ctk.CTkEntry(input_frame)
lon_degrees_entry.grid(row=3, column=1, padx=10, pady=5)

ctk.CTkLabel(input_frame, text="Longitude Minutes:").grid(row=4, column=0, padx=10, pady=5)
lon_minutes_entry = ctk.CTkEntry(input_frame)
lon_minutes_entry.grid(row=4, column=1, padx=10, pady=5)

ctk.CTkLabel(input_frame, text="Longitude Seconds:").grid(row=5, column=0, padx=10, pady=5)
lon_seconds_entry = ctk.CTkEntry(input_frame)
lon_seconds_entry.grid(row=5, column=1, padx=10, pady=5)

convert_button = ctk.CTkButton(input_frame, text="Convert", command=convert_dms_to_dd)
convert_button.grid(row=6, column=0, columnspan=2, pady=10)

result_label = ctk.CTkLabel(input_frame, text="Latitude: , Longitude: ")
result_label.grid(row=7, column=0, columnspan=2, pady=5)

copy_button = ctk.CTkButton(input_frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=8, column=0, columnspan=2, pady=10)

image = Image.open("img/01.jpg")
photo = ctk.CTkImage(image, size=(300, 300))

image_label = ctk.CTkLabel(root, image=photo, text="")
image_label.grid(row=0, column=1, padx=10, pady=10)
image_label.bind("<Button-1>", open_profile)

heading_label = ctk.CTkLabel(root, text="DMS to Decimal Degrees Converter", font=("Helvetica", 16, "bold"))
heading_label.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
