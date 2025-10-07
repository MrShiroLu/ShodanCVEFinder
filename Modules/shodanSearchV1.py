import os
import shodan
from dotenv import load_dotenv


def search_shodan(ip):

    load_dotenv()
    key = os.getenv("API_SHO")

    if not key:
        raise ValueError("API_KEY not found in environment variables")

    api = shodan.Shodan(key)
    
    proAndServ = []

    try:
        host = api.host(ip)

        print(f"Open Ports: {host['ports']}")
        
        for item in host['data']:
            print(f"\nPort: {item['port']}")
            print(f"Product: {item.get('product', 'UNKOWN')}\nVersion: {item.get('version', 'UNKOWN')}")
            
            proAndServ.append(f"{item.get('product', 'UNKOWN')} {item.get('version', 'UNKOWN')}")

            if 'vulns' in item:
                print("Vulnerabilities:")
                for vuln in item['vulns']:
                    print(f"  - {vuln}")
                    proAndServ.append(f" Cve: {vuln}")
            
            print("="*80)

    except shodan.APIError as e:
        print(f"Error: {e}")

    return proAndServ