# PK - Primary Key Implementation

A simple Python implementation demonstrating Primary Key (PK) concepts.

## Overview

This repository contains a Python module that implements a Primary Key manager, demonstrating core concepts of primary keys including:
- Unique identifier generation
- Data registration with PKs
- Data retrieval by PK
- PK existence checking
- Record deletion
- Listing all PKs

## Usage

### Basic Example

```python
from pk import PKManager

# Create a manager instance
manager = PKManager()

# Generate a new primary key
pk = manager.create_pk()

# Register data with the PK
manager.register(pk, {"name": "Alice", "age": 30})

# Retrieve data by PK
data = manager.get(pk)
print(data)  # {'name': 'Alice', 'age': 30}

# Check if PK exists
if manager.exists(pk):
    print("PK exists!")

# Delete a record
manager.delete(pk)

# Get all registered PKs
all_pks = manager.get_all_pks()
```

### Running the Example

```bash
python3 pk.py
```

## Testing

Run the test suite:

```bash
python3 -m unittest test_pk.py -v
```

## Features

- **Automatic PK Generation**: Sequential unique IDs starting from 1
- **Duplicate Prevention**: Ensures each PK is unique
- **Simple API**: Easy-to-use methods for CRUD operations
- **Comprehensive Tests**: Full test coverage with unittest

## Files

- `pk.py` - Main implementation of PKManager
- `test_pk.py` - Unit tests for PKManager
- `README.md` - This file