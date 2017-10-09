#!/usr/bin/env python
#-*- coding:utf-8 -*-

import nmap

nm = nmap.PortScanner() # instantiate nmap.PortScanner object
nm.scan('127.0.0.1', '22-443') # scan host 127.0.0.1, ports from 22 to 443
print nm.command_line() # get command line used for the scan : nmap -oX - -p 22-443 127.0.0.1
print nm.scaninfo() # get nmap scan informations {'tcp': {'services': '22-443', 'method': 'connect'}}
print nm.all_hosts() # get all hosts that were scanned
print nm['127.0.0.1'].hostname() # get one hostname for host 127.0.0.1, usualy the user record
print nm['127.0.0.1'].hostnames() # get one hostname for host 127.0.0.1, usualy the user record
print nm['127.0.0.1'].state() # get state of host 127.0.0.1 (up|down|unknown|skipped) 
