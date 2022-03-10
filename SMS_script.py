
def send_SMS(flow, water_level, temperature, humidity, number):
    import requests

    


    url = "https://www.fast2sms.com/dev/bulkV2"


    

    payload = "sender_id=TXTIND&message=EMERGENCY!!! Water Level: {} cm; Flow rate: {} LPM; Temperature: {} celsius; Relative humidity: {} %; Please take control &route=v3&numbers={}".format(water_level,flow, temperature, humidity, number)
    headers = {
        'authorization': "5RmthKnDLbGfwiTBzUQN79j6MoxPZckadVlHq0IX8s132YpCWebHsB1W58jnovQ06XuDAg7fVTJ3Yctx",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

