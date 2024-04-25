from converter import CurrencyConverter, combine_json_files
import tkinter as tk
from tkinter import ttk

# Combine the JSON files
combine_json_files()

# Create the converter object
converter = CurrencyConverter("combined_data.json")


class CurrencyConverterApp(tk.Tk):
    """
    A GUI class for the currency converter.

    Args:
        converter (CurrencyConverter): The CurrencyConverter object to use for conversion.


    """

    def __init__(self, converter):
        """
        Initialize the CurrencyConverterApp.

        Args:
            converter (CurrencyConverter): The CurrencyConverter object to use for conversion.

        :param converter:
        """
        super().__init__()

        self.converter = converter

        # Set the title
        self.title("Valuto kenverto")

        # Create variables
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()
        self.amount_var = tk.DoubleVar()
        self.result_var = tk.DoubleVar()

        # Set default values
        self.from_currency_var.set("Swedish Krona")
        self.to_currency_var.set("US Dollar")

        self.create_widgets()

    def create_widgets(self):
        """
        Create the widgets for the GUI.

        :return:
        """
        from_currency_label = ttk.Label(self, text="From currency:")
        from_currency_combobox = ttk.Combobox(self, textvariable=self.from_currency_var)
        to_currency_label = ttk.Label(self, text="To currency:")
        to_currency_combobox = ttk.Combobox(self, textvariable=self.to_currency_var)
        amount_label = ttk.Label(self, text="Amount:")
        amount_entry = ttk.Entry(self, textvariable=self.amount_var)
        convert_button = ttk.Button(self, text="Convert", command=self.convert)
        result_label = ttk.Label(self, text="Result:")
        result_label = ttk.Label(self, textvariable=self.result_var)

        # Layout the widgets
        from_currency_label.grid(row=0, column=0, sticky="w")
        from_currency_combobox.grid(row=0, column=1, sticky="ew")
        to_currency_label.grid(row=1, column=0, sticky="w")
        to_currency_combobox.grid(row=1, column=1, sticky="ew")
        amount_label.grid(row=2, column=0, sticky="w")
        amount_entry.grid(row=2, column=1, sticky="ew")
        convert_button.grid(row=3, column=0, columnspan=2, sticky="ew")
        result_label.grid(row=4, column=0, columnspan=2, sticky="w")

        # Populate the comboboxes
        currencies = list(self.converter.data.keys())
        from_currency_combobox["values"] = currencies
        to_currency_combobox["values"] = currencies

    def convert(self):
        """
        Convert the currency and update the result label.


        :return:
        """
        from_currency = self.from_currency_var.get()
        to_currency = self.to_currency_var.get()
        amount = self.amount_var.get()

        result = self.converter.convert(from_currency, to_currency, amount)
        self.result_var.set(result)


# Create the app and run the main loop
app = CurrencyConverterApp(converter)
app.mainloop()
