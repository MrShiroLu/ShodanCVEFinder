from Modules.shodanSearchV1 import search_shodan
from Modules.find import find_cve   
from Modules.greeting import opening

def main():
    opening()
    ip_address = str(input("Enter the IP address to search: ")).strip()

    if ip_address == "" or len(ip_address) > 15 or len(ip_address) < 7:
        print("No IP address provided. Exiting.")
        exit(0)

    print("Starting Shodan search...")
    shodan_results = search_shodan(ip_address)
    print("Shodan search completed.")

    print("Starting CVE search...")
    cve_results = find_cve(shodan_results,ip_address)
    print("CVE search completed.")

    print("-"*80)
    print(cve_results)

if __name__ == "__main__":
    main()