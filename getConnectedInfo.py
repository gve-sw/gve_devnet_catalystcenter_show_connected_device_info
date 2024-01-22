"""
Copyright (c) 2023 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

__author__ = "Hyeyoung Kim <hyeyokim@cisco.com>"
__copyright__ = "Copyright (c) 2023 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


from catalyst import *
from env import *
from datetime import datetime


try:
    token = get_token(env)
    interfacelist = get_interface_list_by_deviceid(env, token, env['device_id'])
    device = get_device_details(env, token, env['device_id'])
    date = datetime.now().strftime("%Y%m%d-%HH%MM%SS")


    with open(env['log_path'] + device['hostname'] + "-" + str(date) + ".txt", "w+") as outFile:
        outFile.writelines('-------------------------------------------------------------\n')
        print('-------------------------------------------------------------')
        outFile.writelines('<Device {} information>\n\n'.format(device['hostname']))
        print('<Device {} information>\n'.format(device['hostname']))

        for key, value in device.items():
            outFile.writelines('{} : {}\n'.format(key, value))
            print('{} : {}'.format(key, value))
        print('-------------------------------------------------------------')
        outFile.writelines('-------------------------------------------------------------\n')
        print('<Interface information>\n')
        outFile.writelines('<Interface information>\n\n')

        for interface in interfacelist:
            outFile.writelines('port : {portName}, port MAC : {mac}\n'.format(portName = interface['portName'], mac=interface['macAddress']))
            print('port : {portName}, port MAC : {mac}'.format(portName = interface['portName'], mac=interface['macAddress']))
            outFile.writelines('ipv4 Address : {ipv4}, ipv4 Mask : {mask}\n'.format(ipv4=interface['ipv4Address'], mask=interface['ipv4Mask']))
            print('ipv4 Address : {ipv4}, ipv4 Mask : {mask}'.format(ipv4=interface['ipv4Address'], mask=interface['ipv4Mask']))

            connectedDevice = get_connected_device_list(env, token, env['device_id'], interface['instanceUuid'])
            outFile.writelines(str(connectedDevice) + '\n')
            print(str(connectedDevice))
            print('-------------------------------------------------------------')
            outFile.writelines('-------------------------------------------------------------\n')
except Exception as e:
    print(e)
