# Challenging the Parquet Dogma: CSV vs Parquet Benchmark

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)

> **“Tested like an engineer, visualized like a designer, reported like a professional.”**

## 🚀 Project Overview

This repository rigorously benchmarks the performance of CSV and Parquet file formats using [Polars](https://www.pola.rs/) in Python. It challenges common assumptions that Parquet universally outperforms CSV in all use cases. By analyzing file loading speed, memory efficiency, and runtime profiling under both cold (after reboot) and warm (cached) OS-level conditions, this project provides real-world, reproducible insights for data engineers and analysts.

---

## 🎯 Key Features & Technologies

* **Benchmarking:** Compare CSV and Parquet file formats for local analytics workflows
* **Polars:** Ultra-fast DataFrame operations (Rust backend)
* **psutil:** Precise per-process memory measurement
* **cProfile & SnakeViz:** In-depth runtime profiling and flame graph visualization
* **Matplotlib:** Automated result charting
* **Cross-platform:** Works on Windows, macOS, and Linux

---

## 📂 Project Structure

```
benchmark_project/
├── benchmark.py             # Main benchmarking script
├── analyze_profile.py       # Summarize cProfile results, generate images
├── generate_profile_images.py # Batch conversion to PNG via gprof2dot
├── snakeviz_viewer_all.py   # Opens all profiles in browser via SnakeViz
├── visualize_results.py     # Plots time/memory graphs from logs
├── requirements.txt         # Required Python packages
├── results/                 # Benchmark logs, .prof files, profile images (auto-generated)
├── sample_data/             # (Optional) Example CSV/Parquet for demo (not included by default)
└── README.md

docs/
├── challenging-the-parquet-dogma-tech-report.pdf   # Full technical report (PDF)
├── challenging-the-parquet-dogma-tech-report.pages # Apple Pages editable source
```

---

## ⚙️ Setup & Installation

1. **Clone this repository**

```bash
git clone https://github.com/its-spark-dev/csv-vs-parquet-benchmark.git
cd csv-vs-parquet-benchmark/benchmark_project
```

2. **(Recommended) Create a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate   # On Unix/macOS
venv\Scripts\activate     # On Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## 🚦 How to Run the Benchmark

### 1. **Prepare Data**

* By default, the script looks for `csv_data/` and `parquet_data/` in the project folder.
* These data folders are **not included in the repo** (to save space).

  * Use your own test files, or generate synthetic data as needed.
  * Optionally, add a few small sample files to `sample_data/` for quick demos.

### 2. **Run the Benchmark**

```bash
# Simulate cold cache (run after reboot or first run)
python benchmark.py --cache cold

# Simulate warm cache (repeat run)
python benchmark.py --cache warm
```

* Results (logs, .prof, .png) are written to `results/`.

### 3. **Visualize Results**

**Charts:**

```bash
python visualize_results.py
```

**Flame Graphs (SnakeViz):**

```bash
python snakeviz_viewer_all.py
```

**Static Profile Images:**

```bash
python analyze_profile.py
```

---

## 📊 Sample Results (from actual runs)

| Cache Type | Format  | Avg Time (sec) | Avg Memory (MB) |
| ---------- | ------- | -------------- | --------------- |
| Cold       | CSV     | 0.29           | 32.6            |
| Cold       | Parquet | 0.82           | 205.1           |
| Warm       | CSV     | 0.25           | 14.8            |
| Warm       | Parquet | 0.82           | 132.9           |

> **Note:** Despite Parquet’s reputation, CSV outperformed it for small files in these experiments. Profiling details and rationale are below.

---

## 🔥 Figure: SnakeViz Flame Graph Example

![SnakeViz Flame Graph](https://github.com/user-attachments/assets/0da3fb3f-dac1-4ad8-9ccc-1c9be3cd3a33)

**Figure.** Flame graph showing the call stack for reading Parquet files. Most time is spent in `collect()` during LazyFrame execution.

---


## 🔬 Profiling Analysis (Why CSV Was Faster)

* **Polars** loads Parquet via *lazy evaluation*, so `.collect()` triggers full data materialization — adds runtime overhead.
* **CSV** is read eagerly; no equivalent `.collect()` step.
* For many small files, CSV’s simplicity and reduced overhead produced superior performance in this context.
* See the included [technical report](https://github.com/its-spark-dev/csv-vs-parquet-benchmark/edit/main/README.md#-full-technical-report-downloads) and flame graph images for deep-dive analysis.

---

## 📌 When Parquet Is Still Better

Parquet still excels for:

* Large-scale, columnar queries
* Distributed/cloud-based data processing
* Selective I/O or columnar reads

**CSV** remains a better choice for:

* Simple, local batch jobs
* Lightweight analytics
* Immediate data access (no extra tooling)

---

## 🧪 Benchmark Environment

* OS: Windows 10 Pro, Version 22H2, Build 19045.5854
* Python: 3.13.3 (64-bit)
* CPU: AMD Ryzen 5 5600X — 6C/12T @ 3.70 GHz
* RAM: 15.9 GB
* GPU: NVIDIA GeForce RTX 3060

---

## 🗂️ Data Policy

> **Note:** Large-scale experimental data files (`csv_data/`, `parquet_data/`) are not included. To reproduce experiments, generate your own sample files or contact the maintainer. Example scripts or instructions can be provided.

---

## 📄 Full Technical Report (Downloads)

* [📄 Download PDF: Challenging the Parquet Dogma – Tech Report](docs/challenging-the-parquet-dogma-tech-report.pdf)
* [📝 Download Apple Pages (editable): Challenging the Parquet Dogma – Tech Report](docs/challenging-the-parquet-dogma-tech-report.pages)

  * The full report includes background, benchmarking methodology, results, profiling, and recommendations for real-world file format selection.

---

## 🙋 Maintainer & Contact

**Sanghyeon Park**

* [LinkedIn](https://www.linkedin.com/in/park3283/)
* [GitHub](https://github.com/its-spark-dev)

---

## 📝 License

[MIT License](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)

---

> *“Tested like an engineer, visualized like a designer, reported like a professional.”*
