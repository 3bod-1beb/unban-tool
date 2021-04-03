import threading
import requests
abood = requests.session()
fullname = input('Full name :')
usr = input('Username :')
eml = input('Email :')
phone = input('Phone number :')
thhred = int(input('Thread :'))
import random
ul ='https://help.instagram.com/ajax/help/contact/submit/page'
prox = open('proxies.txt', 'r').read().splitlines()
data_uae = {
                "jazoest": 2934,
                "lsd": "AVpKi-QPgmI",
                'AccountType': 'Personal',
                'name': fullname,
                'Field1489970557888767': usr,
                'email': eml,
                'Field236858559849125_iso2_country_code': '',
                'Field236858559849125': 'United Arab Emirates',
                "support_form_id": 1652567838289083,
                "support_form_hidden_fields": '{"904224879693114":false,"495070633933955":false,"1489970557888767":false,"488955464552044":false,"236858559849125":false,"1638971086372158":true,"1615324488732156":true,"236548136468765":true}',
                "support_form_fact_false_fields": "[]",
                "__user": 0,
                "__a": 1,
                "__dyn": "7xe6Fo4OQ1PyWwHBWo5O12wAxu13wqovzEy58ogbUuw9-3K4o1j8hwem0nCq1ewcG0KEswaq1xwEw7BKdwnU1e42C220qu1TwoU2swdq0Ho2ew",
                "__csr": "",
                "__req": 8,
                "__beoa": 0,
                "__pc": "PHASED:DEFAULT",
                "__bhv": 2,
                "dpr": 1,
                "__ccg": "GOOD",
                "__rev": 1003553210,
                "__s": "1p5i82:v1452w:6dkngr",
                "__hsi": "6946150823796336233-0",
                "__comet_req": 0,
                "__spin_r": 1003553210,
                "__spin_b": "trunk",
                "__spin_t": 1617276766
}
data_iq = {
                "jazoest": 2934,
                "lsd": "AVpKi-QPgmI",
                'AccountType': 'Personal',
                'name': fullname,
                'Field1489970557888767': usr,
                'email': eml,
                'Field236858559849125_iso2_country_code': '',
                'Field236858559849125': 'Iraq',
                "support_form_id": 1652567838289083,
                "support_form_hidden_fields": '{"904224879693114":false,"495070633933955":false,"1489970557888767":false,"488955464552044":false,"236858559849125":false,"1638971086372158":true,"1615324488732156":true,"236548136468765":true}',
                "support_form_fact_false_fields": "[]",
                "__user": 0,
                "__a": 1,
                "__dyn": "7xe6Fo4OQ1PyWwHBWo5O12wAxu13wqovzEy58ogbUuw9-3K4o1j8hwem0nCq1ewcG0KEswaq1xwEw7BKdwnU1e42C220qu1TwoU2swdq0Ho2ew",
                "__csr": "",
                "__req": 8,
                "__beoa": 0,
                "__pc": "PHASED:DEFAULT",
                "__bhv": 2,
                "dpr": 1,
                "__ccg": "GOOD",
                "__rev": 1003553210,
                "__s": "1p5i82:v1452w:6dkngr",
                "__hsi": "6946150823796336233-0",
                "__comet_req": 0,
                "__spin_r": 1003553210,
                "__spin_b": "trunk",
                "__spin_t": 1617276766
}
dat_usa = {
                "jazoest": 2934,
                "lsd": "AVpKi-QPgmI",
                'AccountType': 'Personal',
                'name': fullname,
                'Field1489970557888767': usr,
                'email': eml,
                'Field236858559849125_iso2_country_code': '',
                'Field236858559849125': 'United States',
                "support_form_id": 1652567838289083,
                "support_form_hidden_fields": '{"904224879693114":false,"495070633933955":false,"1489970557888767":false,"488955464552044":false,"236858559849125":false,"1638971086372158":true,"1615324488732156":true,"236548136468765":true}',
                "support_form_fact_false_fields": "[]",
                "__user": 0,
                "__a": 1,
                "__dyn": "7xe6Fo4OQ1PyWwHBWo5O12wAxu13wqovzEy58ogbUuw9-3K4o1j8hwem0nCq1ewcG0KEswaq1xwEw7BKdwnU1e42C220qu1TwoU2swdq0Ho2ew",
                "__csr": "",
                "__req": 8,
                "__beoa": 0,
                "__pc": "PHASED:DEFAULT",
                "__bhv": 2,
                "dpr": 1,
                "__ccg": "GOOD",
                "__rev": 1003553210,
                "__s": "1p5i82:v1452w:6dkngr",
                "__hsi": "6946150823796336233-0",
                "__comet_req": 0,
                "__spin_r": 1003553210,
                "__spin_b": "trunk",
                "__spin_t": 1617276766
}
dat_uk = {
                "jazoest": 2934,
                "lsd": "AVpKi-QPgmI",
                'AccountType': 'Personal',
                'name': fullname,
                'Field1489970557888767': usr,
                'email': eml,
                'Field236858559849125_iso2_country_code': '',
                'Field236858559849125': 'United Kingdom',
                "support_form_id": 1652567838289083,
                "support_form_hidden_fields": '{"904224879693114":false,"495070633933955":false,"1489970557888767":false,"488955464552044":false,"236858559849125":false,"1638971086372158":true,"1615324488732156":true,"236548136468765":true}',
                "support_form_fact_false_fields": "[]",
                "__user": 0,
                "__a": 1,
                "__dyn": "7xe6Fo4OQ1PyWwHBWo5O12wAxu13wqovzEy58ogbUuw9-3K4o1j8hwem0nCq1ewcG0KEswaq1xwEw7BKdwnU1e42C220qu1TwoU2swdq0Ho2ew",
                "__csr": "",
                "__req": 8,
                "__beoa": 0,
                "__pc": "PHASED:DEFAULT",
                "__bhv": 2,
                "dpr": 1,
                "__ccg": "GOOD",
                "__rev": 1003553210,
                "__s": "1p5i82:v1452w:6dkngr",
                "__hsi": "6946150823796336233-0",
                "__comet_req": 0,
                "__spin_r": 1003553210,
                "__spin_b": "trunk",
                "__spin_t": 1617276766
}
dat_fr = {
                "jazoest": 2934,
                "lsd": "AVpKi-QPgmI",
                'AccountType': 'Personal',
                'name': fullname,
                'Field1489970557888767': usr,
                'email': eml,
                'Field236858559849125_iso2_country_code': '',
                'Field236858559849125': 'France',
                "support_form_id": 1652567838289083,
                "support_form_hidden_fields": '{"904224879693114":false,"495070633933955":false,"1489970557888767":false,"488955464552044":false,"236858559849125":false,"1638971086372158":true,"1615324488732156":true,"236548136468765":true}',
                "support_form_fact_false_fields": "[]",
                "__user": 0,
                "__a": 1,
                "__dyn": "7xe6Fo4OQ1PyWwHBWo5O12wAxu13wqovzEy58ogbUuw9-3K4o1j8hwem0nCq1ewcG0KEswaq1xwEw7BKdwnU1e42C220qu1TwoU2swdq0Ho2ew",
                "__csr": "",
                "__req": 8,
                "__beoa": 0,
                "__pc": "PHASED:DEFAULT",
                "__bhv": 2,
                "dpr": 1,
                "__ccg": "GOOD",
                "__rev": 1003553210,
                "__s": "1p5i82:v1452w:6dkngr",
                "__hsi": "6946150823796336233-0",
                "__comet_req": 0,
                "__spin_r": 1003553210,
                "__spin_b": "trunk",
                "__spin_t": 1617276766
}
hdgg = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '890',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'ig_did=28615C70-EFAC-457D-A24C-352A83D1F057; mid=YBPMXwALAAH4dviOdXdTwThW-ifm; ig_nrcb=1; csrftoken=TlQJVO3GFRrdCtydedVinnbyWnuvlgno; ds_user_id=45741299458; sessionid=45741299458%3AacSX0w8CeFcNNF%3A12; datr=I6NkYMRBzw-VwCEI8eRD-yEk',
        'origin': 'https://help.instagram.com',
        'referer': 'https://help.instagram.com/contact/1652567838289083?helpref=page_content',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1',
        'x-fb-lsd': 'AVpKi-QPgmI'
}
head2 = {
                "Host": "help.instagram.com",
                "Accept": "*/*",
                "X-FB-LSD": "AVr_Dx9PS9A",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-us",
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": "https://help.instagram.com",
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
                "Connection": "keep-alive",
                "Referer": "https://help.instagram.com/contact/606967319425038?helpref=page_content",
            }
data_spam = {
                "jazoest": 2890,
                "lsd": "AVr_Dx9PS9A",
                "name": fullname,
                "instagram_username": usr,
                "email": eml,
                "mobile_number": phone,
                "appeal_reason": 'Dear instagram,My account was disabled for violating your terms even thought my account is a normal account for jokes...Please restore my account because it doesn’t contain any Credible threats to harm others or the promotion of self-destructive behaviorAnd it does not Targeting individualsAlso it does not contain Hate speech or singling people out based on race, ethnicity, national origin, religion, sex, gender, sexual orientation, disability or diseaseEventhough there is no Graphic content including sadistic displays of violence against people or animals and depictions of sexual assault..I hope you will take my request into full consideration.Thank you.',
                "support_form_id": 606967319425038,
                "support_form_hidden_fields": "{}",
                "support_form_fact_false_fields": "[]",
                "__user": 0,
                "__a": 1,
                "__dyn": "7xe6Fo4OQ1PyWwHBWo5O12wAxu13wqovzEy58ogbUuw9-3K4o1j8hwem0nCq1ewcG0KEswaq1xwEw7BKdwnU1e42C220qu1TwoU2swdq0Ho2ew",
                "__csr": "",
                "__req": "h",
                "__beoa": 0,
                "__pc": "PHASED:DEFAULT",
                "__bhv": 2,
                "dpr": 3,
                "__ccg": "EXCELLENT",
                "__rev": 1003521343,
                "__s": "8x0mgw:dal0sr:s5g412",
                "__hsi": "6943937313156005653-0",
                "__comet_req": 0,
                "__spin_r": 1003521343,
                "__spin_b": "trunk",
                "__spin_t": 1616761394
            }
def send():
    spam = 1
    req_spam = 1
    while True:
        try:
            proxing = []
            for i in prox:
                proxing.append(i)
            proxy1 = str(random.choice(proxing))
            pro2 = {
                'http': f'{proxy1}', 'https': f'{proxy1}'
            }
            abood.proxies = pro2
            req_uae = abood.post(ul ,headers=hdgg ,data=data_uae)
            if '"#FieldErrorSection763233237023765"' in req_uae.text:
                print('request done >> [uae]')
            elif '"Slow down to keep using this feature"' in req_uae.text:
                spam += 1
                bb = str(spam)
                print(f'spam >> [{bb}]')
            req_iq = abood.post(ul ,headers=hdgg ,data=data_iq)
            if '"#FieldErrorSection763233237023765"' in req_iq.text:
                print('request done >> [iq]')
            elif '"Slow down to keep using this feature"' in req_iq.text:
                spam += 1
                bb = str(spam)
                print(f'spam >> [{bb}]')
            req_usa = abood.post(ul ,headers=hdgg ,data=dat_usa)
            if '"#FieldErrorSection763233237023765"' in req_usa.text:
                print('request done >> [usa]')
            elif '"Slow down to keep using this feature"' in req_usa.text:
                spam += 1
                bb = str(spam)
                print(f'spam >> [{bb}]')
            req_uk = abood.post(ul ,headers=hdgg ,data=dat_uk)
            if '"#FieldErrorSection763233237023765"' in req_uk.text:
                print('request done >> [Uk]')
            elif '"Slow down to keep using this feature"' in req_uk.text:
                spam += 1
                bb = str(spam)
                print(f'spam >> [{bb}]')
            req_fr = abood.post(ul ,headers=hdgg ,data=dat_fr)
            if '"#FieldErrorSection763233237023765"' in req_fr.text:
                print('request done >> [France]')
            elif '"Slow down to keep using this feature"' in req_fr.text:
                spam += 1
                bb = str(spam)
                print(f'spam >> [{bb}]')
            req_spam2 = abood.post(ul ,headers=head2 ,data=data_spam)
            if ">Form submitted successfully" in req_spam2.text:
                req_spam += 1
                bb2 = str(req_spam)
                print(f'request done url spam >> [{bb2}]')
            elif "You may want to slow down or stop to avoid a restriction on your account" in req_spam2.text:
                spam += 1
                print(f'spam >> [{spam}]')
        except requests.exceptions.ConnectionError:
            print('proxy error')

            pass
threads = []
for i in range(thhred):
    th = threading.Thread(target=send)
    th.start()
    threads.append(th)
for thread2 in threads:
    thread2.join()
