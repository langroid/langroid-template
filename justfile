# Build and serve docs at http://127.0.0.1:8000
docs:
    @echo "Starting documentation server..."
    @echo "View docs at: http://127.0.0.1:8000"
    mkdocs build
    mkdocs serve
