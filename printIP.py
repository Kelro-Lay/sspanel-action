import requests
##requests.packages.urllib3.disable_warnings()

#print('printIP')
resp = requests.get('http://ifconfig.me')
print(f'This IP is {resp.text}')
#print('end')