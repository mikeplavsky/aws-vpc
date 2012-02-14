#!/usr/bin/python

import boto
from boto import config as cfg

conn = boto.connect_vpc()

cidr = boto.config.get('VPC', 'cidr')
dhcp = boto.config.get('VPC', 'dhcp-id') 

vpc = conn.create_vpc(cidr) 
conn.create_subnet( vpc.id,cidr)

group = conn.create_security_group("VPCIN", "important text", vpc.id)
print group.id

gate = conn.create_internet_gateway()
conn.attach_internet_gateway( gate.id, vpc.id)

conn.associate_dhcp_options(dhcp , vpc.id)
