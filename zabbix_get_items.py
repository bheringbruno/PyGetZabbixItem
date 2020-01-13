import requests, json, os, sys
from pyzabbix.api import ZabbixAPI

template = sys.argv[1]

dict_item = {}
dict_trigger = {}

def get(user, password, template, url):
    zabbix = ZabbixAPI(url=url, user=user, password=password)
    f = zabbix.do_request('template.get', {'filter': {'host': template},'output': 'templateid'})
    templateid = f['result'][0]['templateid']
    item = zabbix.do_request('item.get',{'templateids': templateid,'output': 'extend'})
    for n in item['result']:
         dict_item.update({ n['name']: n['key_']})
    get_triggers(templateid, url, user, password)

def get_triggers(templateid, url, user, password):
    zabbix = ZabbixAPI(url=url, user=user, password=password)
    item = zabbix.do_request('trigger.get',{'templateids': templateid,'output': 'extend'})
    for n in item['result']:
        dict_trigger.update({ n['triggerid']: n['description']})
    zabbix.user.logout()

def get_items(template):
    template = template
    url = os.environ['URL']
    user = os.environ['USER']
    password = os.environ['PASSWORD']
    get(user, password, template, url)

def main():
    get_items(template)
    print("ITEMS" + json.dumps(dict_item, indent=4, sort_keys=True))
    print("TRIGGERS" + json.dumps(dict_trigger, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()
