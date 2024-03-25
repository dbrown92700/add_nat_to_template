#!python
from vmanage_api import VmanageRestApi

###############################################################
# Edit these variables before using

vmanage_ip = '100.21.172.200'
vmanage_user = 'faraz'
vmanage_password = input('Enter your vmanage password: ')
start_nat = 1000
end_nat = 2000
templateId = '978cb573-9a8f-4506-853a-35be6042a4d8'
source_var = 'vpn_nat_static_source_ip_'
translate_var = 'vpn_nat_static_translate_ip_'

###############################################################
url = f'/template/feature/object/{templateId}'
vmanage = VmanageRestApi(vmanage_ip, vmanage_user, vmanage_password)
template = vmanage.get_request(url)
new_template = {}
for x in ['deviceType', 'templateType', 'templateMinVersion', 'templateDefinition', 'factoryDefault']:
    new_template[x] = \
        template[x]
new_template['templateName'] = 'COPY_OF_' + template['templateName']
new_template['templateDescription'] = 'COPY_OF_' + template['templateDescription']

for x in range(start_nat, end_nat):

    nat = {
        "pool-name": {
            "vipObjectType": "object",
            "vipType": "ignore",
            "vipValue": "_empty",
            "vipVariableName": "vpn_nat_static_pool_name"
        },
        "source-ip": {
            "vipObjectType": "object",
            "vipType": "variableName",
            "vipValue": "",
            "vipVariableName": f'{source_var}{x}'
        },
        "translate-ip": {
            "vipObjectType": "object",
            "vipType": "variableName",
            "vipValue": "",
            "vipVariableName": f'{translate_var}{x}'
        },
        "static-nat-direction": {
            "vipObjectType": "object",
            "vipType": "constant",
            "vipValue": "inside",
            "vipVariableName": "vpn_nat_static_nat_direction"
        },
        "vipOptional": True,
        "priority-order": [
            "source-ip",
            "translate-ip",
            "static-nat-direction",
            "pool-name"
        ]
    }
    new_template['templateDefinition']['nat']['static']['vipValue'].append(nat)

url = '/template/feature'
template_id = vmanage.post_request(url, new_template)
print(template_id)