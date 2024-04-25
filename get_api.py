import requests
import json
import os
from datetime import datetime


class CurrencyData:
    """
    A class to download and save currency data from an API.

    Attributes:
        filename (str): The filename to save the data to.
        url (str): The URL of the API to download the data from.

    """

    def __init__(self, filename, url):
        """
        Initialize the CurrencyData object with a filename and URL.

        Args:
            filename (str): The filename to save the data to.
            url (str): The URL of the API to download the data from.
        :param filename:
        :param url:
        """
        self.filename = filename
        self.url = url

    def _has_internet(self):
        """
        Check if there is an internet connection.

        Returns:
            bool: True if there is an internet connection, False otherwise.
        """
        try:
            requests.get("https://google.com", timeout=5)
            return True
        except requests.exceptions.ConnectionError:
            return False

    def _download_and_save_json(self):
        """
        Download JSON data from the API and save it to a file.

        Returns:
            None
        """
        response = requests.get(self.url)
        data = json.loads(response.content)

        with open(self.filename, "w") as f:
            json.dump(data, f)

    def get_data(self):
        """
        Get currency data from the API or file.

        Returns:
            dict: A dictionary containing currency data.

        """
        last_modified = None
        if os.path.exists(self.filename):
            last_modified = datetime.fromtimestamp(os.path.getmtime(self.filename))

        # Check if there is an internet connection
        if self._has_internet():
            # The file is missing or older than 1 hour
            if not last_modified or (datetime.now() - last_modified).total_seconds() / 3600 > 1:
                print("Laddar ner data...")
                self._download_and_save_json()
            else:
                print("Filen är redan uppdaterad.")
        else:
            print("Ingen internetanslutning. Använder befintlig fil...")

        # Read the data from the file
        with open(self.filename, "r") as f:
            data = json.load(f)

        return data

# makes a class that takes in filename and url
# checks if there is an internet connection with the requests.get method
# downloads and saves the json data from the api
# gets the currency data from the api or file based on the internet connection and the last modified date of the file
# returns the data
