# Command-line Billing Application

A simple command-line billing application written in Python that allows users to:

- Add items with quantity and price
- View current bill with subtotal, tax (5%), and total
- Generate receipts that are saved to a text file

## Features

- Add multiple items with name, quantity and price per item
- View running bill total with tax calculation
- Generate and save receipts to `bill.txt`
- Clear bill after receipt generation
- Simple command-line interface with 4 options:
  1. Add Item
  2. View Current Bill 
  3. Generate Receipt
  4. Exit

## Usage

Run `billing.py` and follow the prompts to:
- Add items by entering name, quantity and price
- View the current bill at any time
- Generate a final receipt when done, which saves to `bill.txt`
- Exit the program

The bill includes:
- Itemized list with quantities and prices
- Subtotal
- 5% tax calculation
- Final total with tax
