import google.generativeai as genai
import time

def find_cve(info,ip_address):

    with open("API/apiKeyGemini.txt", "r", encoding="utf-8") as f:
        key = f.read().strip()

    genai.configure(api_key=key)
    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(f"""Given a software named "{info}", check whether it has multiple known CVEs (Common Vulnerabilities and Exposures).

    If it has one or more CVEs, list ALL of them separately. Do not stop at the first one.
    For each CVE, write the following clearly in plain text (no markdown, no asterisks, no hashtags, no formatting):

    Important:
    - Do not use any markdown syntax (no #, *, -, etc.)
    - Do not summarize or skip CVEs
    - Do not stop after the first CVE
    - Output must be plain, structured text only
    - Outout must be like this:
        CVE ID: CVE-YYYY-NNNN
        Description: [1-2 sentence description]
        Mitigation: [1-2 sentence mitigation]
        Exploitation: [1-2 sentence explanation]
         
        NIST: https://nvd.nist.gov/vuln/detail/cve-YYYY-NNNN
    - If no CVEs are found, respond exactly with:
        No known CVEs found for this version.""")
    
    with open(f"Results/cve_results_{ip_address}.txt", "w", encoding="utf-8") as f:
        f.write(response.text)

    return response.text