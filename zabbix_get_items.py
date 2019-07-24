import requests, json, os, sys
from pyzabbix.api import ZabbixAPI

template = sys.argv[1]
url = sys.argv[0]
dicionario = {}

def get(user, password, template):
    zabbix = ZabbixAPI(url=url, user=user, password=password)
    f = zabbix.do_request('template.get', {'filter': {'host': template},'output': 'templateid'})
    templateid = f['result'][0]['templateid']
    item = zabbix.do_request('item.get',{'templateids': templateid,'output': 'extend'})
    for n in item['result']:
         dicionario.update({ n['name']: n['key_']})
    zabbix.user.logout()

def get_items(template):
    template = template
    user = os.environ['USER']
    password = os.environ['PASSWORD']
    get(user, password, template)

def main():
    get_items(template)
    print(json.dumps(dicionario, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()
