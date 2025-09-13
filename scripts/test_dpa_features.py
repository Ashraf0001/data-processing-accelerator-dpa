#!/usr/bin/env python3
"""
Comprehensive DPA Feature Testing Script
Tests all DPA features with synthetic data
"""

import subprocess
import time
import os
import json
from pathlib import Path

class DPATester:
    def __init__(self):
        self.test_data_dir = Path("test_data")
        self.results = {
            "test_start": time.strftime("%Y-%m-%d %H:%M:%S"),
            "tests": [],
            "summary": {}
        }
        
    def run_command(self, cmd, description):
        """Run a command and record results"""
        print(f"\n🧪 {description}")
        print(f"   Command: {cmd}")
        
        start_time = time.time()
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
            end_time = time.time()
            
            test_result = {
                "description": description,
                "command": cmd,
                "success": result.returncode == 0,
                "duration": round(end_time - start_time, 2),
                "stdout": result.stdout,
                "stderr": result.stderr,
                "return_code": result.returncode
            }
            
            if result.returncode == 0:
                print(f"   ✅ SUCCESS ({test_result['duration']}s)")
            else:
                print(f"   ❌ FAILED ({test_result['duration']}s)")
                print(f"   Error: {result.stderr}")
            
            self.results["tests"].append(test_result)
            return test_result
            
        except subprocess.TimeoutExpired:
            print(f"   ⏰ TIMEOUT (300s)")
            test_result = {
                "description": description,
                "command": cmd,
                "success": False,
                "duration": 300,
                "stdout": "",
                "stderr": "Command timed out after 300 seconds",
                "return_code": -1
            }
            self.results["tests"].append(test_result)
            return test_result
    
    def test_basic_commands(self):
        """Test basic DPA commands"""
        print("\n" + "="*60)
        print("🔧 TESTING BASIC COMMANDS")
        print("="*60)
        
        # Test help
        self.run_command("dpa --help", "Show DPA help")
        
        # Test subcommand help
        self.run_command("dpa filter --help", "Show filter command help")
        self.run_command("dpa select --help", "Show select command help")
        self.run_command("dpa convert --help", "Show convert command help")
        self.run_command("dpa profile --help", "Show profile command help")
    
    def test_data_profiling(self):
        """Test data profiling features"""
        print("\n" + "="*60)
        print("📊 TESTING DATA PROFILING")
        print("="*60)
        
        # Test profiling on different datasets
        datasets = ["customers", "products", "transactions", "employees", "sales", "web_analytics"]
        
        for dataset in datasets:
            csv_file = self.test_data_dir / f"{dataset}.csv"
            if csv_file.exists():
                self.run_command(
                    f"dpa profile {csv_file}",
                    f"Profile {dataset} dataset"
                )
    
    def test_data_filtering(self):
        """Test data filtering features"""
        print("\n" + "="*60)
        print("🔍 TESTING DATA FILTERING")
        print("="*60)
        
        # Test filtering customers by segment
        self.run_command(
            "dpa filter test_data/customers.csv -w \"segment = 'Premium'\" -o test_output/customers_premium.csv",
            "Filter customers by Premium segment"
        )
        
        # Test filtering transactions by amount
        self.run_command(
            "dpa filter test_data/transactions.csv -w \"final_amount > 1000\" -o test_output/transactions_high_value.csv",
            "Filter high-value transactions (>$1000)"
        )
        
        # Test filtering with date range
        self.run_command(
            "dpa filter test_data/sales.csv -w \"date >= '2024-01-01'\" -o test_output/sales_recent.csv",
            "Filter sales from 2024 onwards"
        )
        
        # Test filtering with multiple conditions
        self.run_command(
            "dpa filter test_data/employees.csv -w \"department = 'Engineering' AND salary > 80000\" -o test_output/employees_engineering.csv",
            "Filter Engineering employees with salary > $80k"
        )
    
    def test_column_selection(self):
        """Test column selection features"""
        print("\n" + "="*60)
        print("📋 TESTING COLUMN SELECTION")
        print("="*60)
        
        # Test selecting specific columns
        self.run_command(
            "dpa select test_data/customers.csv -c 'customer_id,name,segment,country' -o test_output/customers_basic.csv",
            "Select basic customer information"
        )
        
        # Test selecting columns from transactions
        self.run_command(
            "dpa select test_data/transactions.csv -c 'transaction_id,customer_id,product_id,final_amount,transaction_date' -o test_output/transactions_summary.csv",
            "Select transaction summary columns"
        )
        
        # Test selecting columns from products
        self.run_command(
            "dpa select test_data/products.csv -c 'product_id,name,category,price,cost' -o test_output/products_pricing.csv",
            "Select product pricing information"
        )
    
    def test_data_conversion(self):
        """Test data format conversion"""
        print("\n" + "="*60)
        print("🔄 TESTING DATA CONVERSION")
        print("="*60)
        
        # Test CSV to Parquet conversion
        self.run_command(
            "dpa convert test_data/customers.csv test_output/customers_converted.parquet",
            "Convert customers CSV to Parquet"
        )
        
        # Test Parquet to CSV conversion
        self.run_command(
            "dpa convert test_data/products.parquet test_output/products_converted.csv",
            "Convert products Parquet to CSV"
        )
        
        # Test with different compression (if supported)
        self.run_command(
            "dpa convert test_data/transactions.csv test_output/transactions_compressed.parquet",
            "Convert transactions to Parquet"
        )
    
    def test_combined_operations(self):
        """Test combined filtering and selection"""
        print("\n" + "="*60)
        print("🔗 TESTING COMBINED OPERATIONS")
        print("="*60)
        
        # Filter and select in one operation
        self.run_command(
            "dpa filter test_data/transactions.csv -w \"final_amount > 500\" -s \"transaction_id,customer_id,final_amount,transaction_date\" -o test_output/transactions_filtered_selected.csv",
            "Filter high-value transactions and select key columns"
        )
        
        # Filter web analytics and convert
        self.run_command(
            "dpa filter test_data/web_analytics.csv -w \"device = 'Mobile'\" -o test_output/web_analytics_mobile.parquet",
            "Filter mobile sessions and convert to Parquet"
        )
        
        # Select and convert
        self.run_command(
            "dpa select test_data/sales.csv -c \"date,region,product,sales_amount\" -o test_output/sales_summary.parquet",
            "Select sales summary and convert to Parquet"
        )
    
    def test_performance_benchmarks(self):
        """Test performance on large datasets"""
        print("\n" + "="*60)
        print("⚡ TESTING PERFORMANCE BENCHMARKS")
        print("="*60)
        
        # Test profiling large dataset
        self.run_command(
            "dpa profile test_data/web_analytics.csv",
            "Profile large web analytics dataset (100k rows)"
        )
        
        # Test filtering large dataset
        self.run_command(
            "dpa filter test_data/web_analytics.csv -w \"browser = 'Chrome'\" -o test_output/web_analytics_chrome.csv",
            "Filter large dataset by browser"
        )
        
        # Test conversion of large dataset
        self.run_command(
            "dpa convert test_data/transactions.csv test_output/transactions_large.parquet",
            "Convert large transactions dataset (50k rows)"
        )
    
    def test_error_handling(self):
        """Test error handling"""
        print("\n" + "="*60)
        print("🚨 TESTING ERROR HANDLING")
        print("="*60)
        
        # Test with non-existent file
        self.run_command(
            "dpa profile nonexistent.csv",
            "Test with non-existent file"
        )
        
        # Test with invalid filter
        self.run_command(
            "dpa filter test_data/customers.csv -w \"invalid_column > 100\" -o test_output/invalid.csv",
            "Test with invalid column in filter"
        )
        
        # Test with invalid output format
        self.run_command(
            "dpa convert test_data/customers.csv test_output/invalid.xyz",
            "Test with invalid output format"
        )
    
    def create_output_directory(self):
        """Create output directory for test results"""
        os.makedirs("test_output", exist_ok=True)
        print("📁 Created test_output directory")
    
    def generate_summary(self):
        """Generate test summary"""
        total_tests = len(self.results["tests"])
        successful_tests = sum(1 for test in self.results["tests"] if test["success"])
        failed_tests = total_tests - successful_tests
        
        total_duration = sum(test["duration"] for test in self.results["tests"])
        
        self.results["summary"] = {
            "total_tests": total_tests,
            "successful_tests": successful_tests,
            "failed_tests": failed_tests,
            "success_rate": round((successful_tests / total_tests) * 100, 2) if total_tests > 0 else 0,
            "total_duration": round(total_duration, 2),
            "test_end": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        print("\n" + "="*60)
        print("📊 TEST SUMMARY")
        print("="*60)
        print(f"Total Tests: {total_tests}")
        print(f"Successful: {successful_tests}")
        print(f"Failed: {failed_tests}")
        print(f"Success Rate: {self.results['summary']['success_rate']}%")
        print(f"Total Duration: {self.results['summary']['total_duration']}s")
        
        if failed_tests > 0:
            print(f"\n❌ Failed Tests:")
            for test in self.results["tests"]:
                if not test["success"]:
                    print(f"  - {test['description']}")
                    if test["stderr"]:
                        print(f"    Error: {test['stderr'].strip()}")
    
    def save_results(self):
        """Save test results to file"""
        results_file = "test_output/dpa_test_results.json"
        with open(results_file, "w") as f:
            json.dump(self.results, f, indent=2)
        print(f"\n💾 Test results saved to: {results_file}")
    
    def run_all_tests(self):
        """Run all tests"""
        print("🚀 Starting comprehensive DPA feature testing...")
        print(f"📁 Test data directory: {self.test_data_dir}")
        
        # Create output directory
        self.create_output_directory()
        
        # Run all test suites
        self.test_basic_commands()
        self.test_data_profiling()
        self.test_data_filtering()
        self.test_column_selection()
        self.test_data_conversion()
        self.test_combined_operations()
        self.test_performance_benchmarks()
        self.test_error_handling()
        
        # Generate summary and save results
        self.generate_summary()
        self.save_results()
        
        print(f"\n🎉 Testing complete!")
        return self.results["summary"]["success_rate"]

def main():
    """Main test runner"""
    tester = DPATester()
    success_rate = tester.run_all_tests()
    
    if success_rate >= 90:
        print(f"\n🎊 Excellent! {success_rate}% success rate!")
        exit(0)
    elif success_rate >= 70:
        print(f"\n👍 Good! {success_rate}% success rate, but some issues to address.")
        exit(1)
    else:
        print(f"\n⚠️  Needs improvement! Only {success_rate}% success rate.")
        exit(2)

if __name__ == "__main__":
    main()
