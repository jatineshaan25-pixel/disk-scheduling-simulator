import tkinter as tk
from tkinter import ttk, messagebox
from algorithms import fcfs, sstf, scan, c_scan


def run_algorithm():
    try:
        requests = [int(x) for x in entry_requests.get().split(",")]
        head = int(entry_head.get())
        disk_size = int(entry_disk.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")
        return

    choice = combo_algo.get()
    if choice == "FCFS":
        result = fcfs(requests, head)
    elif choice == "SSTF":
        result = sstf(requests, head)
    elif choice == "SCAN":
        result = scan(requests, head, disk_size, "up")
    else:
        result = c_scan(requests, head, disk_size)

    avg = result["total_seek"] / len(requests)
    label_result.config(
        text="Total seek: " + str(result["total_seek"]) + "   Average: " + str(round(avg, 2))
    )


root = tk.Tk()
root.title("Advanced Disk Scheduling Simulator")

tk.Label(root, text="Requests (comma separated):").grid(row=0, column=0)
entry_requests = tk.Entry(root, width=40)
entry_requests.grid(row=0, column=1)

tk.Label(root, text="Head start:").grid(row=1, column=0)
entry_head = tk.Entry(root)
entry_head.grid(row=1, column=1)

tk.Label(root, text="Disk size:").grid(row=2, column=0)
entry_disk = tk.Entry(root)
entry_disk.grid(row=2, column=1)

tk.Label(root, text="Algorithm:").grid(row=3, column=0)
combo_algo = ttk.Combobox(root, values=["FCFS", "SSTF", "SCAN", "C-SCAN"])
combo_algo.current(0)
combo_algo.grid(row=3, column=1)

tk.Button(root, text="Run", command=run_algorithm).grid(row=4, column=0, columnspan=2)

label_result = tk.Label(root, text="")
label_result.grid(row=5, column=0, columnspan=2)

root.mainloop()