#!/usr/bin/python

import boto
from boto import config as cfg

conn = boto.connect_vpc()
cidr = "10.0.0.0/24"

vpc = conn.create_vpc(cidr) 
conn.create_subnet( vpc.id,cidr)

gate = conn.create_internet_gateway()
conn.attach_internet_gateway( gate.id, vpc.id)

conn.associate_dhcp_options( "dopt-c2ad5eaa", vpc.id )
