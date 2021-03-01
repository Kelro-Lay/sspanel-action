import requests
requests.packages.urllib3.disable_warnings()

base_url = ''
email = ''
password = ''

if base_url == '' :
    base_url = input('host:')
if base_url == '' :
    raise AssertionError("ERROR: Need config host")
host = base_url
response = 0

def checkin():
    global response,email,password
    if email=='' :
        email = input('email: ')
    if password=='' :
        password = input('password: ')

    email = email.split('@')
    print(f"登陆 {host[0:11]}....{host[-5:]}   email:{email[0][0:2]}...@...{email[1][-4:]}" )
    email = email[0] + '%40' + email[1]

    session = requests.session()
    
    resp = session.get(base_url, verify=False)
    if resp.status_code != 200 :
        raise AssertionError(f"ERROR: {base_url} : {resp.status_code}")
    
    login_url = base_url + '/auth/login'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    post_data = 'email=' + email + '&passwd=' + password + '&code='
    post_data = post_data.encode()
    response = session.post(login_url, post_data, headers=headers, verify=False)

    if response.text[0]!='{' :
        raise AssertionError('登陆失败：\n' + response.text)
    resp = response.json()
    if resp['ret']==0 :
        raise AssertionError('登陆失败：' + resp['msg'])
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Referer': base_url + '/user'
    }

    response = session.post(base_url + '/user/checkin', headers=headers, verify=False)
    if response.status_code != 200 :
        raise AssertionError('签到失败：\n' + response.text)
    resp = response.json()
    print(resp['msg'])


try:
    checkin()
except AssertionError as e:
    print(e.args[0])
