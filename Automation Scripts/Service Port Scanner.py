#Python script that allows me to modify the dictionary and scan the devices in my lab quickly to see whether they are up and running.

import socket
import datetime

services = {
    'pi-hole' :{'host': '192.168.1.101',
                'port': 443,
                'protocol' : 'TCP'},
    'Cisco Catalyst 3750' :{'host': '192.168.1.75',
                            'port': 22,
                            'protocol': 'TCP'},
    'PFSense Firewall' :{'host': '172.16.1.1',
                         'port': 443,
                         'protocol': 'TCP'}
}

def port_scan(host, port, protocol):
    #Checks if port number is an integer and tries to convert if possible.
    try:
        port = int(port)
    except ValueError:
        return("Port must be a number")
    #Checks whether the port is a number between 0-65355
    if port < 0 or port > 65535:
        return('Port number incorrect')
    #Checkes whether the value is UDP or TCP and adjusts protocols.
    if protocol == 'TCP':
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.settimeout(1)
        result = server.connect_ex((host,port))
        if result == 0:
            server.close()
            return(f'Hostname: {host} is open on port {port} using TCP')
        else:
            server.close()
            return(f'Hostname: {host} is closed on port {port} - TCP')
    elif protocol == 'UDP':
        return('UDP scanning not implemented yet')
    else:
        return('Protocol error. Invalid TCP/UDP value')

       
#for loop that iterates through all entries in the dictionary and performs the function on each of them.

for service, specs in services.items():
        currenttime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f' {currenttime} - Scanning {service}.....')
        print(port_scan(**specs))
