class Bill:
    def __init__(self):
        self.items = []
        self.subtotal = 0
        self.tax = (5/100)
    def add_item(self,item_nm,qty,price):
        self.items.append([item_nm,qty,price])
        self.subtotal += (qty * price)
    def view_bill(self):
        print("Current Bill: ")
        for item in self.items:
            print(f"- {item[0]} ({item[1]} @ {item[2]}₹): {item[1] * item[2]}")
        print(f"Subtotal: {self.subtotal}₹")
        print(f"Tax (5%): {self.tax * self.subtotal}₹")
        print(f"Total : {self.subtotal + (self.tax * self.subtotal)}₹")
    def generate_receipt(self):
        print("Receipt: ")
        for item in self.items:
            print(f"- {item[0]} ({item[1]} @ {item[2]}₹): {item[1] * item[2]}")
        print(f"Subtotal: {self.subtotal}₹")
        print(f"Tax (5%): {self.tax * self.subtotal}₹")
        print(f"Total : {self.subtotal + (self.tax * self.subtotal)}₹")
        print("Thank you for your purchase!")
        with open('bill.txt','w') as file:
            file.write("Receipt: ")
            file.write("\n")
            for item in self.items:
                file.write(f"- {item[0]} ({item[1]} @ {item[2]}rs): {item[1] * item[2]}")
                file.write("\n")
            file.write(f"Subtotal: {self.subtotal}rs")
            file.write("\n")
            file.write(f"Tax (5%): {self.tax * self.subtotal}rs")
            file.write("\n")
            file.write(f"Total : {self.subtotal + (self.tax * self.subtotal)}rs")
            file.write("\n")
            file.write("Thank you for your purchase!")
        self.items = []
        self.subtotal = 0


def main():
    print("Welcome to the Command-line Billing App!")
    print("1. Add Item")
    print("2. View Current Bill")
    print("3. Generate Receipt")
    print("4. Exit")
    for i in range(3):
        print()
    billone = Bill()
    while True:
        choose = int(input("Choose an option: "))
        if choose == 1:
            item = input("Enter item name: ")
            qty = int(input("Enter quantity: "))
            price = int(input("Enter price per item: "))
            #function
            billone.add_item(item,qty,price)
            print("Item added successfully!")
        elif choose == 2:
            billone.view_bill()
        elif choose == 3:
            billone.generate_receipt()
        elif choose == 4:
            print("Goodbye!")
            break
        else:
            print("Prompt not found!")
if __name__ == "__main__":
    main()