import yfinance as yf
import matplotlib.pyplot
import seaborn


class Stock:
    def __init__(self, name):
        self.name = name
        self.stock = yf.Ticket(name.upper())

    def get_name(self):
        return self.name

    def get_info(self):
        return self.stock.info

    def get_history(self, period):
        return self.stock.history(period=period)

    def get_plot(self, period, label):
        hist = self.get_history(period)
        return hist[label].plot(figsize=(16, 9))

def main(name, function):
    stock = Stock(name)
    match function:
        case 'info':
            return stock.get_info()
        case 'history':
            return stock.get_history()
        case 'plot':
            stock.get_plot()
            return
        