import pytest
import csv

def test_commands(telnet_dut):
	with open('commands.csv','r') as input_file, open('output.txt','wb') as output_file:
		reader = csv.DictReader(input_file)
		for line in reader:
			telnet_dut.write(b'conf t\r')
			telnet_dut.read_until(b'(config)#',5)
			telnet_dut.write(line['commands'].encode('utf-8'))
			telnet_dut.write(b'\rq\b')
			output = telnet_dut.read_until(b'#',5)
			writer = output_file.write(output)
			telnet_dut.write(b'exit\r')