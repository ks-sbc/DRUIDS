#!/bin/bash
# Quick test to see if mkdocs serve starts successfully

echo "Testing mkdocs serve..."
mkdocs serve &
SERVER_PID=$!

# Wait a bit for server to start
sleep 3

# Check if process is still running
if ps -p $SERVER_PID > /dev/null; then
    echo "✅ MkDocs serve started successfully on PID $SERVER_PID"
    echo "Server is running at http://localhost:8000"
    echo "Press Ctrl+C to stop the server"
    wait $SERVER_PID
else
    echo "❌ MkDocs serve failed to start"
    exit 1
fi