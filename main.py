# 1. Hardcoded dictionary defining stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "NVDA": 130,
    "AMZN": 190
}

def run_portfolio_tracker():
    print("=== Welcome to the Stock Portfolio Tracker ===")
    print("Available stocks and their current prices:")
    for stock, price in STOCK_PRICES.items():
        print(f" - {stock}: ${price}")
    print("=============================================\n")

    portfolio = {}
    total_investment_value = 0

    # 2. User inputs stock names and quantities
    while True:
        stock_name = input("Enter the stock symbol you own (or type 'done' to finish): ").upper().strip()

        if stock_name == 'DONE':
            break

        if stock_name not in STOCK_PRICES:
            print(f"Sorry, '{stock_name}' is not in our system. Please try a valid stock from the list.")
            continue

        try:
            quantity = int(input(f"How many shares of {stock_name} do you own? "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
        except ValueError:
            print("Invalid input. Please enter a whole number for the quantity.")
            continue

        # If they enter the same stock twice, add the quantities together
        if stock_name in portfolio:
            portfolio[stock_name] += quantity
        else:
            portfolio[stock_name] = quantity
        print(f"Added {quantity} shares of {stock_name}.\n")

    # 3. Display total investment value
    if not portfolio:
        print("\nYour portfolio is empty. No data to save.")
        return

    print("\n================ PORTFOLIO SUMMARY ================")
    summary_lines = []

    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        # Basic arithmetic calculation
        stock_total = qty * price
        total_investment_value += stock_total

        line = f"{stock}: {qty} shares x ${price} = ${stock_total:,}"
        print(line)
        summary_lines.append(line)

    total_line = f"\nTotal Investment Value: ${total_investment_value:,}"
    print("---------------------------------------------------")
    print(total_line)
    print("===================================================")

    # 4. File handling: Save the result to a .txt file
    save_choice = input("\nWould you like to save this summary to a file? (yes/no): ").lower().strip()
    if save_choice in ['yes', 'y']:
        filename = "portfolio_summary.txt"
        with open(filename, "w") as file:
            file.write("STOCK PORTFOLIO SUMMARY\n")
            file.write("=======================\n")
            for line in summary_lines:
                file.write(line + "\n")
            file.write("-----------------------\n")
            file.write(total_line + "\n")
        print(f"Success! Portfolio saved to '{filename}'.")
    else:
        print("Summary not saved.")

if __name__ == "__main__":
    run_portfolio_tracker()