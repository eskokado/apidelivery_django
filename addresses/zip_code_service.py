import requests
from functools import lru_cache


class ZipCodeService:
    def __init__(self, base_url):
        self.base_url = base_url

    @lru_cache(maxsize=128)
    def get_zip_code_address(self, zip_code):
        url = f"{self.base_url}/{zip_code}/json/"
        response = requests.get(url)

        if response.status_code == 200:
            zip_code_address = response.json()
            return zip_code_address
        else:
            return None
