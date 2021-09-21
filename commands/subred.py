import requests, json, os, random

#Work In Progress
def reddit():
    ured = '<Insert UserName>'
    pred = '<Insert Password>'
    idred = '<Insert App ID>'
    secred = '<Insert Secret>'
    base_urlred = 'https://www.reddit.com/'
    datared = {'grant_type': 'password', 'username': ured, 'password': pred}
    authred = requests.auth.HTTPBasicAuth(idred, secred)
    rred= requests.post(base_urlred + 'api/v1/access_token',
                    data=datared,
                    headers={'user-agent': 'Insert User Agent'},
            auth=authred)

    resred = json.loads(rred.content)
    tokenred = (resred['access_token'])
    nurlred = 'https://oauth.reddit.com/random.json'
    h1red = {'user-agent': '<insert user agent>', 'Authorization': f'bearer {tokenred}' }
    r1red = requests.get(nurlred, headers=h1red)
    jresred = json.loads(r1red.content)
    outred = (jresred[0]['data']['children'][0]['data']['permalink'])
    rurl = (f'https://reddit.com{outred}')
    return rurl

 #Work in Progress
def twit():
    twurl_id = 'https://id.twitch.tv/oauth2/token?client_id=<Insert Client ID>&client_secret=<Insert Client Secret>&grant_type=client_credentials'
    twreq_id = requests.post(twurl_id)

    twreq = json.loads(twreq_id.content)
    twtoken = (twreq['access_token'])
    game_id = ['509658', '116747788', '509659', '509667', '509671', '499634', '509670', '515214', '509669', '509660', '518203', '26936', '509663' ,'509660', '509673']
    get_id = random.choice(game_id)
    twurl = f'https://api.twitch.tv/helix/streams?first=100&game_id={get_id}'
    twc = {'Client-Id': '<Insert Client ID>', 'Authorization': f'Bearer {twtoken}'}
    twstr = requests.get(twurl, headers=twc)
    twjson = json.loads(twstr.content)
    twlist = twjson['data']
    twresult = []
    for f in twlist:
        twresult.append(f['user_login'])

    thot =  random.choice(twresult)
    fin = (f'https://twitch.tv/{thot}')
    return fin
