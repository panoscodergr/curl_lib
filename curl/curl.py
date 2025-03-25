import http.client
import json
import urllib.parse
from .utils import parse_url
from .cookies import Cookies

class Curl:
    def __init__(self, url):
        self.url = url
        self.connection = None
        self.headers = {}
        self.data = None
        self.cookies = Cookies()

    def _connect(self):
        """Σύνδεση με τον server (HTTPS υποστήριξη)"""
        parsed_url = parse_url(self.url)
        if parsed_url["scheme"] == "https":
            self.connection = http.client.HTTPSConnection(parsed_url["host"])
        else:
            self.connection = http.client.HTTPConnection(parsed_url["host"])

    def set_headers(self, headers):
        """Ορισμός επικεφαλίδων"""
        self.headers = headers

    def set_data(self, data):
        """Ορισμός δεδομένων για POST/PUT"""
        self.data = json.dumps(data)

    def _handle_response(self, response):
        """Εξαίρεση σε περίπτωση σφαλμάτων"""
        if 400 <= response.status < 500:
            raise Exception(f"Client Error: {response.status} - {response.reason}")
        elif 500 <= response.status < 600:
            raise Exception(f"Server Error: {response.status} - {response.reason}")
        return response.read().decode()

    def get(self):
        """Αίτημα GET"""
        self._connect()
        parsed_url = parse_url(self.url)
        self.connection.request("GET", parsed_url["path"], headers=self.headers)
        response = self.connection.getresponse()
        # Διαχείριση cookies
        self.cookies.update(response)
        return self._handle_response(response)

    def post(self):
        """Αίτημα POST"""
        self._connect()
        parsed_url = parse_url(self.url)
        self.connection.request("POST", parsed_url["path"], body=self.data, headers=self.headers)
        response = self.connection.getresponse()
        # Διαχείριση cookies
        self.cookies.update(response)
        return self._handle_response(response)

    def put(self):
        """Αίτημα PUT"""
        self._connect()
        parsed_url = parse_url(self.url)
        self.connection.request("PUT", parsed_url["path"], body=self.data, headers=self.headers)
        response = self.connection.getresponse()
        # Διαχείριση cookies
        self.cookies.update(response)
        return self._handle_response(response)
