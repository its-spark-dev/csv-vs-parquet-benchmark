# CSV vs Parquet Benchmark

This project benchmarks the performance of CSV and Parquet file formats using [Polars](https://www.pola.rs/) in Python. The focus is on **file loading speed** and **memory efficiency**, both **with and without OS-level cache**, across 50 identically structured files in each format.

---

## 📂 Project Structure

```
benchmark_project/
├── csv_data/ # 50 CSV files
├── parquet_data/ # 50 Parquet files
├── benchmark.py # Main benchmarking script
├── results/ # Benchmark results and plots
└── README.md
```

---

## ⚙️ Setup

### 1. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 2. Install dependencies

```bash
pip install polars pandas psutil matplotlib
```

---

## 🚀 Usage
Run the benchmark:

```bash
python benchmark.py
```
You can customize the script to test:
- Initial load time (cold cache)
- Repeated load time (warm cache)
- Memory usage via psutil
- Comparison between Polars and Pandas (optional)

---

## 📊 Results (TBA)

| Format  | Avg Load Time (Cold) | Avg Load Time (Warm) | Avg File Size |
| ------- | -------------------- | -------------------- | ------------- |
| CSV     | X.X sec              | X.X sec              | XXX MB        |
| Parquet | X.X sec              | X.X sec              | XX MB         |

These values are illustrative. Your results may vary depending on hardware and dataset.

---

## 📌 Why Parquet? (EXAMPLE)

Parquet is a columnar storage format optimized for:
- Faster load times
- Lower disk I/O
- Smaller file size (especially for repeated fields or numeric data)
- Efficient filtering and projection (read only required columns)

---

## 🧪 Benchmarked Using

- Python 3.10+
- Polars v0.20+
- Windows 10 / macOS (cross-platform)

---

## 🧾 License

This project is licensed under the MIT License.
See the LICENSE file for full details.

---

## 🙋‍♂️ Maintainer

Created by Sanghyeon Park
