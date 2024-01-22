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
import pprint
from datetime import datetime

try:
    token = get_token(env)
    date = datetime.now().strftime("%Y%m%d-%HH%MM%SS")

    with open(env['log_path'] + 'DeviceList'+ "-" + str(date) + ".txt", "w+") as outFile:
        outFile.writelines('< Device List >\n')
        print('< Device List >')

        devicelist = get_device_list(env, token)
        for device in devicelist:
            print('Device name : {}, Device id : {}'.format(device['hostname'], device['id']))
            outFile.writelines('Device name : {}, Device id : {}\n'.format(device['hostname'], device['id']))
except Exception as e:
    print(e)