## Get Item Zabbix ##

* Python 3

### Install ###
You can install Zabbix modules for Python with pip:

```
pip3 install py-zabbix
```

### Examples ###

```
export USER=username
export PASSWORD=password

zabbix_get_items.py "http://server.name/" "Template-Name"
```

### Output ###
* Json
