## Get Item & Triggers Zabbix ##

* Python 3

### Install ###
You can install Zabbix modules for Python with pip:

```
pip3 install py-zabbix
```

### Examples ###

```
export URL="http://zabbix.server.name/"
export USER=username
export PASSWORD=password

python3 zabbix_get_items.py "Template-Name"
```

### Output ###
* Json
