# ochsner_web2com

`ochsner_web2com` is a Python module that read or write paramters of a web2com interface from ochser heat pump via SOAP requests.

Example

```python
    import ochsner_web2com.web2com as web2com
    
    ## Connect to a web2com server with default eBus and device id.
    ## Use Digest access authentication as default
    w2c = web2com.Service('192.168.188.50', 'OEM', 'password')

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
    result = w2c.get(web2com.HEAT_PUMP.Thermal_energy_kWh)
    print(result)
    ## set value via predefined enum
    result = w2c.set(web2com.HEATING_CIRCUIT.Normal_setpoint_room_temperature_heating, 20.0)
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
```
The first parameter of the result holds the HTTP result code
and the second paramter the value of the paramter.

Paramter List:

| Description | ID chain |
| --------------- | --------------- |
| heat pump: State heat generator control | /1/2/1/125/0 | 
| heat pump: Flow temperature heat generator | /1/2/1/125/1 |
| heat pump: Return flow temperature heat generator | /1/2/1/125/2 |
| heat pump: Heat source outlet temperature | /1/2/1/125/3 |
| heat pump: Heat source inlet temperature | /1/2/1/125/4 |
| heat pump: Operation cycles | /1/2/1/125/5 |
| heat pump: Operation hours | /1/2/1/125/6 |
| heat pump: Volume flow heat energy | /1/2/1/125/7 |
| heat pump: Flow rate heat source | /1/2/1/125/8 |
| heat pump: Thermal energy kWh | /1/2/1/125/9 |
| heat pump: Thermal energy MWh | /1/2/1/125/10 |
| heat pump: Energy DHW kWh | /1/2/1/125/11 |
| heat pump: Energy DHW MWh | /1/2/1/125/12 |
| auxiliary: State heat generator control | /1/2/2/126/0 |
| auxiliary: Flow temperature heat generator | /1/2/2/126/1 |
| auxiliary: Operation cycles | /1/2/2/126/2 |
| auxiliary: Operation hours | /1/2/2/126/3 |
| auxiliary: Thermal energy kWh | /1/2/2/126/4 |
| auxiliary: Thermal energy MWh | /1/2/2/126/5 |
| heating circuit: State heating circuit control | /1/2/4/119/0 |
| heating circuit: Outdoor temperature | /1/2/4/119/1 |
| heating circuit: Outdoor temperature average value | /1/2/4/119/2 |
| heating circuit: Setpoint room temperature | /1/2/4/119/3 |
| heating circuit: Actual heating circuit flow temperature | /1/2/4/119/4 |
| heating circuit: Setpoint heating circuit flow temperature | /1/2/4/119/5 |
| DHW: State DHW control | /1/2/7/121/0 |
| DHW: Actual DHW temperature | /1/2/7/121/1 |
| DHW: DHW setpoint | /1/2/7/121/2 |
| Manager: Storage tank temperature top | /1/2/8/122/0 |
| Manager: Storage tank temperature center | /1/2/8/122/1 |
| Manager: Plant flow temperature | /1/2/8/122/2 |
| Manager: Plant CH setpoint flow temperature | /1/2/8/122/3 |
| Manager: Heating power in heating mode | /1/2/8/122/4 |
| Manager: Heating power in DHW mode | /1/2/8/122/5 |
| Manager: State heating manager | /1/2/8/122/6 |


Default paramter:

| Description | ID |
| ----------- | -- |
| eBus | 1 | 
| device | 2 |




