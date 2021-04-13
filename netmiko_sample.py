import netmiko
from netmiko import ConnectHandler

router = {}
router['device_type'] = 'cisco_xr'
router['ip'] = 'sbx-iosxr-mgmt.cisco.com'
router['username'] = 'admin'
router['password'] = 'C1sco12345'
router['port'] = 8181


if __name__ == '__main__':
    net_connect = ConnectHandler(**router)

    # roda o comando e printa no python
    output = net_connect.send_command('show ip int brief')
    print(output)

    # roda a configuracao (implicito o comando configure)
    output = net_connect.send_config_set(['hostname fabmoura_devnet2'])

    # realiza commit das alteracoes
    net_connect.commit()
    print(output)
