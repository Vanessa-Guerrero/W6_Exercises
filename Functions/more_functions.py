def display_mailing_label(name, address, city, state, zip):
    print(f"{name}\n{address}\n{city}, {state} {zip}\n")

def add_numbers(*args):
    result = sum(args)
    numbers = ''

    for x in args:
        if numbers:             # If numbers already has a value, add " + "
            numbers += ' + '
        numbers += str(x)       # Converts the number(x in args) to a string and adds it to the string numbers

    return f'{numbers} = {result}'

def display_receipt(total_due, amount_paid):
    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}\n")

    change_due = amount_paid - total_due

    if amount_paid >= total_due:
        print(f"Change Due: ${change_due:.2f}\n")
    else:
        # If the amount paid is less, show the remaining balance
        remaining_balance = total_due - amount_paid
        print(f"Remaining Balance: ${remaining_balance:.2f}\n")


# Calling display_mailing_label with two different people
display_mailing_label("Jane Doe", "123 Cedar St", "Chicago", "IL", "60601")
display_mailing_label("John Smith", "456 Pine Rd", "Chicago", "IL", "60601")

# Calling add_numbers with different amounts of arguments
add_numbers(5)                # One number
add_numbers(10, 20)           # Two numbers
add_numbers(1, 2, 3, 4, 5)    # Five numbers

# Calling display_receipt with different payment scenarios
display_receipt(50.00, 60.00)  # Overpaid
display_receipt(30.00, 30.00)  # Exact amount paid
display_receipt(40.00, 30.00)  # Underpaid