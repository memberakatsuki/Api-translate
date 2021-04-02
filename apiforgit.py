import json
import requests
import base64

class Traslate:
    def __init__(self):
        self.url = 'https://api.gotit.ai/Translation/v1.1/Translate'


        self.userAndPass = base64.b64encode(b"Key Identifier:Key Secret").decode("ascii")
        
        self.headers = {
            'Content-type': 'application/json', 
            'Authorization': f"Basic {self.userAndPass}"
        }

    def translate(self,text,opc):
        if opc == 1:
            self.sl = 'PtBr'
            self.lin = 'EnUs'
        else:
            self.sl = 'EnUs'
            self.lin = 'PtBr'

        self.payload = json.dumps({
            "T":f"{text}.",
            "SL":f"{self.sl}",
            "TL":f"{self.lin}"
        })

        self.response = requests.post(self.url, data=self.payload, headers=self.headers)
        self._ = self.response.json()['result']

        return self._
        
    
if __name__ == '__main__':
    print('\033[31mDigite o que você deseja Traduzir:\033[31m'.center(80))
    text = input('\033[32m')
    print('\033[0;0m\033[31mTraduzir para - [1 - Inglês ou 2 - Português]:\033[31m'.center(98))
    opc = int(input('\033[32m'))
    app = Traslate()
    result = app.translate(text,opc)
    print('\033[0;0m\033[31mTradução:\033[31m'.center(80))
    print(f'\033[32m{result}\033[0;0m\n')
