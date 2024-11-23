import requests
import xmltodict
from enum import Enum

class HEAT_PUMP(Enum):
    State_heat_generator_control = [1, 125, 0]
    Flow_temperature_heat_generator = [1, 125, 1]
    Return_flow_temperature_heat_generator = [1, 125, 2]
    Heat_source_outlet_temperature = [1, 125, 3]
    Heat_source_inlet_temperature = [1, 125, 4]
    Operation_cycles = [1, 125, 5]
    Operation_hours = [1, 125, 6]
    Volume_flow_heat_energy = [1, 125, 7]
    Flow_rate_heat_source = [1, 125, 8]
    Thermal_energy_kWh = [1, 125, 9]
    Thermal_energy_MWh = [1, 125, 10]
    Energy_DHW_kWh = [1, 125, 11]
    Energy_DHW_MWh = [1, 125, 12]

class AUXILIARY(Enum):
    State_heat_generator_control = [2, 126, 0]
    Flow_temperature_heat_generator = [2, 126, 1]
    Operation_cycles = [2, 126, 2]
    Operation_hours = [2, 126, 3]
    Thermal_energy_kWh = [2, 126, 4]
    Thermal_energy_MWh = [2, 126, 5]

class HEATING_CIRCUIT(Enum):
    State_heating_circuit_control = [4, 119, 0]
    Outdoor_temperature = [4, 119, 1]
    Outdoor_temperature_average_value = [4, 119, 2]
    Setpoint_room_temperature = [4, 119, 3]
    Actual_heating_circuit_flow_temperature = [4, 119, 4]
    Setpoint_heating_circuit_flow_temperature = [4, 119, 5]
    Normal_setpoint_room_temperature_heating = [4, 99, 6]

class DHW(Enum):
    State_DHW_control = [7, 121, 0]
    Actual_DHW_temperature = [7, 121, 1]
    DHW_setpoint =[7, 121, 2]

class MANAGER(Enum):
    Storage_tank_temperature_top = [8, 122, 0]
    Storage_tank_temperature_center = [8, 122, 1]
    Plant_flow_temperature = [8, 122, 2]
    Plant_CH_setpoint_flow_temperature = [8, 122, 3]
    Heating_power_in_heating_mode = [8, 122, 4]
    Heating_power_in_DHW_mode = [8, 122, 5]
    State_heating_manager = [8, 122, 6]

class AUTH(Enum):
    BASIC = 0
    DIGEST = 1

class Service:
     
    def __init__(
        self,
        ip_number: str,
        user_name: str,
        password: str,
        auth = AUTH.DIGEST,
        **kwargs,
    ):
        assert ip_number, "IP number must be defined"
        assert user_name, "User name must be defined"
        assert password, "Password must be defined"
        assert auth, "Authentication method must be defined"

        self.chain_seperator = "/"

        self.ip_number = ip_number
        self.user_name = user_name
        self.password = password
        self.auth = auth

        self.eBus_id = 1
        self.device_id = 2

    def set_eBus_id(self, eBus = 1):
        self.eBus_id = eBus
    def set_device_id(self, device = 2):
        self.device_id = device

    def get_auth_method(self):
        if self.auth == AUTH.DIGEST:
            return requests.auth.HTTPDigestAuth(self.user_name, self.password)
        else:
            return requests.auth.HTTPBasicAuth(self.user_name, self.password)

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
                                auth = self.get_auth_method())
            value = 0.0
            if result.status_code == 200:
                python_dict = xmltodict.parse(result.content)
                value = float(python_dict['SOAP-ENV:Envelope']['SOAP-ENV:Body']['ns:getDpResponse']['dpCfg']['value'])
            return (result.status_code, value)
        except:
            return (0, 0.0)
        
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
                                auth = self.get_auth_method())
            value = 0.0
            if result.status_code == 200:
                value = float(command_value)
            return (result.status_code, value)
        except:
            return (0, 0.0)

    def get_chain_id (self, enum_id_list):
        try:
            id = self.chain_seperator
            id += str(self.eBus_id)
            id += self.chain_seperator
            id += str(self.device_id)
            for enum_id in enum_id_list:
                id += self.chain_seperator + str(enum_id)
            return (id)
        except:
            return ("")
    

    def get(self, enum_id):
        try:
            if isinstance(enum_id, list):
                id = self.get_chain_id(enum_id)
            else:
                id = self.get_chain_id(enum_id.value)
            result = self.get_value(id)
            return (result)
        except:
            return (0, 0.0)
    
    def set(self, enum_id, command_value):
        try:
            if isinstance(enum_id, list):
                id = self.get_chain_id(enum_id)
            else:
                id = self.get_chain_id(enum_id.value)
            result = self.set_value(id, command_value)
            return (result)
        except:
            return (0, 0.0)


if __name__ == '__main__':
    
    ## Connect to a web2com server with default eBus and device id.
    ## Use Digest access authentication as default
    w2c = Service('192.168.188.50', 'OEM', 'password')

    ## Change the id's of ebus or device.
    w2c.set_eBus_id(1)
    w2c.set_device_id(2)

    ## get value via chain id
    result = w2c.get_value('/1/2/1/125/9')
    print(result)
    ## set value via chain id
    result = w2c.set_value('/1/2/4/99/6', 20.0)
    print(result)

    ## get value via predefined enum
    result = w2c.get(HEAT_PUMP.Thermal_energy_kWh)
    print(result)
    ## set value via predefined enum
    result = w2c.set(HEATING_CIRCUIT.Normal_setpoint_room_temperature_heating, 20.0)
    print(result)

    ## get values via list of id's (eBus and device will be added)
    result = w2c.get([1, 125, 9])
    print(result)
    ## set value via list of id's (eBus and device will be added)
    result = w2c.set([4, 99, 6], 20.0)
    print(result)

    ## Connect to a web2com server with default eBus and device id.
    ## Use Basic access authentication
    w2c_basic = Service('192.168.188.50', 'OEM', 'password', auth=AUTH.BASIC)

    ## get value via chain id
    result = w2c_basic.get_value('/1/2/1/125/9')
    print(result)
   

