import os
import time
import psutil
from datetime import datetime
import polars as pl

# Set the base directory (adjust this path if needed)
BASE_DIR = "C:/Users/spark/Documents/Git/csv-vs-parquet-benchmark/benchmark_project"
CSV_DIR = os.path.join(BASE_DIR, "csv_data")
PARQUET_DIR = os.path.join(BASE_DIR, "parquet_data")
RESULTS_PATH = os.path.join(BASE_DIR, "results", "benchmark_log.txt")

# Benchmark function to read all files in a folder using the specified reader
def benchmark_read_folder(folder_path: str, file_ext: str, read_func) -> tuple:
    process = psutil.Process(os.getpid())
    start_mem = process.memory_info().rss  # Memory at start (bytes)
    start_time = time.time()

    for file in os.listdir(folder_path):
        if file.endswith(file_ext):
            file_path = os.path.join(folder_path, file)
            _ = read_func(file_path)

    end_time = time.time()
    end_mem = process.memory_info().rss  # Memory at end (bytes)

    elapsed_time = round(end_time - start_time, 3)
    mem_used_mb = round((end_mem - start_mem) / (1024 ** 2), 2)  # Convert to MB

    return elapsed_time, mem_used_mb

# Main function to run the benchmark
def main():
    print("Starting benchmark...\n")

    if not os.path.exists(CSV_DIR):
        print(f"[ERROR] CSV folder not found: {CSV_DIR}")
        return
    if not os.path.exists(PARQUET_DIR):
        print(f"[ERROR] Parquet folder not found: {PARQUET_DIR}")
        return

    # Step 1: Warm-up run to simulate OS-level caching
    print("Running warm-up pass to simulate warm cache...\n")
    _ = benchmark_read_folder(CSV_DIR, ".csv", pl.read_csv)
    _ = benchmark_read_folder(PARQUET_DIR, ".parquet", pl.read_parquet)

    # Step 2: Measured run (Warm Cache)
    print("Running measured benchmark pass (Warm Cache)...\n")
    csv_time, csv_mem = benchmark_read_folder(CSV_DIR, ".csv", pl.read_csv)
    parquet_time, parquet_mem = benchmark_read_folder(PARQUET_DIR, ".parquet", pl.read_parquet)

    result = (
        f"Benchmark run at {datetime.now()} (Warm Cache)\n"
        f"CSV    → Time: {csv_time} sec | Memory: {csv_mem} MB\n"
        f"Parquet→ Time: {parquet_time} sec | Memory: {parquet_mem} MB\n"
        + "-" * 40 + "\n"
    )

    print(result)

    # Save the result with UTF-8 encoding
    with open(RESULTS_PATH, "a", encoding="utf-8") as f:
        f.write(result)

# Run the benchmark if this file is executed directly
if __name__ == "__main__":
    main()
