from flask import Flask, render_template, request
import requests

count=0
ListofGiffs = []
apiKey = 'acc_2e84de7b64f0e9a'
apiSecret = '06e63891e5927c5c6eaf4745847c982b'
url = 'https://api.imagga.com/v2/uploads'

app = Flask(__name__)


@app.route('/')
def upload():
    return render_template('UploadImg.html')


@app.route('/result', methods=['GET','POST'])
def gif():
    load = request.files['FileToLoad']
    load.save(load.filename)
    
    
    
    upload = requests.post(url  = url ,auth=(apiKey,apiSecret),
                           files={'image': open(pic.filename, 'rb')})
    response = upload.json()['result']['upload_id']
#

    response = requests.get('https://api.imagga.com/v2/tags',
                            auth=(apiKey, apiSecret),params={'image_upload_id': upload})
    response = response.json()
    final = response['result']['tags'][0]['tag']['en']

    final = requests.get('http://api.giphy.com/v1/gifs/search',
                         params={'q': result, 'api_key': 'WFwH1cxKZ2TVN3pGn5uMPNrmbr0W3i7X'}).json()['data']
    

    while count<=10:
        gifs = final[count]['images']['fixed_height']['url']
        ListofGiffs.append(gifs)
        count=count+1

        
    return render_template('ordergifs.html', resp=ListofGiffs)

    


