# ochsner_web2com

`ochsner_web2com` is a Python module that read or write paramters of a web2com interface from ochser heat pump via SOAP requests.

Example

```python
    import ochsner_web2com.web2com as w2c

    web2com = w2c.Service('192.168.188.50', 'OEM', 'password')

    result = web2com.get_value('/1/2/1/125/9')
    print(result)

    result = web2com.set_value('/1/2/4/99/6', 20.0)
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




