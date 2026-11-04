import tkinter as tk
from tkinter import ttk, messagebox
from algorithms import fcfs, sstf, scan, c_scan
from visualizer import calculate_metrics, plot_path, plot_comparison


def read_inputs():
    try:
        requests = [int(x) for x in entry_requests.get().split(",")]
        head = int(entry_head.get())
        disk_size = int(entry_disk.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")
        return None
    if disk_size <= 0 or head < 0 or head >= disk_size:
        messagebox.showerror("Error", "Head must be inside the disk")
        return None
    for r in requests:
        if r < 0 or r >= disk_size:
            messagebox.showerror("Error", "Every request must be between 0 and " + str(disk_size - 1))
            return None
    return requests, head, disk_size


def get_result(choice, requests, head, disk_size):
    if choice == "FCFS":
        return fcfs(requests, head)
    elif choice == "SSTF":
        return sstf(requests, head)
    elif choice == "SCAN":
        return scan(requests, head, disk_size, "up")
    else:
        return c_scan(requests, head, disk_size)


def run_algorithm():
    data = read_inputs()
    if data is None:
        return
    requests, head, disk_size = data
    choice = combo_algo.get()
    result = get_result(choice, requests, head, disk_size)
    m = calculate_metrics(result, len(requests))
    label_result.config(
        text="Total seek: " + str(m["total"])
        + "   Average: " + str(m["average"])
        + "   Throughput: " + str(m["throughput"])
    )
    plot_path(result["path"], choice + " head movement", disk_size)


def compare_all():
    data = read_inputs()
    if data is None:
        return
    requests, head, disk_size = data
    results = {}
    for name in ["FCFS", "SSTF", "SCAN", "C-SCAN"]:
        results[name] = get_result(name, requests, head, disk_size)
    plot_comparison(results)


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

tk.Button(root, text="Run", command=run_algorithm).grid(row=4, column=0)
tk.Button(root, text="Compare All", command=compare_all).grid(row=4, column=1)

label_result = tk.Label(root, text="")
label_result.grid(row=5, column=0, columnspan=2)

root.mainloop()