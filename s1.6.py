def calculate_value_per_dollar(quantity, total_price):
    return quantity / total_price

def main():
    print("Value Calculator")
    print("This program calculates the value of a product based on the quantity and total price of the product.")
    print("First we'll need a little information from you.")

    # Define base units for each type, but will assume all inputs are in the same unit now
    print("Please select the type of units you will use for all products:")
    print("1. Volume (liquids)")
    print("2. Weight")
    print("3. Area")
    unit_choice = input("Enter your choice (1, 2, or 3): ")

    while unit_choice not in ['1', '2', '3']:
        print("Invalid choice. Please enter a valid option (1, 2, or 3).")
        unit_choice = input("Enter your choice (1, 2, or 3): ")

    if unit_choice == '1':
        print("Enter the volume unit (e.g., cups, mL, ounces, liters): ")
    elif unit_choice == '2':
        print("Enter the weight unit (e.g., ounces, lbs, grams, kg): ")
    elif unit_choice == '3':
        print("Enter the area unit (e.g., square inches, square meters, hectares): ")
    unit_sub_choice = input()

    products = []

    while True:
        # Gather input for product
        quantity = float(input(f"Enter the quantity in {unit_sub_choice}: "))
        total_price = float(input("Enter the total price of the product in dollars: "))

        value_per_dollar = calculate_value_per_dollar(quantity, total_price)
        products.append((value_per_dollar, f"{quantity:.2f} {unit_sub_choice} at ${total_price:.2f} total"))

        # Ask to compare more products
        more_products = input("Would you like to enter another product to compare? (yes/no): ").lower()
        if more_products != 'yes':
            break

    # Finding the product with the best value
    best_value = max(products, key=lambda x: x[0])
    print(f"The product with the best value is the {best_value[1]}, as it provides {best_value[0]:.2f} {unit_sub_choice} per dollar.")

if __name__ == "__main__":
    main()



