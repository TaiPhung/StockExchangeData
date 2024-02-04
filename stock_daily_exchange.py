import os
import sys
from stock_info import StockInfo

class StockDailyExchange:
    def __init__(self):
        self.stock_info = StockInfo()
        self.date = None
        self.total_volume = None
        self.total_value = None
        self.ref = None # Reference price open
        self.ceil = None # Ceil price open
        self.floor = None # Floor price open
        self.matched = None # Close price
        self.high = None # High price
        self.avg = None # Average price
        self.low = None # Low price
        self.foreign_bought = None
        self.foreign_sold = None

    def ToString(self):
        return ",".join([self.date, self.total_volume, self.total_value, self.ref, self.ceil,
            self.floor, self.matched, self.high, self.avg, self.low, self.foreign_bought,
            self.foreign_sold])

    def FromString(self, input_string):
        values = input_string.split(',')
        if (len(values) != 12):
            print("Wrong format of stock daily exchange data string: {0}".format(input_string))
            sys.exit(1)
        self.date = input_string[0].strip()
        self.total_volume = input_string[1].strip()
        self.total_value = input_string[2].strip()
        self.ref = input_string[3].strip()
        self.ceil = input_string[4].strip()
        self.floor = input_string[5].strip()
        self.matched = input_string[6].strip()
        self.high = input_string[7].strip()
        self.avg = input_string[8].strip()
        self.low = input_string[9].strip()
        self.foreign_bought = input_string[10].strip()
        self.foreign_sold = input_string[11].strip()

    # Daily exchange data will be saved into a specific file for a stock with the first line of
    # stock information
    def WriteToFile(self, target_file):
        if not os.path.exists(target_file):
            # Write the first line as information of stock
            with open(target_file, "w") as myfile:
                myfile.write(self.stock_info.ToString())
        # Write daily exchange data
        with open(target_file, "a") as myfile:
            myfile.write("\n")
            myfile.write(self.ToString())
