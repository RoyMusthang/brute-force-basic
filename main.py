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
                except Exception as error:
                    print(error)
                    pass

    if __name__ == "__main__":
        url = sys.argv[1]
        wordlist = sys.argv[2]

        with open(wordlist, "r") as file:
            wordlist = file.readlines()
            brute(url, wordlist)
