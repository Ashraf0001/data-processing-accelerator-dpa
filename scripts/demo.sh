#!/bin/bash
# DPA Demo Script
# Showcases DPA's capabilities with sample data

echo "🚀 DPA (Data Processing Accelerator) Demo"
echo "=========================================="
echo ""

# Check if DPA is installed
if ! command -v dpa &> /dev/null; then
    echo "❌ DPA is not installed. Please install it first:"
    echo "   pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ dpa-cli==0.2.3"
    exit 1
fi

echo "✅ DPA is installed and ready!"
echo ""

# Create demo data if it doesn't exist
if [ ! -d "test_data" ]; then
    echo "📊 Generating demo data..."
    python scripts/generate_synthetic_data.py
    echo ""
fi

echo "🎯 Demo 1: Data Profiling"
echo "-------------------------"
echo "Let's analyze our customer data:"
dpa profile test_data/customers.csv
echo ""

echo "🎯 Demo 2: Data Filtering"
echo "-------------------------"
echo "Filtering Premium customers:"
dpa filter test_data/customers.csv -w "segment = 'Premium'" -o demo_premium_customers.csv
echo "✅ Created demo_premium_customers.csv"
echo ""

echo "🎯 Demo 3: Column Selection"
echo "---------------------------"
echo "Selecting key customer information:"
dpa select test_data/customers.csv -c "customer_id,name,segment,country" -o demo_customer_summary.csv
echo "✅ Created demo_customer_summary.csv"
echo ""

echo "🎯 Demo 4: Format Conversion"
echo "----------------------------"
echo "Converting CSV to Parquet (smaller file size):"
dpa convert test_data/customers.csv demo_customers.parquet
echo "✅ Created demo_customers.parquet"
echo ""

echo "🎯 Demo 5: Combined Operations"
echo "-----------------------------"
echo "Filtering high-value transactions and selecting key columns:"
dpa filter test_data/transactions.csv -w "final_amount > 1000" -s "transaction_id,customer_id,final_amount,transaction_date" -o demo_high_value_transactions.csv
echo "✅ Created demo_high_value_transactions.csv"
echo ""

echo "🎯 Demo 6: Performance Test"
echo "---------------------------"
echo "Processing large dataset (100k rows):"
time dpa profile test_data/web_analytics.csv
echo ""

echo "📊 Demo Results Summary"
echo "======================="
echo "Generated files:"
ls -la demo_*.csv demo_*.parquet 2>/dev/null | awk '{print "  " $9 " (" $5 " bytes)"}'
echo ""

echo "🎉 Demo completed successfully!"
echo ""
echo "💡 Try these commands yourself:"
echo "   dpa --help                    # Show all commands"
echo "   dpa profile <your_file.csv>   # Analyze your data"
echo "   dpa filter <file> -w 'condition' -o <output>  # Filter data"
echo "   dpa select <file> -c 'col1,col2' -o <output>  # Select columns"
echo "   dpa convert <input> <output>  # Convert formats"
echo ""
echo "📚 For more examples, see the README.md file"
