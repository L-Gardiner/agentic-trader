# Tests Directory

This directory contains integration and system-wide tests for the trading bot.

## Structure

- `integration/` - Integration tests between different domains
- `system/` - End-to-end system tests
- `fixtures/` - Test fixtures and mock data
- `conftest.py` - Shared pytest fixtures and configuration

## Running Tests

```bash
# Run all tests
pytest

# Run specific test category
pytest tests/integration/
pytest tests/system/

# Run with coverage
pytest --cov=domains
```
