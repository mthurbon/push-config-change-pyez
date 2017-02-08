from jnpr.junos import Device
from pprint import pprint
dev = Device(host='172.16.66.101',user='root',passwd='lab123')
from jnpr.junos.utils.config import Config
cu = Config(dev)
dev.open()
rsp = cu.load( path="config-example.conf" )
cu.commit()
