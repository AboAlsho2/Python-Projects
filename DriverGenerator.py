import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime
import os

def generate_files():
    author = author_entry.get()
    layer = layer_entry.get()
    driver_name = driver_name_entry.get().upper()  # Convert driver name to uppercase
    files = [file_listbox.get(idx) for idx in file_listbox.curselection()]
    folder_path = folder_path_entry.get()

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    for file_name in files:
        full_file_name = f"{driver_name}_{file_name}"
        file_path = os.path.join(folder_path, full_file_name)
        with open(file_path, 'w') as f:
            # Write header comment block
            f.write("/******************************************************/\n")
            f.write(f"/* Author :       {author}                              */\n")
            f.write(f"/* Version:         V1                                */\n")
            f.write(f"/* Layer  :        {layer}                               */\n")
            f.write(f"/* Date   :       {datetime.today().strftime('%Y-%m-%d')}                         */\n")
            f.write("/******************************************************/\n\n")
            
            # Add file guard if the file is a header file
            if full_file_name.endswith('.h'):
                file_guard = f"_{driver_name}_{file_name.split('.')[0].upper()}_H_"
                f.write(f"#ifndef {file_guard}\n")
                f.write(f"#define {file_guard}\n\n")
                
                # Close the file guard at the end of the file
                f.write(f"#endif /* {file_guard} */\n")

    messagebox.showinfo("Done", "Files have been generated successfully!")
    root.quit()  # Close the GUI after generation

def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(0, folder_path)

# Create the main window
root = tk.Tk()
root.title("Embedded System File Generator")

# Create widgets
tk.Label(root, text="Driver Name:").grid(row=0, column=0)
driver_name_entry = tk.Entry(root)
driver_name_entry.grid(row=0, column=1)

tk.Label(root, text="Author:").grid(row=1, column=0)
author_entry = tk.Entry(root)
author_entry.grid(row=1, column=1)

tk.Label(root, text="Layer:").grid(row=2, column=0)
layer_entry = tk.Entry(root)
layer_entry.grid(row=2, column=1)

tk.Label(root, text="Select Files:").grid(row=3, column=0)
file_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
file_listbox.grid(row=3, column=1)

# Add example file options including the new config.h
for file_name in ["interface.h", "private.h", "config.h", "main.c"]:
    file_listbox.insert(tk.END, file_name)

tk.Label(root, text="Folder Path:").grid(row=4, column=0)
folder_path_entry = tk.Entry(root)
folder_path_entry.grid(row=4, column=1)
tk.Button(root, text="Browse", command=browse_folder).grid(row=4, column=2)

tk.Button(root, text="Generate Files", command=generate_files).grid(row=5, column=1)

# Run the application
root.mainloop()

