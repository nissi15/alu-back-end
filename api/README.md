# API

Python scripts that query the [JSONPlaceholder](https://jsonplaceholder.typicode.com/)
REST API for an employee's TODO list and display or export the results.

## Files

| File | Description |
| ---- | ----------- |
| `0-gather_data_from_an_API.py` | Prints an employee's TODO list progress |
| `1-export_to_CSV.py` | Exports an employee's tasks to `USER_ID.csv` |
| `2-export_to_JSON.py` | Exports an employee's tasks to `USER_ID.json` |
| `3-dictionary_of_list_of_dictionaries.py` | Exports all employees' tasks to `todo_all_employees.json` |

## Usage

```
$ python3 0-gather_data_from_an_API.py 2
$ python3 1-export_to_CSV.py 2
$ python3 2-export_to_JSON.py 2
$ python3 3-dictionary_of_list_of_dictionaries.py
```

## Requirements

- Python 3
- `requests`
