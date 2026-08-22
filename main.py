import csv, json, random, datetime
stocks = {}
now = datetime.datetime.now()
def load_market():
    with open("stocks.csv",'r') as file:
        data = csv.DictReader(file)
        for row in data:
            stocks[row["Symbol"]] = float(row["Price"])
   
    return stocks 

load_market()
with open("portfolio.json",'r') as file:
    data = json.load(file)


def update_market(market):
    print("========== MARKET ==========")
    for stock in market:
        percent_change = (random.uniform(-5,5))
        market[stock] = round((market[stock]*(1 + percent_change/100)),2) 
        print(stock,"                ",market[stock])    
    return market
current_cash = data["Cash"]
class portfolio():
    def __init__(self,name):
        self.name = name
        self.quantity = data["Holding"][self.name]
        return
    @property
    def price(self):
        
        return stocks[self.name]
    def buy(self,quantity):
        global current_cash
        if current_cash - self.price*quantity >= 0:
            current_cash -= self.price*quantity
            self.quantity += quantity
            print(f"Succesfully bought {quantity} shares of {self.name}")
        else:
            print(f"Insufficient funds, you are short by {self.price*quantity - current_cash} rs")    
    def sell(self,quantity):
        global current_cash
        if self.quantity >= quantity:
            current_cash += self.price*quantity
            self.quantity -= quantity
            print(f"Succesfully sold {quantity} shares of {self.name}")
        else: 
            print(f"You only {self.quantity} units, short by {quantity - self.quantity} units.")    
def portfolio_overview(portfolio_object):
        print(f"""========== Your Portfolio ==========
Current Cash -                {current_cash}""")
        for pair in portfolio_objects.items():
            if pair[1].quantity > 0:
                print(f"{pair[1].name}                {pair[1].quantity} shares")
        print(f"Total Value                {sum(pair[1].price*pair[1].quantity for pair in portfolio_objects.items())}")
        
portfolio_objects = {stock:portfolio(stock) for stock in stocks}

def buy_sell_algo(stock,choice2):
    if choice2 == 3:
        general()
    quantity = int(input("How many units?: "))    
    if choice2 == 1:
        stock.buy(quantity)
        with open ("log.txt",'a') as file:
            file.write(f"\n{now} Bought {quantity} shares of {stock.name} ")
    if choice2 == 2:
        stock.sell(quantity)
        with open ("log.txt",'a') as file:
            file.write(f"\n{now} Sold {quantity}shares of {stock.name} ")

i = 1
second_choice = {}
for symbol,obj in portfolio_objects.items():
    second_choice[i] = obj 
    i += 1        
def stock_catalogue(choice):
    if choice == 0:
        portfolio_overview(portfolio_objects)
    if choice != 0:
        print(f"{second_choice[choice].name} price = {second_choice[choice].price},You own {second_choice[choice].quantity} shares. You have {current_cash} cash")
        print("1.Buy")
        print("2.Sell")
        print("3.Exit")
        choice2 = int(input("Enter input: "))
        buy_sell_algo(second_choice[choice],choice2) 
                  
def general():      
    global stocks
    print("Welcome to Stock Market:")
    print("1.View Market")
    print("2.TransactStocks")
    print("3.Exit")
    choice = int(input("Select Your Operation: "))  
    if choice == 1:
      stocks =  update_market(stocks)    
    if choice == 2:
        print("========== STOCKS ==========") 
        print("0.Portfolio Overview")
        for pair in second_choice.items():
            print(f"{pair[0]}.{pair[1].name}")
        choice = int(input("Serial Number of the Stock to view: "))
        stock_catalogue(choice)
    if choice == 3:
        exit()
          
general()  
with open("portfolio.json",'w') as file:
    data = {"Cash": current_cash, "Holding": {pair[1].name:pair[1].quantity for pair in portfolio_objects.items()}}
    writer = json.dump(data,file)
with open("stocks.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Symbol", "Price"])
    writer.writerows(stocks.items())
    