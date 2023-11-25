import time
from flask import Flask, request, render_template
from GenerateRandomIPS import randomIP
from CheckIfWebsiteUp import CheckIP, CheckIPsecure , run_start_with_threads, run_start_with_threads_secure

app = Flask(__name__)
@app.route('/', methods=['GET'])
def index2():
    return render_template('index.html')
@app.route('/', methods=['POST'])
def index():
    if 'Random HTTPS' in request.form:
        NotFinish = 1  
        iptest = 0
        result = ''
        IPs = []
        with open('PUBLICIPFOUND.txt','w') as file:
            file.write('')

        while(NotFinish == 1):
            for i in range(40):
                IPs.append(randomIP())
            check = run_start_with_threads_secure(IPs)
            with open('PUBLICIPFOUND.txt','r') as file:
                result = file.readline()
                if len(result) == 0:
                    do = 'nothing'
                else:
                    NotFinish = 0
                    return render_template('index.html',ip_value_HTTPS=result)
        return render_template('index.html')
    
    if 'Random HTTP' in request.form:
        NotFinish = 1  
        iptest = 0
        result = ''
        IPs = []
        with open('PUBLICIPFOUND.txt','w') as file:
            file.write('')

        while(NotFinish == 1):
            for i in range(40):
                IPs.append(randomIP())
            check = run_start_with_threads(IPs)
            with open('PUBLICIPFOUND.txt','r') as file:
                result = file.readline()
                if len(result) == 0:
                    do = 'nothing'
                else:
                    NotFinish = 0
                    return render_template('index.html',ip_value_HTTP=result)
        return render_template('index.html')  


if __name__ == '__main__':
    app.run("127.0.0.1", debug=True,port=4444)
    