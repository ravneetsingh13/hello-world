import sys
import json
import time
from datetime import datetime
import requests
from requests import Request, Session
from requests.auth import HTTPBasicAuth

########################################################################
# variables
Host     = '10.133.136.85'
TcpPort  = '8080'
Protocol = 'http'
UserName = 'rwa'
PassWord = 'rwa'
LoginUrl = '%s://%s:%s/auth/token' % (Protocol,Host,TcpPort)
QueryUrl = '%s://%s:%s/rest/restconf/data/' % (Protocol,Host,TcpPort)

########################################################################
# prepare HTTPs session
session         = Session()
session.verify  = False
session.timeout = 2
session.headers.update({'Accept':           'application/json',
                        'Accept-Encoding':  'gzip, deflate, br',
                        'Connection':       'keep-alive',
                        'Cache-Control':    'no-cache',
                        'Pragma':           'no-cache',
                        })

###############################################################
##                       routines                            ##
###############################################################
def login(UserName,PassWord):
    global session
    
    body = '{"username": "%s", "password" : "%s" }' % (UserName,PassWord)
    #headers= '{"content-type":"application/json"}'
    print(LoginUrl)
    
    try:
        response = session.put( LoginUrl, body )
        print(json.dumps(response.json()))        
        print(response)
    except KeyboardInterrupt:
        print ("INFO: CTRL-C interuption")
        sys.exit(0)
    except Exception:
        print ('ERROR: host '+ Host + ' unreachable')
        sys.exit(1)

    if response.status_code != 200:
        print ("{0:0.1f}ms   ERROR: login failed".format( response.elapsed.total_seconds() * 1000 ))
        print (response.headers)
        sys.exit(1)
    else:
        print ("{0:0.1f}ms   INFO: login passed".format( response.elapsed.total_seconds() * 1000 ))

    session.headers.update({ 'X-Auth-Token': response.headers['X-Auth-Token'] })

    authorizationcode = response.headers['X-Auth-Token']
    return authorizationcode