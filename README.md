# gve_devnet_catalystcenter_show_connected_device_info
Prototype to retrieve devices' ip address which is connected to Switch with using Catalyst api


## Contacts
* Hye young Kim


## Solution Components
* Catalyst center


## Installation/Configuration
1. Clone this repository with `git clone https://github.com/gve-sw/gve_devnet_catalystcenter_show_connected_device_info`
`
2. Add the IP address, username, and password of your Catalyst Center to the credentials file

```
env = {
    "base_url": "", #Catalyst center url
    "username": "", #Catalyst center username
    "password": "", #Catalyst center password
    "version": "",   #Catalyst center version
    "device_id" : "", #ID of network device
    "log_path" : "" #Log Path
}
```

3. Set up a Python virtual environment. Make sure Python 3 is installed in your environment, and if not, you may download Python [here](https://www.python.org/downloads/). Once Python 3 is installed in your environment, you can activate the virtual environment with the instructions found [here](https://docs.python.org/3/tutorial/venv.html).

4. Install the requirements with pip3 install -r requirements.txt


## Usage
To run the code, use the command:
```
$ python3 getConnectedInfo.py
```

# Screenshots
![/IMAGES/screenshot.png](/IMAGES/screenshot.png)



![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
