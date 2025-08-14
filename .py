# Marquez Omar Higgins
# CIS261 week 6
# Invoice Line-Item Calculator
# 8/14/2025

def get_price():
    # Get and validate a price from user input
    while True:
        try:
            cost = float(input("Enter the cost of item:  "))
            #print(f"\nCost is: {cost:.2f}")
            return cost

        except ValueError:
            print("Invalid entry! Please enter a valid number.")


def get_quantity():
    # Get and validate a quantity from user input
    while True:
        try:
            quantity = int(input("Enter the quantity of items:  "))
            #print(f"\nQuantity is: {quantity}")
            return quantity

        except ValueError:
            print("Invalid entry! Please enter a valid number.")

def main():
    print("The Invoice Line Item Calculator\n")
    cost = get_price()
    quantity = get_quantity()
    total = cost * quantity
    print(f"\nPRICE:  {cost:.2F}")
    print(f"QUANTITY:  {quantity}")
    print(f"TOTAL: {total:.2f}")

# Funtion to run code  
if __name__ == "__main__":
    main()


# Loop to run payroll until user types "End"
while True:
    user_input = input("\nType 'N' to stop or press 'Y' to continue: ").strip()
    if user_input.lower() == "n":
        print("\nBye!.")
        break
    if __name__ == "__main__":
        main()



