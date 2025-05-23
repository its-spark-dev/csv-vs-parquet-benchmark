import matplotlib.pyplot as plt
import re

# Log file path
LOG_PATH = "results/benchmark_log.txt"

# Containers
labels = []
csv_times = []
parquet_times = []
csv_mems = []
parquet_mems = []

with open(LOG_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Split log by run blocks
blocks = content.strip().split("-" * 40)

# Parse each block
for block in blocks:
    if "CSV" in block and "Parquet" in block:
        try:
            csv_time = float(re.search(r"CSV.*Time: ([\d.]+)", block).group(1))
            csv_mem = float(re.search(r"CSV.*Memory: ([\d.]+)", block).group(1))
            parquet_time = float(re.search(r"Parquet.*Time: ([\d.]+)", block).group(1))
            parquet_mem = float(re.search(r"Parquet.*Memory: ([\d.]+)", block).group(1))

            label = "Warm" if "Warm Cache" in block else "Cold"
            labels.append(label)

            csv_times.append(csv_time)
            csv_mems.append(csv_mem)
            parquet_times.append(parquet_time)
            parquet_mems.append(parquet_mem)

        except AttributeError:
            print(f"[WARNING] Could not parse block:\n{block}")



# Plot 1: Load Time
x = range(len(labels))
plt.figure()
plt.bar(x, csv_times, label="CSV", width=0.4, align="center")
plt.bar([i + 0.4 for i in x], parquet_times, label="Parquet", width=0.4, align="center")
plt.xticks([i + 0.2 for i in x], labels)
plt.ylabel("Time (sec)")
plt.title("File Load Time: CSV vs Parquet")
plt.legend()
plt.tight_layout()
plt.savefig("results/load_time_comparison.png")
plt.close()

# Plot 2: Memory Usage
plt.figure()
plt.bar(x, csv_mems, label="CSV", width=0.4, align="center")
plt.bar([i + 0.4 for i in x], parquet_mems, label="Parquet", width=0.4, align="center")
plt.xticks([i + 0.2 for i in x], labels)
plt.ylabel("Memory (MB)")
plt.title("Memory Usage: CSV vs Parquet")
plt.legend()
plt.tight_layout()
plt.savefig("results/memory_usage_comparison.png")
plt.close()

print("✅ Visualization completed! Graphs saved in /results/")
