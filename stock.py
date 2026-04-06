# stock portfolio tracker
# calculate total investment
stock_prices={"DIXON":250,"AAPL":180,
              "TSLA":250,"META":300,"NVDA":190,
              "AMZN":210,"MSFT":290,"VVDN":310}
total=0
print("###~stock portfolio tracker~###")
print("stock available..",", ".join(stock_prices.keys()))
#user validation
while True:     
    symbol= input("enter stock (or 'done'):").upper()

    if symbol== "DONE":
        break

    if symbol not in stock_prices:
        print("stock not found. Try again!")
        continue

    quantity=int(input(f" quantity of {symbol}:"))
    investment = stock_prices[symbol] * quantity
    total += investment
    print(f" {symbol} * {quantity} = ${investment}\n")
print(f"\nTotal Investment: ${total}")    
    

