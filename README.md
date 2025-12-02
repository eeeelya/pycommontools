# pycommontools

A collection of common Python utilities and tools for your personal projects.

## Installation

```bash
pip install pycommontools
# or
uv add pycommontools
```

## Features

### Resources

**Singleton Metaclass** - Implement the singleton pattern easily:

```python
from pycommontools.resources.singleton import Singleton

class DatabaseConnection(metaclass=Singleton):
    def __init__(self, host: str):
        self.host = host

# Both instances will be the same object
db1 = DatabaseConnection("localhost")
db2 = DatabaseConnection("localhost")
assert db1 is db2  # True
```

### Configs

**Logger Setup** - Configure loggers with custom levels:

```python
from pycommontools.configs.logging import setup_logger
import logging

# Create a logger with DEBUG level
logger = setup_logger("myapp", level=logging.DEBUG)
logger.debug("Debug message")
logger.info("Info message")

# Create a logger with WARNING level
warn_logger = setup_logger("myapp.warnings", level="WARNING")
```

## Development

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

```bash
# Install dependencies
uv sync

# Run tests (when available)
uv run pytest
```

## Requirements

- Python 3.13+

## License

MIT
