import json
from datetime import datetime

# Global variable
stock_data = {}

def add_item(item=None, qty=0, logs=None):
    """Add quantity of an item to inventory."""
    if logs is None:
        logs = []

    # Input validation
    if not isinstance(item, str) or not isinstance(qty, int):
        print("Invalid input! item must be string and qty must be integer.")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove quantity of an item from inventory."""
    try:
        if not isinstance(item, str) or not isinstance(qty, int):
            print("Invalid input! item must be string and qty must be integer.")
            return

        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found in inventory!")


def get_qty(item):
    """Get quantity of a specific item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load inventory data from file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        print("Inventory file not found. Starting with empty stock.")
        stock_data = {}
    except json.JSONDecodeError:
        print("Error reading file — resetting inventory.")
        stock_data = {}


def save_data(file="inventory.json"):
    """Save inventory data to file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f)


def print_data():
    """Print inventory items."""
    print("Items Report")
    for i in stock_data:
        print(f"{i} -> {stock_data[i]}")


def check_low_items(threshold=5):
    """Return items with quantity below threshold."""
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types now handled
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
