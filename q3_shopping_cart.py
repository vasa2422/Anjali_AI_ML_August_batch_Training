# Shopping Cart Management System


# Create a new shopping cart
def create_cart(owner, discount=0):

    cart = {
        "owner": owner,
        "items": [],
        "discount": discount
    }

    return cart


# Add an item to the cart
def add_to_cart(cart, name, price, qty=1):

    item = {
        "name": name,
        "price": price,
        "qty": qty
    }

    cart["items"].append(item)

    print(name, "added to", cart["owner"], "'s cart")


# Try to modify a tuple
def update_price(price_tuple, new_price):

    try:
        price_tuple[0] = new_price

    except TypeError:
        print("Error: Tuple cannot be modified because tuples are immutable.")


# Calculate total price
def calculate_total(cart):

    total = 0

    for item in cart["items"]:

        total = total + (item["price"] * item["qty"])

    # Apply discount
    discount_amount = total * cart["discount"] / 100

    final_total = total - discount_amount

    return final_total


# Display cart
def show_cart(cart):

    print("\n-------------------------")
    print("Customer:", cart["owner"])
    print("Discount:", cart["discount"], "%")
    print("Items:")

    for item in cart["items"]:

        print(
            item["name"],
            "- Price:", item["price"],
            "- Quantity:", item["qty"]
        )

    total = calculate_total(cart)

    print("Final Total:", total)
    print("-------------------------")


# Main program
def main():

    # Create two separate carts
    cart1 = create_cart("Aarav", 10)
    cart2 = create_cart("Rahul", 5)

    # Add items to first customer's cart
    add_to_cart(cart1, "Laptop", 50000, 1)
    add_to_cart(cart1, "Mouse", 1000, 2)

    # Add items to second customer's cart
    add_to_cart(cart2, "Keyboard", 2000, 1)
    add_to_cart(cart2, "Headphones", 3000, 2)

    # Display both carts
    show_cart(cart1)
    show_cart(cart2)

    # Demonstrate tuple immutability
    price = (1000, "Mouse")

    print("\nOriginal tuple:", price)

    update_price(price, 1500)

    print("Tuple after attempt:", price)


# Start program
main()