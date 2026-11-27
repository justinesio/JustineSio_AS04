def calculate_change(open_price, close_price):
    return close_price - open_price


def calculate_percent_change(open_price, close_price):
    change = close_price - open_price
    return (change / open_price) * 100


def get_market_status(change):
    if change > 0:
        return "GAIN"
    elif change < 0:
        return "LOSS"
    else:
        return "NO CHANGE"


def display_summary(stock_name, open_price, close_price, change, percent_change, status):
    print("\nDAILY STOCK SUMMARY")
    print(f"Stock: {stock_name}")
    print(f"Opening Price: {open_price:.2f}")
    print(f"Closing Price: {close_price:.2f}")
    print(f"Price Change: {change:+.2f}")
    print(f"Percent Change: {percent_change:+.2f}%")
    print(f"Status: {status}")


stock_name = input("Enter stock name: ")
open_price = float(input("Enter opening price: "))
close_price = float(input("Enter closing price: "))

price_change = calculate_change(open_price, close_price)
percent_change = calculate_percent_change(open_price, close_price)
market_status = get_market_status(price_change)

display_summary(
    stock_name,
    open_price,
    close_price,
    price_change,
    percent_change,
    market_status,
)