import shodan

API_KEY = "YOUR_APİ"
api = shodan.Shodan(API_KEY)

ip = "IP_ADdRESS"

try:
    host = api.host(ip)

    print(f"Açık portlar: {host['ports']}")
    print("\nDetaylı bilgi:")

    for item in host['data']:
        print(f"\nPort: {item['port']}")
        print(f"Servis: {item.get('product', 'Bilinmiyor')} version: {item.get('version', '')} data: {item.get('data', '')}")
        
        if 'vulns' in item:
            print("Zafiyetler (CVE):")
            for vuln in item['vulns']:
                print(f"  - {vuln}")

except shodan.APIError as e:
    print(f"Hata: {e}")
