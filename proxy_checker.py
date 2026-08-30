import requests


def verify_proxy(proxy_url):
  test_url = "https://httpbin.org/ip"
  proxies = {"http": proxy_url, "https": proxy_url}

  try:
    print(f"[ProxyChecker] Verifying connection for proxy: {proxy_url}")
    response = requests.get(test_url, proxies=proxies, timeout=10)

    if response.status_code == 200:
      external_ip = response.json().get("origin")
      print(f"[ProxyChecker] Success! Live IP detected: {external_ip}")
      return True
    else:
      print(f"[ProxyChecker] Warning: Received status {response.status_code}")
      return False

  except Exception as e:
    print(f"[ProxyChecker] Error: Proxy is dead or unreachable. Details: {e}")
    return False
    
