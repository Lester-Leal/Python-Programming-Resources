class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def add_quantity(self, amount):
        self.quantity += amount

    def update_quantity(self, amount):
        self.quantity = amount

    def display_details(self):
        print(f"Name: {self.name}, Quantity: {self.quantity}")


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity):
        item = self.find_item(name)
        if item:
            item.add_quantity(quantity)
            print("Item quantity updated successfully.")
        else:
            new_item = Item(name, quantity)
            self.items.append(new_item)
            print("Item added successfully.")

    def find_item(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None

    def update_item(self, name, quantity):
        item = self.find_item(name)
        if item:
            item.update_quantity(quantity)
            print("Item updated successfully.")
        else:
            print("Item not found.")

    def generate_report(self):
        if not self.items:
            print("No items in the inventory.")
        else:
            print("Inventory Report:")
            for item in self.items:
                item.display_details()

    def load_data(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    name, quantity = line.strip().split(',')
                    self.add_item(name, int(quantity))
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("File not found.")

    def save_data(self, filename):
        with open(filename, 'w') as file:
            for item in self.items:
                file.write(f"{item.name},{item.quantity}\n")
        print("Data saved successfully.")

    def remove_item(self, name):
        item = self.find_item(name)
        if item:
            self.items.remove(item)
            print("Item removed successfully.")
        else:
            print("Item not found.")

    def check_item_availability(self, name, quantity):
        item = self.find_item(name)
        if item:
            if item.quantity >= quantity:
                print("Item is available in the requested quantity.")
            else:
                print("Item is not available in the requested quantity.")
        else:
            print("Item not found.")

    def sell_item(self, name, quantity):
        item = self.find_item(name)
        if item:
            if item.quantity >= quantity:
                item.update_quantity(item.quantity - quantity)
                print("Item sold successfully.")
            else:
                print("Item is not available in the requested quantity.")
        else:
            print("Item not found.")


def display_menu():
    print("\nMenu:")
    print("1. Add an item")
    print("2. Update an item")
    print("3. Generate a report")
    print("4. Save data")
    print("5. Remove an item")
    print("6. Check item availability")
    print("7. Sell an item")
    print("8. Exit")


def main():
    inventory = Inventory()
    inventory.load_data("inventory.txt")

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            inventory.add_item(name, quantity)
        elif choice == "2":
            name = input("Enter item name to update: ")
            quantity = int(input("Enter new quantity: "))
            inventory.update_item(name, quantity)
        elif choice == "3":
            inventory.generate_report()
        elif choice == "4":
            inventory.save_data("inventory.txt")
        elif choice == "5":
            name = input("Enter item name to remove: ")
            inventory.remove_item(name)
        elif choice == "6":
            name = input("Enter item name to check availability: ")
            quantity = int(input("Enter desired quantity: "))
            inventory.check_item_availability(name, quantity)
        elif choice == "7":
            name = input("Enter item name to sell: ")
            quantity = int(input("Enter quantity to sell: "))
            inventory.sell_item(name, quantity)
        elif choice == "8":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
