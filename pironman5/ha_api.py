
import requests
from utils import log
import os

class HA_API:

    def __init__(self, url="http://supervisor/"):
        if not self.is_homeassistant_addon():
            log(msg="Not home assistant addon, skip init", level='DEBUG')
            return
        self.url = url
        self.token = os.environ['SUPERVISOR_TOKEN']
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    @staticmethod
    def is_homeassistant_addon():
        return 'SUPERVISOR_TOKEN' in os.environ

    def get(self, endpoint):
        try:
            url = f"{self.url}{endpoint}"
            r = requests.get(url, headers=self.headers)
            return r.json()
        except Exception as e:
            log(msg="home assistant get error: " + e, level='WARNING')

    def set(self, endpoint, data=None):
        try:
            url = f"{self.url}{endpoint}"
            requests.post(url, headers=self.headers)
        except Exception as e:
            log(msg="home assistant get error: " + e, level='WARNING')

    def get_ip(self):
        IPs = {}
        data = self.get("network/info")
        interfaces = data["data"]["interfaces"]
        for interface in interfaces:
            name = interface['interface']
            ip = interface['ipv4']['address']
            if len(ip) == 0:
                continue
            ip = ip[0]
            if ip == '':
                continue
            if "/" in ip:
                ip = ip.split("/")[0]
            IPs[name] = ip
        return IPs

    def get_network_connection_type(self):
        connection_type_map = {
            "ethernet": "Wired",
            "wireless": "Wireless",
        }
        connection_type = []
        data = self.get("network/info")
        interfaces = data["data"]["interfaces"]
        for interface in interfaces:
            if interface['connected']:
                connection_type.append(connection_type_map[interface['type']])
        return connection_type

    def shutdown(self):
        '''shutdown homeassistant host'''
        log.info(msg="Shutdown home assistant host")
        self.set("host/shutdown")

