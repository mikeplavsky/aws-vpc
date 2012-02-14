#!/usr/bin/python

import boto
from boto import config as cfg

conn = boto.connect_vpc()

cidr = cfg.get('VPC', 'cidr')
dhcp = cfg.get('VPC', 'dhcp-id')
ip = cfg.get('VPC', 'external-cidr')

vpc = conn.create_vpc(cidr) 
conn.create_subnet( vpc.id,cidr)

group = [gr for gr in conn.get_all_security_groups() if gr.vpc_id == vpc.id][0] 
conn.authorize_security_group(group_id=group.id, ip_protocol='tcp', from_port=0, to_port=65535, cidr_ip=ip)

gate = conn.create_internet_gateway()
conn.attach_internet_gateway( gate.id, vpc.id)

conn.associate_dhcp_options(dhcp , vpc.id)
