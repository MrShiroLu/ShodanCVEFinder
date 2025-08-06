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

To install dependencies:
```bash
pip install shodan google-generativeai pyfiglet
```

## API Keys
You need to create the following files and add your API keys:

- `API/apiKeyShodan.txt` : Should contain your Shodan API key.
- `API/apiKeyGemini.txt` : Should contain your Google Gemini API key.

Each file should contain only the key, nothing else.

## Folder Structure
```
ShodanCVEFinder/
  ├── API/
  │    ├── apiKeyShodan.txt
  │    └── apiKeyGemini.txt
  ├── main.py
  ├── Modules/
  │    ├── find.py
  │    ├── greeting.py
  │    └── shodanSearchV1.py
  ├── Results/
  │    └── cve_results_{IP}.txt
```