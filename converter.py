import json
from get_api import CurrencyData

# URL for currency data
url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/eur.json"
names = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json"

# Filename for storing currency data
filename = "data.json"
fileNames = "names.json"

# Initialize CurrencyData object with filename and URL
currency_data = CurrencyData(filename, url)
name_data = CurrencyData(fileNames, names)
# Fetch data from the API
datan = currency_data.get_data()
name_data = name_data.get_data()


class CurrencyConverter:
    """
    A class to convert currency values.

    Attributes:
        filename (str): The filename of the JSON file containing currency data.
        data (dict): A dictionary containing currency conversion rates.
    """

    def __init__(self, filename):
        """
        Initialize CurrencyConverter with a filename and load data from JSON file.

        Args:
            filename (str): The filename of the JSON file containing currency data.
        """
        self.filename = filename
        self.load_data()

    def load_data(self):
        """
        Load currency data from the JSON file.
        """
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = None

    def get_currency_value(self, currency):
        """
        Get the value of a currency.

        Args:
            currency (str): The currency code.

        Returns:
            float or str: The currency value or an error message.
        """
        if not self.data:
            return "File not found."
        if currency in self.data:
            return self.data[currency]
        else:
            return f"Currency '{currency}' not found."

    def convert(self, currency_from, currency_to, amount):
        """
        Convert amount from one currency to another.

        Args:
            currency_from (str): The currency code to convert from.
            currency_to (str): The currency code to convert to.
            amount (float): The amount to convert.

        Returns:
            float or str: The converted amount in the target currency or an error message.
        """
        rate_from = self.get_currency_value(currency_from)
        rate_to = self.get_currency_value(currency_to)
        if isinstance(rate_from, str) or isinstance(rate_to, str):
            return "Currency not found."
        return (amount / rate_from) * rate_to


def combine_json_files():
    """
    Function to combines the keys from both JSON files and saves the combined data to a new file.

    :return:

    """
    with open('data.json') as f:
        data = json.load(f)
    with open("names.json") as f:
        names = json.load(f)

    # Extract "eur" data
    eur_data = data["eur"]
    # make a new dictionary with the full names instead of the short names
    new_data = {}
    for key, value in eur_data.items():
        new_data[names[key]] = value

    # Save the combined data to a new file
    with open("combined_data.json", "w") as f:
        json.dump(new_data, f, indent=4)
