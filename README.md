# ShodanCVEFinder

ShodanCVEFinder is a tool that finds open ports and services for a given IP address using the Shodan API, then queries known CVE (vulnerability) information for these services via the Google Gemini API. Results are saved to a file.

## Features
- Finds open ports and services for an IP address using the Shodan API.
- Searches for CVEs (Vulnerabilities) for discovered services using the Google Gemini API.
- Displays results on the screen and saves them under the `Results/` folder.
- User-friendly, step-by-step command-line interface.

## Requirements
- Python 3.8+
- [Shodan](https://pypi.org/project/shodan/) Python package
- [google-generativeai](https://pypi.org/project/google-generativeai/) Python package
- [pyfiglet](https://pypi.org/project/pyfiglet/) Python package
- [python-dotenv](https://pypi.org/project/python-dotenv/) Python package


To install dependencies:
```bash
pip install shodan google-generativeai pyfiglet python-dotenv
```

## Folder Structure
```
ShodanCVEFinder/
  ├── main.py
  ├── .env
  ├── Modules/
  │    ├── find.py
  │    ├── greeting.py
  │    └── shodanSearchV1.py
  ├── Results/
  │    └── cve_results_{IP}.txt
```