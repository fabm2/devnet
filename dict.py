from os import system
from ncclient import manager
from pprint import pprint as pp

# DICTIONARY FOR DEVNET IOS-XE ROUTER
router = {
    "host": "dasdjfosd",
    "port": "10000",
    "username": "developer",
    "password": "C1sco12345",
    "hostkey": False
}
# FILTER2 OUTPUT CONFIGURED STATE OF SPECIFIC INTERFACE
netconf_filter3 = """
    <filter>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>GigabitEthernet1</name>
            </interface>
        </interfaces>
    </filter>
"""
# CLEAR CONSOLE
with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"],
                     hostkey_verify=router["hostkey"]) as m:
    print("*" * 50 + "BREAK" + "*" * 50)
    # SEND RPC CALL "get-config" requesting filtered data listed in netconf_filterX variable
    interface_netconf = m.get(netconf_filter3)
    # CONVERT RPC-REPLY object TO XML object
    #xmldata = xmld.parseString(str(interface_netconf))
    # Print XML data
    #print(xmldata.toprettyxml(indent="  "))
    print("*" * 50 + "BREAK" + "*" * 50)
    print("m.get is : " + str(type(m.get)))
    print("interface_netconf is : " + str(type(interface_netconf)))
    #print("xmldata is : " + str(type(xmldata)))
    # CLOSE SESSION
# END