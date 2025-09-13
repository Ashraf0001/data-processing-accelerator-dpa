#!/usr/bin/env python3
"""
Synthetic Data Generator for DPA Testing
Generates realistic datasets to test all DPA features
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os
import json

def generate_customers_data(n_customers=10000):
    """Generate synthetic customer data"""
    print(f"🏪 Generating {n_customers} customers...")
    
    # Customer segments
    segments = ['Premium', 'Standard', 'Basic', 'Enterprise']
    countries = ['US', 'CA', 'UK', 'DE', 'FR', 'JP', 'AU', 'BR', 'IN', 'CN']
    industries = ['Technology', 'Finance', 'Healthcare', 'Retail', 'Manufacturing', 'Education', 'Government']
    
    data = []
    for i in range(n_customers):
        customer = {
            'customer_id': f'CUST_{i+1:06d}',
            'name': f'Customer {i+1}',
            'email': f'customer{i+1}@example.com',
            'segment': random.choice(segments),
            'country': random.choice(countries),
            'industry': random.choice(industries),
            'registration_date': (datetime.now() - timedelta(days=random.randint(30, 1095))).strftime('%Y-%m-%d'),
            'annual_revenue': random.randint(100000, 10000000),
            'employee_count': random.randint(10, 5000),
            'is_active': random.choice([True, False]),
            'credit_score': random.randint(300, 850),
            'last_login': (datetime.now() - timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d %H:%M:%S')
        }
        data.append(customer)
    
    return pd.DataFrame(data)

def generate_products_data(n_products=1000):
    """Generate synthetic product data"""
    print(f"📦 Generating {n_products} products...")
    
    categories = ['Electronics', 'Clothing', 'Books', 'Home & Garden', 'Sports', 'Beauty', 'Automotive', 'Toys']
    brands = ['TechCorp', 'StyleCo', 'BookWorld', 'GardenPro', 'SportMax', 'BeautyPlus', 'AutoTech', 'ToyLand']
    
    data = []
    for i in range(n_products):
        base_price = random.uniform(10, 1000)
        product = {
            'product_id': f'PROD_{i+1:06d}',
            'name': f'Product {i+1}',
            'category': random.choice(categories),
            'brand': random.choice(brands),
            'price': round(base_price, 2),
            'cost': round(base_price * random.uniform(0.3, 0.7), 2),
            'weight': round(random.uniform(0.1, 50), 2),
            'dimensions': f"{random.randint(5, 100)}x{random.randint(5, 100)}x{random.randint(5, 100)}",
            'is_digital': random.choice([True, False]),
            'stock_quantity': random.randint(0, 1000),
            'reorder_level': random.randint(10, 100),
            'supplier_id': f'SUPP_{random.randint(1, 50):03d}',
            'launch_date': (datetime.now() - timedelta(days=random.randint(0, 730))).strftime('%Y-%m-%d'),
            'rating': round(random.uniform(1, 5), 1),
            'review_count': random.randint(0, 1000)
        }
        data.append(product)
    
    return pd.DataFrame(data)

def generate_transactions_data(n_transactions=50000, customers_df=None, products_df=None):
    """Generate synthetic transaction data"""
    print(f"💳 Generating {n_transactions} transactions...")
    
    if customers_df is None or products_df is None:
        raise ValueError("Customers and products dataframes are required")
    
    customer_ids = customers_df['customer_id'].tolist()
    product_ids = products_df['product_id'].tolist()
    product_prices = dict(zip(products_df['product_id'], products_df['price']))
    
    data = []
    for i in range(n_transactions):
        customer_id = random.choice(customer_ids)
        product_id = random.choice(product_ids)
        quantity = random.randint(1, 10)
        base_price = product_prices[product_id]
        
        # Add some price variation
        price_variation = random.uniform(0.8, 1.2)
        unit_price = round(base_price * price_variation, 2)
        total_amount = round(unit_price * quantity, 2)
        
        # Add discounts
        discount_rate = random.uniform(0, 0.3) if random.random() < 0.3 else 0
        discount_amount = round(total_amount * discount_rate, 2)
        final_amount = round(total_amount - discount_amount, 2)
        
        transaction = {
            'transaction_id': f'TXN_{i+1:08d}',
            'customer_id': customer_id,
            'product_id': product_id,
            'quantity': quantity,
            'unit_price': unit_price,
            'total_amount': total_amount,
            'discount_rate': round(discount_rate, 3),
            'discount_amount': discount_amount,
            'final_amount': final_amount,
            'transaction_date': (datetime.now() - timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d %H:%M:%S'),
            'payment_method': random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer', 'Cash']),
            'channel': random.choice(['Online', 'Store', 'Mobile App', 'Phone']),
            'region': random.choice(['North', 'South', 'East', 'West', 'Central']),
            'is_return': random.choice([True, False]) if random.random() < 0.05 else False,
            'return_reason': random.choice(['Defective', 'Wrong Size', 'Not Satisfied', 'Changed Mind']) if random.random() < 0.05 else None
        }
        data.append(transaction)
    
    return pd.DataFrame(data)

def generate_employees_data(n_employees=500):
    """Generate synthetic employee data"""
    print(f"👥 Generating {n_employees} employees...")
    
    departments = ['Engineering', 'Sales', 'Marketing', 'HR', 'Finance', 'Operations', 'Customer Service']
    positions = ['Manager', 'Senior', 'Mid-level', 'Junior', 'Intern']
    
    data = []
    for i in range(n_employees):
        department = random.choice(departments)
        position = random.choice(positions)
        
        # Salary based on position and department
        base_salary = {
            'Manager': random.randint(80000, 150000),
            'Senior': random.randint(60000, 120000),
            'Mid-level': random.randint(40000, 80000),
            'Junior': random.randint(30000, 50000),
            'Intern': random.randint(20000, 35000)
        }
        
        employee = {
            'employee_id': f'EMP_{i+1:05d}',
            'name': f'Employee {i+1}',
            'email': f'employee{i+1}@company.com',
            'department': department,
            'position': position,
            'salary': base_salary[position],
            'hire_date': (datetime.now() - timedelta(days=random.randint(30, 1825))).strftime('%Y-%m-%d'),
            'manager_id': f'EMP_{random.randint(1, 50):05d}' if position != 'Manager' else None,
            'location': random.choice(['New York', 'San Francisco', 'London', 'Berlin', 'Tokyo', 'Remote']),
            'is_active': random.choice([True, False]),
            'performance_score': round(random.uniform(1, 5), 1),
            'years_experience': random.randint(0, 20)
        }
        data.append(employee)
    
    return pd.DataFrame(data)

def generate_sales_data(n_records=25000):
    """Generate synthetic sales data with time series patterns"""
    print(f"📈 Generating {n_records} sales records...")
    
    regions = ['North America', 'Europe', 'Asia Pacific', 'Latin America', 'Middle East & Africa']
    products = [f'Product_{i}' for i in range(1, 101)]
    
    data = []
    start_date = datetime.now() - timedelta(days=365)
    
    for i in range(n_records):
        # Create time series with some seasonality
        days_offset = random.randint(0, 365)
        record_date = start_date + timedelta(days=days_offset)
        
        # Add some seasonal patterns
        month = record_date.month
        seasonal_multiplier = 1.0
        if month in [11, 12]:  # Holiday season
            seasonal_multiplier = 1.5
        elif month in [6, 7, 8]:  # Summer
            seasonal_multiplier = 1.2
        
        base_sales = random.randint(1000, 10000)
        sales_amount = round(base_sales * seasonal_multiplier, 2)
        
        record = {
            'date': record_date.strftime('%Y-%m-%d'),
            'region': random.choice(regions),
            'product': random.choice(products),
            'sales_amount': sales_amount,
            'units_sold': random.randint(1, 100),
            'sales_rep': f'Rep_{random.randint(1, 50):03d}',
            'customer_type': random.choice(['Enterprise', 'SMB', 'Individual']),
            'discount_applied': random.choice([True, False]),
            'promotion_id': f'PROMO_{random.randint(1, 20):03d}' if random.random() < 0.3 else None
        }
        data.append(record)
    
    return pd.DataFrame(data)

def generate_web_analytics_data(n_sessions=100000):
    """Generate synthetic web analytics data"""
    print(f"🌐 Generating {n_sessions} web sessions...")
    
    pages = ['/home', '/products', '/about', '/contact', '/blog', '/pricing', '/login', '/signup']
    devices = ['Desktop', 'Mobile', 'Tablet']
    browsers = ['Chrome', 'Safari', 'Firefox', 'Edge', 'Opera']
    countries = ['US', 'CA', 'UK', 'DE', 'FR', 'JP', 'AU', 'BR', 'IN', 'CN']
    
    data = []
    for i in range(n_sessions):
        session_duration = random.randint(10, 3600)  # 10 seconds to 1 hour
        page_views = random.randint(1, 20)
        
        session = {
            'session_id': f'SESS_{i+1:08d}',
            'user_id': f'USER_{random.randint(1, 10000):06d}',
            'timestamp': (datetime.now() - timedelta(seconds=random.randint(0, 86400*30))).strftime('%Y-%m-%d %H:%M:%S'),
            'page': random.choice(pages),
            'device': random.choice(devices),
            'browser': random.choice(browsers),
            'country': random.choice(countries),
            'session_duration': session_duration,
            'page_views': page_views,
            'bounce_rate': random.uniform(0, 1),
            'conversion': random.choice([True, False]) if random.random() < 0.05 else False,
            'traffic_source': random.choice(['Organic', 'Paid', 'Direct', 'Social', 'Email', 'Referral']),
            'campaign_id': f'CAMP_{random.randint(1, 50):03d}' if random.random() < 0.2 else None
        }
        data.append(session)
    
    return pd.DataFrame(data)

def main():
    """Generate all synthetic datasets"""
    print("🚀 Starting synthetic data generation...")
    print("=" * 50)
    
    # Create data directory
    os.makedirs('test_data', exist_ok=True)
    
    # Generate datasets
    datasets = {}
    
    # Core business data
    datasets['customers'] = generate_customers_data(10000)
    datasets['products'] = generate_products_data(1000)
    datasets['transactions'] = generate_transactions_data(50000, datasets['customers'], datasets['products'])
    datasets['employees'] = generate_employees_data(500)
    datasets['sales'] = generate_sales_data(25000)
    datasets['web_analytics'] = generate_web_analytics_data(100000)
    
    # Save datasets
    print("\n💾 Saving datasets...")
    for name, df in datasets.items():
        csv_path = f'test_data/{name}.csv'
        parquet_path = f'test_data/{name}.parquet'
        
        # Save as CSV
        df.to_csv(csv_path, index=False)
        print(f"  ✅ {name}.csv ({len(df):,} rows)")
        
        # Save as Parquet
        df.to_parquet(parquet_path, index=False)
        print(f"  ✅ {name}.parquet ({len(df):,} rows)")
    
    # Generate metadata
    metadata = {
        'generated_at': datetime.now().isoformat(),
        'datasets': {
            name: {
                'rows': len(df),
                'columns': len(df.columns),
                'file_size_csv': f"{os.path.getsize(f'test_data/{name}.csv') / 1024 / 1024:.2f} MB",
                'file_size_parquet': f"{os.path.getsize(f'test_data/{name}.parquet') / 1024 / 1024:.2f} MB"
            }
            for name, df in datasets.items()
        }
    }
    
    with open('test_data/metadata.json', 'w') as f:
        json.dump(metadata, f, indent=2)
    
    print(f"\n📊 Dataset Summary:")
    print("=" * 50)
    for name, info in metadata['datasets'].items():
        print(f"  {name:15} | {info['rows']:>8,} rows | {info['columns']:>2} cols | CSV: {info['file_size_csv']:>8} | Parquet: {info['file_size_parquet']:>8}")
    
    print(f"\n🎉 Synthetic data generation complete!")
    print(f"📁 All files saved in: test_data/")
    print(f"📋 Metadata saved in: test_data/metadata.json")

if __name__ == "__main__":
    main()
