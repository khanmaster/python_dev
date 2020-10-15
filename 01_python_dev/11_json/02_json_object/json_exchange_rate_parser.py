# we will build class to parse json file
# we have a json file with exchange rates

import json

class RateParser:

    def __init__(self, rate_file):
        rates_info = self._open_json_file(rate_file)
        # calling our private method to parse the file holding it in the rate_info
        # we'll create method down the line

        self.base = rates_info['base']
        self.date = rates_info['date']
        self.rates = rates_info['rates']
        self.aud = self.rates['AUD']
        self.gpb = self.rates['GBP']

    def _open_json_file(self, file):
        with open(file) as rates:
            return json.load(rates)

rates_reader = RateParser("exchange_rate.json")

print(rates_reader.base)
print(rates_reader.rates)