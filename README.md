## Bank Operations Widget

This project provides a widget for displaying and processing bank operations data, including filtering and sorting.

Installation:

```bash
git clone https://github.com/nagibator228777/bank_nagibator.git
```

# Usage:

Run main.py:
```bash
python main.py
```

# Testing:

### New Test Coverage
Main application workflow

User input handling

Transaction display formatting

Category statistics calculation

Regex-based search functionality


Running Tests:
```bash
# Install dependencies
pip install pytest pytest-cov
```
```bash
# Run all tests
pytest tests/
```
```bash
# With coverage report
pytest --cov=src tests/
```
```bash
# HTML coverage report
pytest --cov=src --cov-report html
open htmlcov/index.html
```