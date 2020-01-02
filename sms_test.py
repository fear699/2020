import requests


def send_sms(mobile, vcode):
    api = 'https://open.ucpaas.com/ol/sms/sendsms'
    args = {
        "sid": '2ff56f07e2d002ab9900777dd4b09edf',
        "token": 'd763718424035afc347cbd3bba3813a2',
        "appid": '8235102f41ed4603802b05264c59430e',
        "templateid": '503617',
        "param": vcode,
        "mobile": mobile
    }

    response = requests.post(api, json=args)
    return response
