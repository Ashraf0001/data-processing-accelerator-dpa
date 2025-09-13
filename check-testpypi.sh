#!/bin/bash

# TestPyPI Package Checker
# Continuously checks if dpa-cli package is available on TestPyPI

echo "🔍 Monitoring TestPyPI for dpa-cli package..."
echo "Press Ctrl+C to stop monitoring"
echo ""

while true; do
    # Check if package exists
    if curl -s https://test.pypi.org/pypi/dpa-cli/json > /dev/null 2>&1; then
        echo "✅ Package found on TestPyPI!"
        echo "📦 Installing with pip..."
        pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ dpa-cli
        
        echo "🧪 Testing installation..."
        dpa --help
        python3 -c "import dpa_core; print('✅ dpa_core imported successfully')"
        
        echo "🎉 TestPyPI installation successful!"
        break
    else
        echo "⏳ Package not found yet... ($(date))"
        sleep 30  # Check every 30 seconds
    fi
done

