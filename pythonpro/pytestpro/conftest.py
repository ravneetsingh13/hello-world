import pytest
import telnetlib

@pytest.fixture
def telnet_dut():
    hostname = "10.133.136.85"
    username = "rwa"
    password = "rwa"
    t = telnetlib.Telnet(hostname)            # actively connects to a telnet server
    t.read_until(b'Login:', 10)               # waits until it recieves a string 'login:'
    t.write(username.encode('utf-8'))         # sends username to the server
    print("User name has entered")
    t.write(b'\r')                            # sends return character to the server
    t.read_until(b'Password:', 10)            # waits until it recieves a string 'Password:'
    print("Password has entered")
    t.write(password.encode('utf-8'))         # sends password to the server
    t.write(b'\r')                            # sends return character to the server
    t.write(b'enable\r') 
    n, match, previous_text = t.expect([br'Login failed', br'Bad Login/Password'], 4)
    if n == 0:
        print('Username and password failed - giving up')
    else:
        t.write(b'conf t\r')
        t.read_until(b'#',5)
        t.write(b'cli timeout 65535\r')
        t.read_until(b'#',5)
        t.write(b'terminal length 64\r')
        t.read_until(b'#',5)
        t.write(b'exit\r')
    yield t
    print("teardown telnet")
    t.close()
