import shodan

api = shodan.Shodan('YOUR_API_KEY')

# Lookup an IP
ipinfo = api.host('IP_ADDRESS')
#print(dir(shodan))
print(ipinfo["ports"])

for item in ipinfo["data"]:
    print(item["port"], item.get("product", "Unknown product"))


"""
# Search for websites that have been "hacked"
for banner in api.search_cursor('http.title:"hacked by"'):
    print(banner)

# Get the total number of industrial control systems services on the Internet
ics_services = api.count('tag:ics')
print('Industrial Control Systems: {}'.format(ics_services['total']))"""