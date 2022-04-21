import sys
import requests

    def brute(url, wordlist):
        for word in wordlist:
            try:
                url_end = "{}/{}".format(url, word.strip())
                response = requests.get(url_end)
                code = response.status_code
                if code != 404:
                    print("{} -- {}".format(url_end, code))
                except KeyboardInterrupt:
                    sys.exit(0)
                except 
