# Data Processing Accelerator (DPA)

[![Rust](https://img.shields.io/badge/Rust-1.70+-orange.svg)](https://www.rust-lang.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![TestPyPI](https://img.shields.io/badge/TestPyPI-0.2.3-yellow.svg)](https://test.pypi.org/project/dpa-cli/)
[![Build Status](https://img.shields.io/github/actions/workflow/status/Ashraf0001/data-processing-accelerator-dpa/ci.yml)](https://github.com/Ashraf0001/data-processing-accelerator-dpa/actions)

**High-performance data processing tool built with Rust and Polars, featuring CLI and Python API**

DPA is a blazing-fast data processing tool designed for data scientists, analysts, and engineers who need to work with large datasets efficiently. Built on Rust and Polars, it provides enterprise-grade performance with an intuitive command-line interface.

## 🚀 What DPA Can Handle

### **Data Formats**
- **CSV files** - Comma-separated values with automatic type inference
- **Parquet files** - Columnar storage with compression support
- **Large datasets** - Tested on 100k+ rows with sub-second processing
- **Mixed data types** - Strings, numbers, dates, booleans, nulls

### **Data Operations**
- **📊 Data Profiling** - Comprehensive statistics and data quality insights
- **🔍 Advanced Filtering** - SQL-based WHERE conditions with complex logic
- **📋 Column Selection** - Choose specific columns for focused analysis
- **🔄 Format Conversion** - Seamless CSV ↔ Parquet conversion
- **⚡ Combined Operations** - Filter and select in single commands

### **Performance Features**
- **Rust-powered** - Memory-safe and incredibly fast
- **Polars engine** - Optimized columnar processing
- **Lazy evaluation** - Only processes data when needed
- **Parallel processing** - Multi-core utilization
- **Memory efficient** - Handles datasets larger than RAM

## 📦 Installation

### From TestPyPI (Recommended)

```bash
# Using pip
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ dpa-cli==0.2.3

# Using uv (faster)
uv pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ dpa-cli==0.2.3
```

### From Source

```bash
# Clone the repository
git clone https://github.com/Ashraf0001/data-processing-accelerator-dpa.git
cd data-processing-accelerator-dpa

# Build and install
cargo build --release
pip install -e python/
```

## 🎯 Quick Start

### 1. **Data Profiling**
Get instant insights into your data:

```bash
# Profile a CSV file
dpa profile data.csv

# Profile a Parquet file
dpa profile data.parquet
```

**Output includes:**
- Row and column counts
- Data types for each column
- Null value statistics
- Unique value counts
- Min/max/mean/std for numeric columns
- Memory usage

### 2. **Data Filtering**
Filter rows using SQL-like conditions:

```bash
# Filter by value
dpa filter data.csv -w "age > 25" -o filtered_data.csv

# Filter by string
dpa filter customers.csv -w "segment = 'Premium'" -o premium_customers.csv

# Complex conditions
dpa filter sales.csv -w "amount > 1000 AND region = 'North'" -o high_value_sales.csv

# Date filtering
dpa filter transactions.csv -w "date >= '2024-01-01'" -o recent_transactions.csv
```

### 3. **Column Selection**
Choose specific columns for analysis:

```bash
# Select specific columns
dpa select data.csv -c "id,name,email" -o selected_data.csv

# Select from large dataset
dpa select transactions.csv -c "transaction_id,amount,date" -o transaction_summary.csv
```

### 4. **Format Conversion**
Convert between CSV and Parquet:

```bash
# CSV to Parquet (smaller file size)
dpa convert data.csv data.parquet

# Parquet to CSV (human readable)
dpa convert data.parquet data.csv
```

### 5. **Combined Operations**
Filter and select in one command:

```bash
# Filter high-value transactions and select key columns
dpa filter transactions.csv -w "amount > 500" -s "id,customer,amount,date" -o high_value_summary.csv

# Filter mobile users and convert to Parquet
dpa filter users.csv -w "device = 'Mobile'" -o mobile_users.parquet
```

## 📊 Real-World Examples

### **E-commerce Analytics**
```bash
# Analyze customer segments
dpa profile customers.csv
dpa filter customers.csv -w "segment = 'Premium'" -o premium_customers.csv

# High-value transactions
dpa filter transactions.csv -w "amount > 1000" -s "transaction_id,customer_id,amount,date" -o high_value.csv

# Recent sales analysis
dpa filter sales.csv -w "date >= '2024-01-01'" -o sales_2024.csv
```

### **Web Analytics**
```bash
# Mobile traffic analysis
dpa filter web_logs.csv -w "device = 'Mobile'" -o mobile_traffic.csv

# Chrome users
dpa filter sessions.csv -w "browser = 'Chrome'" -s "session_id,user_id,duration,page_views" -o chrome_users.csv

# High engagement sessions
dpa filter analytics.csv -w "session_duration > 300 AND page_views > 5" -o engaged_users.csv
```

### **Financial Data**
```bash
# Large transactions
dpa filter transactions.csv -w "amount > 10000" -o large_transactions.csv

# Recent activity
dpa filter payments.csv -w "date >= '2024-01-01'" -s "payment_id,amount,method,date" -o recent_payments.csv

# Convert to Parquet for storage
dpa convert financial_data.csv financial_data.parquet
```

## 🔧 Advanced Usage

### **SQL-Style Filtering**
DPA supports SQL-like WHERE conditions:

```bash
# Numeric comparisons
dpa filter data.csv -w "age > 25 AND salary < 100000" -o filtered.csv

# String operations
dpa filter data.csv -w "name LIKE 'John%'" -o johns.csv

# Date ranges
dpa filter data.csv -w "date BETWEEN '2024-01-01' AND '2024-12-31'" -o year_2024.csv

# Multiple conditions
dpa filter data.csv -w "(status = 'Active' OR status = 'Premium') AND score > 80" -o active_high_score.csv
```

### **Performance Tips**
```bash
# Use Parquet for large datasets (3-10x smaller files)
dpa convert large_data.csv large_data.parquet

# Profile first to understand your data
dpa profile data.csv

# Combine operations to reduce I/O
dpa filter data.csv -w "condition" -s "col1,col2,col3" -o result.csv
```

## 📈 Performance Benchmarks

DPA has been tested on various dataset sizes:

| Dataset Size | Operation | Time | Memory |
|-------------|-----------|------|--------|
| 10k rows    | Profile   | 0.13s | 0.85MB |
| 50k rows    | Filter    | 0.14s | 1.77MB |
| 100k rows   | Convert   | 0.26s | 3.12MB |

**Performance highlights:**
- ⚡ **Sub-second processing** for most operations
- 🧠 **Memory efficient** - handles datasets larger than RAM
- 🔄 **Lazy evaluation** - only processes what you need
- 🚀 **Rust performance** - compiled to native machine code

## 🐍 Python API

DPA also provides a Python API for integration into your data pipelines:

```python
import dpa

# Profile data
stats = dpa.profile("data.csv")
print(f"Rows: {stats['rows']}, Columns: {stats['columns']}")

# Filter data
dpa.filter("data.csv", "age > 25", output="filtered.csv")

# Select columns
dpa.select("data.csv", ["id", "name", "email"], output="selected.csv")

# Convert format
dpa.convert("data.csv", "data.parquet")
```

## 🛠️ Command Reference

### **Profile Command**
```bash
dpa profile <input_file>
```
- Analyzes data structure and statistics
- Shows data types, null counts, unique values
- Displays memory usage and performance metrics

### **Filter Command**
```bash
dpa filter <input_file> -w <where_condition> [-s <columns>] -o <output_file>
```
- `-w, --where`: SQL-style WHERE condition
- `-s, --select`: Comma-separated column names (optional)
- `-o, --output`: Output file path

### **Select Command**
```bash
dpa select <input_file> -c <columns> -o <output_file>
```
- `-c, --columns`: Comma-separated column names
- `-o, --output`: Output file path

### **Convert Command**
```bash
dpa convert <input_file> <output_file>
```
- Converts between CSV and Parquet formats
- Automatically detects input/output formats
- Optimizes file size and performance

## 🔍 Data Quality Features

DPA provides comprehensive data quality insights:

- **Null value detection** - Identifies missing data
- **Data type validation** - Ensures consistent types
- **Unique value analysis** - Detects duplicates and patterns
- **Statistical summaries** - Min, max, mean, standard deviation
- **Memory usage tracking** - Optimize your data pipeline

## 🚀 Use Cases

### **Data Scientists**
- Quick data exploration and profiling
- Data cleaning and preprocessing
- Format conversion for different tools
- Performance-optimized data pipelines

### **Data Analysts**
- Fast filtering and aggregation
- Data quality assessment
- Report generation from large datasets
- Ad-hoc data analysis

### **Data Engineers**
- ETL pipeline optimization
- Data format standardization
- Performance monitoring
- Data validation and quality checks

### **Business Users**
- Self-service data analysis
- Quick insights from large datasets
- Data export and sharing
- Automated reporting

## 📚 Documentation

- **[Getting Started Guide](docs/getting-started/quick-start.md)** - Quick setup and first steps
- **[User Guide](docs/user-guide/overview.md)** - Comprehensive usage guide
- **[API Reference](docs/api/python-api.md)** - Python API documentation
- **[Examples](docs/examples/basic-usage.md)** - Real-world use cases
- **[Development Guide](docs/development/contributing.md)** - Contributing to DPA

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](docs/development/contributing.md) for details.

### **Development Setup**
```bash
git clone https://github.com/Ashraf0001/data-processing-accelerator-dpa.git
cd data-processing-accelerator-dpa

# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Install Python dependencies
pip install -r requirements-dev.txt

# Build and test
cargo build
cargo test
python -m pytest
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[Polars](https://pola.rs/)** - High-performance DataFrame library
- **[Rust](https://www.rust-lang.org/)** - Systems programming language
- **[PyO3](https://pyo3.rs/)** - Python-Rust bindings
- **[Clap](https://clap.rs/)** - Command-line argument parser

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/Ashraf0001/data-processing-accelerator-dpa/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Ashraf0001/data-processing-accelerator-dpa/discussions)
- **Documentation**: [GitHub Pages](https://ashraf0001.github.io/data-processing-accelerator-dpa/)

---

**Made with ❤️ and Rust** - Fast, safe, and reliable data processing for everyone.