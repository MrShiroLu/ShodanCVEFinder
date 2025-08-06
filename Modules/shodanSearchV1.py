import shodan

def search_shodan(ip):

    with open("API/apiKeyShodan.txt", "r", encoding="utf-8") as f:
        key = f.read().strip()

    api = shodan.Shodan(key)
    
    proAndServ = []

    try:
        host = api.host(ip)

        print(f"Open Ports: {host['ports']}")
        
        for item in host['data']:
            print(f"\nPort: {item['port']}")
            print(f"Product: {item.get('product', '')}\nVersion: {item.get('version', '')}")
            
            proAndServ.append(f"{item.get('product', '')} {item.get('version', '')}")

            if 'vulns' in item:
                print("Vulnerabilities:")
                for vuln in item['vulns']:
                    print(f"  - {vuln}")
                    proAndServ.append(f" Cve: {vuln}")
            
            print("="*80)

    except shodan.APIError as e:
        print(f"Error: {e}")

    return proAndServ