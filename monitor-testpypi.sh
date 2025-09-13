#!/bin/bash

# TestPyPI Version Monitor
# Monitors when dpa-cli version 0.2.3 becomes available on TestPyPI

echo "🔍 Monitoring TestPyPI for dpa-cli version 0.2.3..."
echo "Press Ctrl+C to stop monitoring"
echo ""

while true; do
    # Check if version 0.2.3 exists
    if curl -s "https://test.pypi.org/pypi/dpa-cli/0.2.3/json" > /dev/null 2>&1; then
        echo "✅ Version 0.2.3 found on TestPyPI!"
        echo "📦 Testing pip installation..."
        pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ dpa-cli==0.2.3 --dry-run
        
        echo "🧪 Testing uv installation..."
        mkdir -p /tmp/test-uv-final && cd /tmp/test-uv-final
        uv init --no-readme
        uv add --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ "dpa-cli==0.2.3"
        
        echo "🎉 TestPyPI version 0.2.3 is ready for testing!"
        break
    else
        echo "⏳ Version 0.2.3 not found yet... ($(date '+%H:%M:%S'))"
        sleep 30
    fi
done

