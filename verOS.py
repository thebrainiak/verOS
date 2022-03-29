#!/usr/bin/python3

#coding: utf-8

import re, sys, subprocess


#formato python3 verOS.py IP

if len(sys.argv) != 2:

	print("\n[!] Te has enterao? Se usa - python3" + sys.argv[0] +  "direccion ip")
	sys.exit(1)

def get_ttl(ip_address):

	proc = subprocess.Popen(["/usr/bin/ping -c 1 %s" % ip_address, ""], stdout = subprocess.PIPE, shell = True)
	(out,err) = proc.communicate()

	out = out.split()
	out = out[12].decode('utf-8')

	ttl_value = re.findall(r"\d{1,3}", out)[0]

	return ttl_value


def get_os(ttl):

	ttl = int(ttl)

	if ttl >= 0 and ttl <= 64:
		return "Esto es linux lo más seguro"

	elif ttl >= 85 and ttl <= 128:

		return "Esto es windows y bill lo sabe"

	else:
		return "Not Found"

if __name__ == '__main__':

	ip_address = sys.argv[1]
 
	ttl = get_ttl(ip_address)

	os_name = get_os(ttl)

	print("\n%s -> %s): %s\n" % (ip_address, ttl, os_name))