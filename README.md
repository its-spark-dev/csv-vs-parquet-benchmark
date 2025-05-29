# CSV vs Parquet Benchmark

This project benchmarks the performance of CSV and Parquet file formats using [Polars](https://www.pola.rs/) in Python. The focus is on **file loading speed** and **memory efficiency**, both **with and without OS-level cache**, across 50 identically structured files in each format.

---

## 📂 Project Structure

```
benchmark_project/
├── csv_data/               # 50 CSV files
├── parquet_data/           # 50 Parquet files
├── benchmark.py            # Main benchmarking script
├── results/                # Benchmark logs, .prof files, and plots
├── snakeviz_viewer_all.py  # Auto-opens SnakeViz for all profiles
└── README.md
```

---

## ⚙️ Setup

### 1. Create a virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate  # on Windows
# or
source venv/bin/activate  # on Unix/Mac
```

### 2. Install dependencies

```bash
pip install polars pandas psutil matplotlib snakeviz gprof2dot
```

---

## 🚀 Usage

### Run benchmark
```bash
# Run with cold cache (e.g., after reboot)
python benchmark.py --cache cold

# Run with warm cache (e.g., second run without reboot)
python benchmark.py --cache warm
```

### Visualize profiler output

Use one of the following options:

#### ▶️ Option A: SnakeViz (web-based, interactive)
```bash
python snakeviz_viewer_all.py
```
- Opens all `.prof` files in browser tabs automatically

#### 🖼️ Option B: gprof2dot (static image)
```bash
gprof2dot -f pstats results/profile_1.prof | dot -Tpng -o results/profile_1.png
```

---

## 🔍 About `benchmark.py`

The benchmark script:
- Loads all files in `csv_data/` and `parquet_data/` using Polars
- Measures **execution time** and **virtual memory (VMS)**
- Appends results to `results/benchmark_log.txt`
- Generates `.prof` files for profiling via `cProfile`
- Labels each run as Cold or Warm based on cache simulation strategy

---

## 📊 Sample Results (example)

| Cache Type | Format  | Time (sec) | Memory (MB) |
|------------|---------|------------|-------------|
| Cold       | CSV     | 0.292      | 32.61       |
| Cold       | Parquet | 0.823      | 205.07      |
| Warm       | CSV     | 0.258      | 14.85       |
| Warm       | Parquet | 0.823      | 132.87      |

> Note: Your results may differ depending on system specs and file structure.

---

## 📌 Why Parquet? (Context)

While Parquet is typically optimized for:
- Large-scale data pipelines
- Selective column reads (projection)
- Compression and disk efficiency

CSV may outperform Parquet for:
- Small or medium-size files
- Full-table reads
- Environments where simplicity and transparency matter

---

## 🧪 Benchmark Environment

- OS: Windows 10 Pro, Version 22H2, Build 19045.5854
- Python: 3.13.3 (64-bit)
- CPU: AMD Ryzen 5 5600X — 6 physical cores, 12 threads @ 3.70 GHz
- RAM: 15.92 GB
- GPU: NVIDIA GeForce RTX 3060

---

## 🧾 License

This project is licensed under the MIT License. See the LICENSE file for full details.

---

## 🙋‍♂️ Maintainer

Created and maintained by Sang Park

---

*"Tested like an engineer, visualized like a designer, reported like a professional."*
