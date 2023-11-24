from htmlextract import extractTxtFromHtml
from gpt_webtxtanalyst import GptWebsiteAnalyser
import requests
import time

with open("upip.txt","r") as f:
    IPs = [line.strip() for line in f]



tooshort = 0
for ip in IPs:
    try:
        print('sending request...')
        url = 'http://'+ ip +'/'
        print(ip)
        r = requests.get(url,allow_redirects=True)


        redirect = r.url
        if(redirect != url):
            print('redirect detected : ' + redirect)
            newurl = r.url
            r = requests.get(newurl)


        data = r.text
        print(len(data))
        if len(data) < 500:
            tooshort = 1
        if len(data) > 30000:
            data = data[:30000]
        


        if tooshort != 1:
            dataExtracted = extractTxtFromHtml(data)
            print('data extracted')
            response = GptWebsiteAnalyser(dataExtracted)
            print('Got response from GPT')
            if len(response) > 0:
                print(' : ' +response)
                with open('labeled_wensites.txt','a') as p:
                    p.write(ip + ' : ' + response + '\n')
            else:
                print('gpt had enough')
        else:
            tooshort = 0
            print('it was too short')
    except Exception as e:
        print(f"Error: {e}")
    
    
