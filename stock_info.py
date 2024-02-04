import sys
from stock_data_def import *


class StockInfo:
    def __init__(self):
        self.code = None # VHM / VCB,...
        self.exchange = None  # HOSE/HNX/UPCOM
        self.company_name = None
        self.field = None # Bank / Real estate / Stock exchange,...

    def ToString(self):
        return ",".join([self.code, self.exchange, self.company_name, self.field])

    def FromString(self, input_string):
        values = input_string.split(',')
        if (len(values) != 4):
            print("Wrong format of stock info string: {0}".format(input_string))
            sys.exit(1)
        self.code = input_string[0].strip()
        self.exchange = input_string[1].strip()
        self.company_name = input_string[2].strip()
        self.field = input_string[3].strip()
