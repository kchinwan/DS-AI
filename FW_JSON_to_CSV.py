import pandas as pd
import json


# exporting data to CSV
def importdata_in_csv ( NAME, ACTION, S_ZONES, S_NETWORKS, S_PORTS, D_ZONES,D_NETWORKS, D_PORTS, USERS, ACTIONS, INTRUSION_POLICY):
    dict = {'NAME' : NAME, 'ACTION' : ACTION, 'S_ZONES':S_ZONES,'S_NETWORKS': S_NETWORKS,'S_PORTS': S_PORTS, 'D_ZONES':D_ZONES, 'D_NETWORKS': D_NETWORKS, 'D_PORTS': D_PORTS, 'USERS': USERS,'ACTIONS': ACTIONS,'INTRUSION_PREVENTION_POLICY': INTRUSION_POLICY }
    df = pd.DataFrame(dict)
    df.to_csv('wldfw1_25Jan.csv')



# Opening JSON file
f = open('clprodfw1_25Jan.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)


#parameters
NAME = []
ACTION = []
S_ZONES = []
S_NETWORKS = []
S_PORTS = []
D_ZONES = []
D_NETWORKS = []
D_PORTS = []
APPLICATIONS = []
URLS = []
USERS = []
ACTIONS = []
INTRUSION_POLICY = []
# Sub-parameters
s_zone = []
s_network =[]
s_port = []
d_zone = []
d_network = []
d_port = []
user = []


# Iterating through the json list
for i in data['items']:
    NAME.append(i['name'])
    ACTION.append(i['ruleAction'])
    if i['sourceNetworks'] == []:
        S_NETWORKS.append("ANY")
    else :
        s_network.clear()
        for sn in i['sourceNetworks']:
            s_network.append(sn['name'])
        S_NETWORKS_1 = '\n'.join(s_network)
        S_NETWORKS.append(S_NETWORKS_1)
    if i['sourceZones'] == []:
        S_ZONES.append("ANY")
    else:
        s_zone.clear()
        for  y in i['sourceZones']:
            s_zone.append(y['name'])
        S_ZONES_1 = '\n'.join(s_zone)
        S_ZONES.append(S_ZONES_1)
    if i['sourcePorts'] == []:
        S_PORTS.append("ANY")
    else:
        s_port.clear()
        for sp in i['sourcePorts']:
            s_port.append(sp['name'])
        S_PORTS_1 = '\n'.join(s_port)
        S_PORTS.append(S_PORTS_1)
    if i['destinationZones'] == []:
        D_ZONES.append("ANY")
    else:
        d_zone.clear()
        for dz in i['destinationZones']:
            d_zone.append(dz['name'])
        D_ZONES_1 = '\n'.join(d_zone)
        D_ZONES.append(D_ZONES_1)
    if i['destinationNetworks'] == []:
        D_NETWORKS.append("ANY")
    else:
        d_network.clear()
        for dn in i['destinationNetworks']:
            d_network.append(dn['name'])
        D_NETWORKS_1 = '\n'.join(d_network)
        D_NETWORKS.append(D_NETWORKS_1)
    if i['destinationPorts'] == []:
        D_PORTS.append("ANY")
    else:
        d_port.clear()
        for dp in i['destinationPorts']:
            d_port.append(dp['name'])
        D_PORTS_1 = '\n'.join(d_port)
        D_PORTS.append(D_PORTS_1)
    if i['users'] == []:
        USERS.append("ANY")
    else:
        user.clear()
        for u in i['users']:
            user.append(i['name'])
        USERS_1 = '\n'.join(user)
        USERS.append(USERS_1)
    ACTIONS.append(i['eventLogAction'])
    if i['intrusionPolicy'] == None :
        INTRUSION_POLICY.append("null")
    else :
        ip = i['intrusionPolicy']
        INTRUSION_POLICY.append(ip['name'])

importdata_in_csv(NAME, ACTION, S_ZONES, S_NETWORKS, S_PORTS, D_ZONES,D_NETWORKS, D_PORTS, USERS, ACTIONS, INTRUSION_POLICY)

    

print(len(S_NETWORKS))
print(len(D_PORTS))
print(len(D_ZONES))
print(len(S_PORTS))

f.close()
print("complete")