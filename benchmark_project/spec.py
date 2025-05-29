import psutil
import platform

# CPU
print("CPU:", platform.processor())
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))

# RAM
ram_gb = psutil.virtual_memory().total / (1024 ** 3)
print(f"RAM: {ram_gb:.2f} GB")
