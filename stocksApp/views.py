from django.shortcuts import render
from .models import Bond, Investor, Stock
import matplotlib.pyplot as plt

# Function to create the home page (index)
# The home page lists the owner, all the symbols for stocks and bonds
# The symbols are links to a separate page showing all data detail
def index(request):
    investorData = Investor.objects.get(investor_id=1)
    bondData = Bond.objects.get(bond_id=1)
    stockData = Stock.objects.all()
    context = {'investor': investorData, 'bond': bondData, 'stocks': stockData}
    return render(request, 'index.html', context)

# Function to render the bond page
# Shows only one bond data from the index page
# Prints all data including calculations for earnings/loss
# and yearly % earnings/loss for the bond 
def bond(request,id):
    investorData = Investor.objects.get(investor_id=1)
    bondData = Bond.objects.get(bond_id=id)
    context = {'investor': investorData, 'bond': bondData}
    return render(request, 'bond.html', context)

# Function to render the stock page
# Shows only one stock data per stock id from the index page
# Prints all data including calculations for earnings/loss
# and yearly % earnings/loss for each stock
def stock(request,id):
    investorData = Investor.objects.get(investor_id=1)
    stockData = Stock.objects.get(stock_id=id)
    context = {'investor': investorData, 'stock': stockData}
    return render(request, 'stock.html', context)

# Function to show all stock data to the view
# Prints all data including calculations for earnings/loss
# and yearly % earnings/loss for each stock and bond 
def allstocks(request):
    investorData = Investor.objects.get(investor_id=1)
    bondData = Bond.objects.get(bond_id=1)
    stockData = Stock.objects.all()
    context = {'investor': investorData, 'bond': bondData, 'stocks': stockData}
    return render(request, 'allstocks.html', context)

# Function to print a pie chart to the view
# The pie chart shows all wedges in percentage
# The largest wedge is calculated and exploded
def chart(request):
    stockData = Stock.objects.all()
    symbols = []  # Stock labels
    prices = []  # List of current stock prices
    explode = [] # For exploding the largest wedge of pie

    max_price = 0
    # Extract the stock symbols and current prices
    for stock in stockData:
        price = stock.current_price
        symbols.append(stock.stock_symbol)
        prices.append(price)

        # Finding the largest wedge of the pie
        if price > max_price:
            max_price = price
            explode.append(0.03)
        else:
            explode.append(0)
    
    # Preparing the figure and pie plot
    fig1, ax1 = plt.subplots()

    # Setting up the pie graph
    ax1.pie(prices,labels=symbols,explode=explode, autopct='%1.1f%%',  startangle=90)

    # The title of the graph
    plt.title('Distribution of company stocks')

    # Set to equal aspect ratio so pie is drawn as a circle
    ax1.axis('equal')  #

    # Save the plog to an image to the images directory
    # to be displayed on the template (browser)    
    plt.savefig('stocksApp/static/images/pie.png')

    return render(request,'chart.html')