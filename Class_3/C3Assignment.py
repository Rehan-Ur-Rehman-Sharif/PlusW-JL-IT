# todo list (simple)
tasks = []


def add(task):
    tasks.append(task)


def remove(task):
    if task in tasks:
        tasks.remove(task)


def display():
    for task in tasks:
        print(task)


add("Learn japanese")
add("Complete Assignment")
display()
remove("Complete Assignment")
display()


# Find Maximum and Minimum Values in a List


def minmax(N):
    max = N[0]
    min = N[0]
    for n in N:
        if n > max:
            max = n
        if n < min:
            min = n
    return max, min


numbers = [3, 9, 2, 8, 1]
max, min = minmax(numbers)
print(f"Max: {max}, Min: {min}")

# phone book using dictionaries
phonebook = {}


def add_contact(name, number):
    phonebook[name] = number


def get_number(name):
    return phonebook.get(name, "Unable to Find Contact")


add_contact("Someone", "+923182467812")
add_contact("Rehan", "+923448075059")
print(get_number("Rehan"))


# inventory

inv = {}


def add_item(item, quantity):
    if item in inv:
        inv[item] += quantity
    else:
        inv[item] = quantity


def remove_item(item, quantity):

    if item in inv and inv[item] >= quantity:
        inv[item] -= quantity

    if inv[item] == 0:
        del inv[item]
    else:
        print(f"Insufficient quantity of {item}.")


def view_inventory():
    for item, quantity in inv.items():
        print(f"{item}: {quantity}")


add_item("Apple", 10)
add_item("Banana", 5)
remove_item("Apple", 3)
view_inventory()


# Tracking Balance in Bank Account


def deposit(balance, amount):
    balance += amount
    print(f"Deposited: {amount}. New balance: {balance}")
    return balance  # Return the updated balance


def withdraw(balance, amount):
    if amount <= balance:
        balance -= amount
        print(f"Withdrew: {amount}. New balance: {balance}")
    else:
        print("Insufficient funds")
    return balance  # Return the updated balance


def check_balance(balance):
    print(f"Current balance: {balance}")


balance = 10000  # Initial balance
balance = deposit(balance, 4200)  # Deposit money
balance = withdraw(balance, 7000)  # Withdraw money
check_balance(balance)
