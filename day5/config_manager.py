# config_manager.py
# This program demonstrates reading and writing JSON files
# using Python's built-in json module.

import json


def save_config(data: dict, filename: str) -> None:
    """Writes a dictionary to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_config(filename: str) -> dict:
    """Reads and returns data from a JSON file."""
    with open(filename, "r") as file:
        return json.load(file)


def update_config(filename: str, key: str, value) -> None:
    """Loads config, updates one key, and saves it."""
    config = load_config(filename)
    config[key] = value
    save_config(config, filename)


# Create initial config
config_data = {
    "model": "NeuralNetwork",
    "learning_rate": 0.001,
    "epochs": 10
}

filename = "config.json"

# Save config
save_config(config_data, filename)

print("Original Config:")
print(load_config(filename))

# Update epochs
update_config(filename, "epochs", 20)

print("\nUpdated Config:")
print(load_config(filename))


# Explore:
# json.dumps() converts Python data into a JSON string and returns it.
# json.dump() writes Python data directly into a JSON file.