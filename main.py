import tkinter as tk
import os
import shutil


def get_size(path):
    total_size = 0
    if os.path.isfile(path):
        total_size = os.path.getsize(path)
    elif os.path.isdir(path):
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if os.path.exists(fp):
                    total_size += os.path.getsize(fp)
    return total_size

def get_folder_size(folder):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.exists(fp):
                total_size += os.path.getsize(fp)
    return total_size

def on_clean_button_click():
    button.pack_forget()
    

    temp_dir = os.getenv("TEMP")
    total_freed = 0

    
    for entry in os.listdir(temp_dir):
        path = os.path.join(temp_dir, entry)
        try:
            if os.path.isfile(path) or os.path.islink(path):
                size = os.path.getsize(path)
                os.remove(path)
                total_freed += size
                print(f"Deleted file: {path}")
            elif os.path.isdir(path):
                # Calculate folder size before deleting
                size = get_folder_size(path)
                shutil.rmtree(path)
                total_freed += size
                print(f"Deleted folder: {path}")
        except Exception as e:
            print(f"Error deleting {path}: {e}")
    
    freed_mb = total_freed / (1024 * 1024)
    tk.Label(root, text=(f"\nTotal storage freed: {freed_mb:.2f} MB"), fg="black", bg="white", font=("Segoe Print", 32)).pack()


root = tk.Tk()

root.title("Drive Duster")
root.configure(background="white")
root.minsize(750, 500)
root.maxsize(1500, 1000)
root.geometry("300x300+50+50")

tk.Label(root, text="Drive Duster", fg="blue", bg="white", font=("Segoe Print", 64)).pack()
button = tk.Button(root, text="Clean PC", font=("Segoe Print", 32), command=on_clean_button_click)
button.pack(pady=100)

root.mainloop()

