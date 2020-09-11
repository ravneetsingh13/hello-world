import sys, json, requests, time
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
def test_vlan(vlanId, stgId, auth):
    global session

    session.headers.update({ 'X-Auth-Token': auth })
    
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

    response = session.post( QueryUrl + dataObject, json=data )
    
    if response.status_code != 201:
        print('ERROR: HTTP ' + response.reason + ' (' + str(response.status_code) + ')')
    else:
        print ("INFO: VLAN %s added" % vlanId)

    #getting vlan
    dataObject = 'openconfig-vlan:vlans/vlan=%s' % vlanId

    response = session.get( QueryUrl + dataObject )
    
    if response.status_code != 200:
        print("INFO: VLAN %s doesn't exists" % vlanId)
    else:
        print("INFO: found VLAN %s " % vlanId)

    #deleting vlan
    dataObject = 'openconfig-vlan:vlans/vlan=%s' % vlanId

    response = session.delete( QueryUrl + dataObject )
    
    if response.status_code != 204:
        print ('ERROR: HTTP ' + response.reason + ' (' + str(response.status_code) + ')')
    else:
        print ("INFO: VLAN %s deleted" % vlanId)


#Main

auth = login(UserName,PassWord)
test_vlan(vlanId, stgId, auth)