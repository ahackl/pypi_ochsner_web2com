import requests
import xmltodict

class Web2com:
     
    def __init__(
        self,
        ip_number: str,
        user_name: str,
        password: str,
        **kwargs,
    ):
        assert ip_number, "IP number must be defined"
        assert user_name, "User name must be defined"
        assert password, "Password must be defined"
        
        self.ip_number = ip_number
        self.user_name = user_name
        self.password = password


    def get_value(self, command_id_sequence):
        url = "http://" + self.ip_number + "/ws"

        payload = '<?xml version="1.0" encoding="UTF-8"?>' + '\n'
        payload += '<SOAP-ENV:Envelope' + '\n'
        payload += 'xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"' + '\n'
        payload += 'xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"' + '\n'
        payload += 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"' + '\n'
        payload += 'xmlns:xsd="http://www.w3.org/2001/XMLSchema"' + '\n'
        payload += 'xmlns:ns="http://ws01.lom.ch/soap/">' + '\n'
        payload += '<SOAP-ENV:Body>' + '\n'
        payload += '<ns:getDpRequest>' + '\n'
        payload += '<ref>' + '\n'
        payload += '<oid>' + command_id_sequence + '</oid>' + '\n'
        payload += '<prop/>' + '\n'
        payload += '</ref>' + '\n'
        payload += '<startIndex>0</startIndex>' + '\n'
        payload += '<count>20</count>' + '\n'
        payload += '</ns:getDpRequest>' + '\n'
        payload += '</SOAP-ENV:Body>' + '\n'
        payload += '</SOAP-ENV:Envelope>' + '\n'

        try:
            session = requests.Session()
            result = session.post(url,  
                                data = payload, 
                                auth = requests.auth.HTTPDigestAuth(self.user_name, self.password))
            value = 0.0
            if result.status_code == 200:
                python_dict = xmltodict.parse(result.content)
                value = float(python_dict['SOAP-ENV:Envelope']['SOAP-ENV:Body']['ns:getDpResponse']['dpCfg']['value'])
            return result.status_code, value
        except:
            return 0, 0.0
        
    def set_value(self, command_id_sequence, command_value):
        url = "http://" + self.ip_number + "/ws"

        payload = '<?xml version="1.0" encoding="UTF-8"?>' + '\n'
        payload += '<SOAP-ENV:Envelope' + '\n'
        payload += 'xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"' + '\n'
        payload += 'xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"' + '\n'
        payload += 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"' + '\n'
        payload += 'xmlns:xsd="http://www.w3.org/2001/XMLSchema"' + '\n'
        payload += 'xmlns:ns="http://ws01.lom.ch/soap/">' + '\n'
        payload += '<SOAP-ENV:Body>' + '\n'
        payload += '<ns:writeDpRequest>' + '\n';
        payload += '<ref>' + '\n';
        payload += '<oid>' + command_id_sequence + '</oid>' + '\n';
        payload += '<prop/>' + '\n';
        payload += '</ref>' + '\n';
        payload += '<dp>' + '\n';
        payload += '<index>' + command_id_sequence[-1] +'</index>' + '\n';
        payload += '<name/>' + '\n';
        payload += '<prop/>' + '\n';
        payload += '<desc/>' + '\n';
        payload += '<value>' + str(command_value) + '</value>' + '\n';
        payload += '<unit/>' + '\n';
        payload += '<timestamp>0</timestamp>' + '\n';
        payload += '</dp>' + '\n';
        payload += '</ns:writeDpRequest>' + '\n';
        payload += '</SOAP-ENV:Body>' + '\n';
        payload += '</SOAP-ENV:Envelope>' + '\n';

        try:
            session = requests.Session()
            result = session.post(url,  
                                data = payload, 
                                auth = requests.auth.HTTPDigestAuth(self.user_name, self.password))
            value = 0.0
            if result.status_code == 200:
                value = float(command_value)
            return result.status_code, value
        except:
            return 0, 0.0
    


if __name__ == '__main__':
    web2com = Web2com('192.168.188.50', 'OEM', 'password')

    result = web2com.get_value('/1/2/1/125/9')
    print(result)

    result = web2com.set_value('/1/2/4/99/6', 20.0)
    print(result)