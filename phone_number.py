import tkinter as tk
from tkinter import messagebox
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

# Function to retrieve phone number information
def get_phone_info():
    try:
        mobile_no = entry.get()
        mobile_no_parsed = phonenumbers.parse(mobile_no)

        time_zones = timezone._country_level_time_zones_for_number(mobile_no_parsed)
        carrier_info = carrier.name_for_number(mobile_no_parsed, "en")
        location_info = geocoder.description_for_number(mobile_no_parsed, "en")
        is_valid = phonenumbers.is_valid_number(mobile_no_parsed)
        is_possible = phonenumbers.is_possible_number(mobile_no_parsed)

        # Clear previous result
        result_text.delete('1.0', tk.END)

        # Display the information
        result_text.insert(tk.END, f"Time Zones: {time_zones}\n")
        result_text.insert(tk.END, f"Carrier: {carrier_info}\n")
        result_text.insert(tk.END, f"Location: {location_info}\n")
        result_text.insert(tk.END, f"Valid Mobile Number: {is_valid}\n")
        result_text.insert(tk.END, f"Possibility of Number: {is_possible}\n")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("ScorpionTaj - Phone Number Information")
root.geometry("500x300")

# Set the font to JetBrains Mono
font_style = ("JetBrains Mono", 12)

# Create widgets
label = tk.Label(root, text="Enter Mobile Number With Country Code:", font=font_style)
label.pack(pady=5)

entry = tk.Entry(root, width=40, font=font_style)
entry.pack(pady=5)

button = tk.Button(root, text="Get Info", command=get_phone_info, font=font_style)
button.pack(pady=5)

result_text = tk.Text(root, wrap=tk.WORD, height=10, width=60, font=font_style)
result_text.pack(pady=10)

root.mainloop()
