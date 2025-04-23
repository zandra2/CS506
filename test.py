import requests

try:
    res = requests.get('http://web.textfiles.com/computers/3dbasics.txt')
    # res = requests.get('http://web.textfiles.com/')
    print(res.raise_for_status())

except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')

except Exceptions as exc:
    print(f'Exce: {exc}')