#!/usr/bin/env python3
import requests
import argparse
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

# We pretend to be a Google Chrome browser on Windows 10
HEADERS_TO_SEND = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5'
}

SECURITY_HEADERS = {
    "Strict-Transport-Security": "Forces HTTPS (Prevents MITM).",
    "Content-Security-Policy": "Prevents XSS attacks.",
    "X-Frame-Options": "Prevents Clickjacking.",
    "X-Content-Type-Options": "Prevents MIME-sniffing.",
    "Referrer-Policy": "Controls outbound link info.",
    "Permissions-Policy": "Restricts browser features."
}

def analyze_headers(url):
    if not url.startswith("http"):
        url = "https://" + url

    print(f"{BLUE}[*] Analyzing: {url}{RESET}")
    print("-" * 60)

    try:
        # We now send the fake browser headers
        response = requests.get(url, headers=HEADERS_TO_SEND, timeout=5, verify=False, allow_redirects=True)
        
        print(f"{YELLOW}[*] Final Destination: {response.url}{RESET}")
        print("-" * 60)
        
        headers = response.headers
        missing_count = 0
        total_headers = len(SECURITY_HEADERS)

        for header, description in SECURITY_HEADERS.items():
            # Special check for Google's Report-Only CSP
            if header == "Content-Security-Policy" and "Content-Security-Policy-Report-Only" in headers:
                print(f"{GREEN}[+] SECURE (Report-Only): {header}{RESET}")
            elif header in headers:
                print(f"{GREEN}[+] SECURE: {header}{RESET}")
            else:
                print(f"{RED}[-] MISSING: {header} ({description}){RESET}")
                missing_count += 1

        print("-" * 60)
        score = total_headers - missing_count
        print(f"{BLUE}[*] Score: {score}/{total_headers}{RESET}")

        if missing_count == 0:
            print(f"{GREEN}[!] Excellent! This site is well-secured.{RESET}")
        elif missing_count <= 2:
            print(f"{YELLOW}[!] Warning: Missing some headers.{RESET}")
        else:
            print(f"{RED}[!] CRITICAL: Highly vulnerable. Missing many headers.{RESET}")

    except requests.exceptions.RequestException as e:
        print(f"{RED}[!] Error connecting: {e}{RESET}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HTTP Security Header Analyzer")
    parser.add_argument("-u", "--url", required=True, help="Target URL (e.g., example.com)")
    args = parser.parse_args()
    analyze_headers(args.url)
