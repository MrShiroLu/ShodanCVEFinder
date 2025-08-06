from pyfiglet import figlet_format

def opening():
    print("="*80)    
    
    netowkrMapper = figlet_format("ShodanCVE ", font="slant")
    
    print(netowkrMapper)
    print("Please make sure you have the apiKeyGemini.txt and apiKeyShodan.txt files in the Modules folder.")
    print("Enter the IP address you want to search.")