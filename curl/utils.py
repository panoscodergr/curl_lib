import urllib.parse

def parse_url(url):
    """Αναλύει τη URL και επιστρέφει τα στοιχεία της (υποστήριξη για query parameters)"""
    parsed_url = urllib.parse.urlparse(url)
    query_params = urllib.parse.parse_qs(parsed_url.query)
    return {
        "scheme": parsed_url.scheme,
        "host": parsed_url.netloc,
        "path": parsed_url.path if parsed_url.path else "/",
        "query_params": query_params
    }
