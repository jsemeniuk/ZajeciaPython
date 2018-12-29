import urllib.request
import datetime

try:
    with urllib.request.urlopen("https://www.actris.pl") as stream:
        print(stream.read())

except urllib.request.HTTPError as err:
    print("Błąd Http")

except urllib.request.ContentTooShortError:
    print("Odpowedź serwera jest za krótka")

except Exception as err:
    with open('error.log', 'a') as fh:
        fh.write('{0}: {1}\n'.format(datetime.datetime.now(), str(err)))

finally:
    stream.close()
