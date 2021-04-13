from ncclient import manager
import xml.dom.minidom

router = {}
router['device_type'] = 'cisco_xr'
router['ip'] = 'sbx-iosxr-mgmt.cisco.com'
router['username'] = 'admin'
router['password'] = 'C1sco12345'
router['port'] = 10000
if __name__ == '__main__':

    with manager.connect(host=router['ip'],
                        port=router['port'],
                        username=router['username'],
                        password=router['password'],
                        hostkey_verify=False) as m:
        data = '''
            <config>
                <vrfs xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-infra-rsi-cfg">
                    <vrf>
                        <vrf-name>CustomerA</vrf-name>
                        <create></create>
                        <bgp-global xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-bgp-cfg">
                            <route-distinguisher>
                                <type>as</type>
                                <as-xx>0</as-xx>
                                <as>65000</as>
                                <as-index>10</as-index>
                            </route-distinguisher>
                        </bgp-global>
                    </vrf>
                </vrfs>
            </config>  
           '''

        result = m.edit_config(target="candidate", config=data).xml
        result = m.commit()
        print(result)