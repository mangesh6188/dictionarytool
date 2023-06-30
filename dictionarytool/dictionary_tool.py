# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=trailing-newlines
# pylint: disable=trailing-whitespace
# pylint: disable=missing-final-newline

import argparse
import logging
import requests

BASE_URL = "https://www.dictionaryapi.com/api/v3/references/collegiate/json"

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class DictionaryTool:
    def __init__(self, api_key):
        self.api_key = api_key

    def lookup_word(self, word):
        # MerriamWebster API URL
        url = f"{BASE_URL}/{word}?key={self.api_key}"
        try:
            # Send GET request to the API
            response = requests.get(url, timeout=5)
            response.raise_for_status() # Raise an exception if the request was unsuccessful
            data = response.json()
            if isinstance(data, list):
                # Retrieve definition details
                logger.info("Successfully able to connect to the dictionary API.")
                if 'shortdef' in data[0]:
                    pronunciation = data[0]['hwi']['prs'][0]['mw']
                    attr = data[0]['fl']
                    short_def = data[0]['shortdef'][0]
                    logger.info(f"Defination of {word} : {pronunciation} ({attr}): {short_def}")
                else:
                    logger.info("Sorry, No definition found.")
        except requests.exceptions.RequestException as e:
            logger.error(f"An error occurred while connecting to the dictionary API - {e}")

def main():
    # Command line parser checks and usage information
    parser = argparse.ArgumentParser(description="Query the Merriam-Webster dictionary and get pronunciation and short definition.")
    parser.add_argument("word", help="The word to look up in the dictionary.")
    parser.add_argument("api_key", help="Your Merriam-Webster API key.")
    args = parser.parse_args()

    dictionary = DictionaryTool(args.api_key)
    dictionary.lookup_word(args.word)

if __name__ == "__main__":
    main()
