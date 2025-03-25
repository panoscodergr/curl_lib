class Cookies:
    def __init__(self):
        self.cookies = {}

    def update(self, response):
        """Ανανεώνει τα cookies με αυτά από την απόκριση"""
        cookie_header = response.getheader('Set-Cookie')
        if cookie_header:
            for cookie in cookie_header.split(';'):
                key, value = cookie.split('=', 1)
                self.cookies[key.strip()] = value.strip()

    def get(self):
        """Επιστρέφει τα cookies για το αίτημα"""
        return self.cookies
