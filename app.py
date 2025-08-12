from operations import (
    add_operation, subtract_operation, multiply_operation, division_operation,
    modulus_operation, power_operation, square_root_operation,
    factorial_operation, absolute_value_operation, percentage_operation
)

def display_menu() -> None:
    """
    Prints the calculator menu options to the terminal.

    This function displays all available operations that the user can choose from,
    including basic arithmetic, advanced functions, and an option to quit.
    """

    print("\n=== Python Calculator ===")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")
    print("5) Modulus (remainder)")
    print("6) Power (a^b)")
    print("7) Square root")
    print("8) Factorial")
    print("9) Absolute value")
    print("10) Percentage (part of whole)")
    print("q) Quit")

def read_float(prompt: str) -> float:
    # Keep asking until the user gives a valid number
    while True:
        try:
            # input(prompt) shows the prompt message and waits for the user to type something
            # float(...) tries to convert the typed value into a float
            return float(input(prompt))
        except ValueError:
            # If the conversion fails (e.g., the user types "apple"),
            # Python raises a ValueError and we handle it here
            print("Please enter a valid number.")

def read_int(prompt: str) -> int:
    """
    Continuously prompts the user until a valid integer is entered.

    Parameters:
        prompt (str): The text displayed to the user.

    Returns:
        int: The integer value entered by the user.
    """

    while True: # Keep asking until valid input is given
        try:
            # Convert the input to an integer
            # If the user types a decimal or non-number, this will raise a ValueError
            return int(input(prompt))
        except ValueError:
            # Runs only if int(...) conversion fails
            print("Please enter a whole number (integer).")

# A mapping of menu choice -> (function, input_type, label)
OPERATIONS = {
    "1": (add_operation, 2, "Add"),
    "2": (subtract_operation, 2, "Subtract"),
    "3": (multiply_operation, 2, "Multiply"),
    "4": (division_operation, 2, "Divide"),
    "5": (modulus_operation, 2, "Modulus"),
    "6": (power_operation, 2, "Power"),
    "7": (square_root_operation, 1, "Square root"),
    "8": (factorial_operation, "int1", "Factorial"),
    "9": (absolute_value_operation, 1, "Absolute value"),
    "10": (percentage_operation, "pct", "Percentage"),
}

def run_calculator() -> None:
    """
    Runs the interactive menu-driven calculator.

    Displays the menu, reads the user's choice, collects the required inputs,
    calls the corresponding operation, and prints the result. Repeats until
    the user chooses to quit.
    """

    while True: # Main loop: keep running until the user quits
        display_menu()
        choice = input("Choose an option: ").strip().lower()

        # Exit conditions: allow several quit keywords
        if choice in ("q", "quit", "exit"):
            print("Goodbye!")
            break

        # Validate the menu choice against the OPERATIONS mapping
        if choice not in OPERATIONS:
            print("Invalid choice. Please try again.")
            continue

        # Unpack the mapping: function to call, input arity(number of arguments a function takes)/type, and label for display
        func, arity, label = OPERATIONS[choice]

        try:
            # Collect inputs according to the operation's arity/type
            if arity == 2:
                a = read_float("Enter first number (a): ")
                b = read_float("Enter second number (b): ")
                result = func(a, b)
            elif arity == 1:
                a = read_float("Enter the number: ")
                result = func(a)
            elif arity == "int1": # factorial: requires a single integer
                n = read_int("Enter a non-negative integer: ")
                result = func(n)
            elif arity == "pct": # percentage: requires part and whole
                part = read_float("Enter the part: ")
                whole = read_float("Enter the whole: ")
                result = func(part, whole)
            else:
                # Defensive branch: arity misconfigured in OPERATIONS
                print("Internal configuration error.")
                continue
        except (ValueError, ZeroDivisionError) as e:
            # Gracefully report common runtime errors from operations (e.g., divide by zero)
            print(f"Error: {e}")
            continue # Do not print a result; restart the loop
        
        # Some operations (e.g., invalid sqrt/percentage) may return None after printing an error
        if result is None:
            continue
        # Present the outcome with a friendly label
        print(f"{label} result: {result}")

if __name__ == "__main__":
    # Entry point so the script can be run directly:
    run_calculator()
