import sys, json, requests, time, pytest
from login import login
from datetime import datetime
from requests import Request, Session
from requests.auth import HTTPBasicAuth

#login variables
Host     = '10.133.136.85'
TcpPort  = '8080'
Protocol = 'http'
UserName = 'rwa'
PassWord = 'rwa'
LoginUrl = '%s://%s:%s/auth/token' % (Protocol,Host,TcpPort)
QueryUrl = '%s://%s:%s/rest/restconf/data/' % (Protocol,Host,TcpPort)

#vlan variables
vlanId = 101
stgId    = 1

#prepare HTTP Session
session         = Session()
session.verify  = False
session.timeout = 2
session.headers.update({'Accept':           'application/json',
                        'Accept-Encoding':  'gzip, deflate, br',
                        'Connection':       'keep-alive',
                        'Cache-Control':    'no-cache',
                        'Pragma':           'no-cache',
                        })

#vlan function
def test_vlan():
    global session

    with open('output.txt', 'w') as output_file:

        #updating header with auth-token
        session.headers.update({ 'X-Auth-Token': auth })
        
        #creating vlan
        dataObject = 'openconfig-vlan:vlans'

        data = {"openconfig-vlan:vlan": [
                    {
                        "config": {
                            "name": "VLAN-%s" % vlanId,
                            "vlan-id": vlanId,
    			"extreme-mod-oc-vlan:stg-id": "%s" % stgId
                        }
                    }
                ]
            }

        uri = QueryUrl + dataObject

        response = session.post( uri , json=data )
        
        if response.status_code != 201:
            print('ERROR: VLAN %s already exists' % vlanId)
            output_file.write('The POST request is FAIL for URI ' + uri + ' and Response is:\n\n')
            output_file.write('Status: '+ str(response.status_code) + ' ' + str(response.reason) + '\n')
            data = json.loads(response.content)
            json.dump(data, output_file, indent = 2)
            output_file.write('\n\n++++++++++++++++++++++++++++++++++++++\n\n')
        else:
            print('INFO: VLAN %s added' % vlanId)
            output_file.write('The POST request is PASS for creating VLAN %s' % vlanId +' and Response is:' + '\n' + str(response)+ '\n' + str(response.reason) +'\n')
            output_file.write('\n++++++++++++++++++++++++++++++++++++++\n')

        #getting vlan
        dataObject = 'openconfig-vlan:vlans/vlan=%s' % vlanId

        uri = QueryUrl + dataObject

        response = session.get(uri)
        
        if response.status_code != 200:
            print("ERROR: VLAN %s doesn't exists" % vlanId)
            output_file.write('The GET request is FAIL for URI ' + uri + ' and Response is:\n\n')
        else:
            print("INFO: found VLAN %s " % vlanId)
            output_file.write('The GET request is PASS for URI ' + uri + ' and Response is:\n\n')
        output_file.write('Status: ' + str(response.status_code) + ' ' + str(response.reason) + '\n')
        data = json.loads(response.content)
        json.dump(data, output_file, indent = 2)
        output_file.write('\n\n++++++++++++++++++++++++++++++++++++++\n\n')


        #deleting vlan
        dataObject = 'openconfig-vlan:vlans/vlan=%s' % vlanId

        uri = QueryUrl + dataObject

        response = session.delete( uri )
        
        if response.status_code != 204:
            print ('ERROR: HTTP ' + response.reason + ' (' + str(response.status_code) + ')')
            output_file.write('The DELETE request is FAIL for URI ' + uri + ' and Response is:\n\n')
            output_file.write('Status: '+ str(response.status_code) + ' ' + str(response.reason) + '\n')
            data = json.loads(response.content)
            json.dump(data, output_file, indent = 2)
            output_file.write('\n\n++++++++++++++++++++++++++++++++++++++\n\n')
        else:
            print ("INFO: VLAN %s deleted" % vlanId)
            output_file.write('The DELETE request is PASS for deleting VLAN %s' % vlanId +' and Response is:' + '\n' + str(response)+ '\n' + str(response.reason) +'\n')
            output_file.write('\n\n++++++++++++++++++++++++++++++++++++++\n\n')


#Main

auth = login(UserName,PassWord)
# test_vlan()