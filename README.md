# luck

A minimal Python module that returns `True` approximately 70% of the time.

## Installation

Install the package using pip:

```bash
pip install luck
```

For development installation:

```bash
pip install -e .
```

## Usage

Import and call the `is_lucky()` function:

```python
from luck import is_lucky

# Returns True approximately 70% of the time
if is_lucky():
    print("You're lucky!")
else:
    print("Not so lucky this time.")
```

## Behavior

The `is_lucky()` function returns `True` with approximately 70% probability and `False` with approximately 30% probability. Each call is independent and uses Python's `random.random()` function to determine the result.

## License

MIT

## Source

Migrated from: https://github.com/JohnAmadeo/luck.git
