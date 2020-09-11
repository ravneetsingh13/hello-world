import pytest

def test_show_soft(telnet_dut):
    telnet_dut.read_until(b'#',5)
    telnet_dut.write(b'show software\r')
    print(telnet_dut.read_until(b'#',5))
   

def test_show_sys_soft(telnet_dut):
    telnet_dut.read_until(b'#',5)
    telnet_dut.write(b'show sys software\r')
    print(telnet_dut.read_until(b'#',5))

def test_show_vlan_members(telnet_dut):
    telnet_dut.read_until(b'#',5)
    telnet_dut.write(b'show vlan members\r')
    print(telnet_dut.read_until(b'#',5))

def test_show_ip_interface(telnet_dut):
    telnet_dut.read_until(b'#',5)
    telnet_dut.write(b'show ip interface\r')
    print(telnet_dut.read_until(b'#',5))

def test_show_spbm(telnet_dut):
    telnet_dut.read_until(b'#',5)
    telnet_dut.write(b'show spbm\r')
    print(telnet_dut.read_until(b'#',5))
