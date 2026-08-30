from playwright.sync_api import sync_playwright
from behavior import BehaviorEngine
from session_manager import SessionManager
from proxy_checker import verify_proxy


class AccountInstance:

  def __init__(self, account_config):
    self.username = account_config["username"]
    self.proxy_url = account_config["proxy"]
    self.session_file = account_config["session_file"]

    self.session_mgr = SessionManager(self.username, self.session_file)
    self.behavior = BehaviorEngine(self.username)

  def initialize_instance(self):
    print(
        f"\n[AccountInstance] Initializing browser environment for:"
        f" {self.username}"
    )

    # Pre-flight proxy check
    if not verify_proxy(self.proxy_url):
      print(f"[AccountInstance] Aborting task for {self.username} due to proxy failure.")
      return

    with sync_playwright() as p:
      proxy_config = {"server": self.proxy_url}

      browser = p.chromium.launch(headless=False, proxy=proxy_config)

      context = browser.new_context(
          user_agent=(
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
              " (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
          )
      )

      cookies = self.session_mgr.load_session()
      if cookies:
        try:
          context.add_cookies(cookies)
          print(f"[AccountInstance] ({self.username}) Cookies injected.")
        except Exception as e:
          print(f"[AccountInstance] Error adding cookies: {e}")

      page = context.new_page()

      try:
        print(f"[AccountInstance] ({self.username}) Navigating to Reddit...")
        page.goto("https://www.reddit.com", timeout=60000)

        self.behavior.simulate_scroll_and_read(page)
        self.behavior.human_jitter(page, 5, 10)

        updated_cookies = context.cookies()
        self.session_mgr.save_session(updated_cookies)

      except Exception as e:
        print(f"[AccountInstance] Error during execution for {self.username}: {e}")

      finally:
        browser.close()
        print(f"[AccountInstance] Browser closed for: {self.username}\n")
