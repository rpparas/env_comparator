# Env Comparator

A simple script to compare two .env files to check keys missing in file2 relative to file1

## Installation

```
git clone https://github.com/rpparas/env_comparator.git
```

## Usage

```
# Recommended: Python3.6 or higher is installed
python compare_env_files.py .env1 .env2

# If you have Docker installed:
make run
```

## Testing

```
# Make sure you have pytest installed locally or in your virtual env
pip install requirements.txt
pytest .

# If you have Docker installed:
make test
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
