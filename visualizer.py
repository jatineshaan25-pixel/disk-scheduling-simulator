import matplotlib.pyplot as plt


def calculate_metrics(result, num_requests):
    total = result["total_seek"]
    average = total / num_requests
    if total > 0:
        throughput = num_requests / total
    else:
        throughput = 0
    return {
        "total": total,
        "average": round(average, 2),
        "throughput": round(throughput, 4),
    }


def plot_path(path, title, disk_size):
    steps = list(range(len(path)))
    plt.figure(figsize=(9, 5))
    plt.plot(path, steps, marker="o")
    plt.gca().invert_yaxis()
    plt.xlim(0, disk_size - 1)
    plt.xlabel("Track number")
    plt.ylabel("Step")
    plt.title(title)
    plt.grid(True)
    for x, y in zip(path, steps):
        plt.annotate(str(x), (x, y), textcoords="offset points", xytext=(0, 8))
    plt.show()


def plot_comparison(results):
    names = list(results.keys())
    totals = [results[name]["total_seek"] for name in names]
    plt.figure(figsize=(7, 5))
    plt.bar(names, totals)
    plt.xlabel("Algorithm")
    plt.ylabel("Total seek time")
    plt.title("Algorithm Comparison")
    for i, value in enumerate(totals):
        plt.text(i, value, str(value), ha="center", va="bottom")
    plt.show()