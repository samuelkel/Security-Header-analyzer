## 🧠 Project Overview
Many organizations fail to configure HTTP security headers, leaving them vulnerable to attacks like Cross-Site Scripting (XSS) and Clickjacking. This tool was built to quickly audit web servers and grade their security posture based on missing headers.

### The Technical Challenge
During development, I discovered that analyzing `google.com` initially resulted in a "Critical" score. 
This was due to two real-world web behaviors:
1. **Redirects:** Google redirects `google.com` to `www.google.com`. The initial scan was only checking the redirect response, not the final destination.
2. **Bot Protection:** The server detected the Python `requests` library and stripped security headers to save bandwidth. 

### The Solution
To make this tool production-ready, I implemented:
*   `allow_redirects=True` to ensure the script evaluates the final HTTP 200 OK response.
*   **User-Agent Spoofing** to mimic a standard Chrome browser, bypassing basic bot-protection mechanisms.
*   **Header Normalization** to detect edge cases like Google's `Content-Security-Policy-Report-Only` header.

## 📸 Screenshot
<img width="1079" height="800" alt="Screenshot_20261112-115052" src="https://github.com/user-attachments/assets/7586f682-5efb-44af-9acc-721df36f1243" />
