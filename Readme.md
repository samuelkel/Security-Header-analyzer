HTTP Security Header Analyzer

A lightweight Python tool designed to perform reconnaissance on web servers by analyzing their HTTP response headers. 

🛠️ Features
- **User-Agent Spoofing:** Mimics a real browser to bypass basic bot protections.
- **Redirect Handling:** Follows 301/302 redirects to analyze the final destination.
- **CSP Edge-case Handling:** Detects `Content-Security-Policy-Report-Only` headers.
- **Color-Coded Output:** Instantly see which headers are secure and which are missing.

🚀 Usage
bash
python3 security_header_analyzer.py -u google.com

⚠️ Disclaimer

This tool is for educational purposes and authorized security testing only.