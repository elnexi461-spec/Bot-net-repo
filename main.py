import json
import random
import time


class RedditAutomationBot:

  def __init__(self, username, proxy_url, session_file):
    self.username = username
    self.proxy_url = proxy_url
    self.session_file = session_file

  def load_session_state(self):
    """Loads existing session cookies to avoid repeated logins and triggers."""
    try:
      with open(self.session_file, 'r') as f:
        print(f'[{self.username}] Loaded existing cookies successfully.')
        return json.load(f)
    except FileNotFoundError:
      print(f'[{self.username}] No session file found. Fresh login required.')
      return None

  def human_jitter(self, min_seconds=30, max_seconds=90):
    """Introduces randomized delays to mimic human reading and reaction time."""
    wait_time = random.uniform(min_seconds, max_seconds)
    print(
        f'[{self.username}] Pausing for {wait_time:.2f} seconds (Jitter'
        ' active)...'
    )
    time.sleep(wait_time)

  def simulate_organic_browsing(self):
    """Simulates scrolling and passive feed viewing before executing actions."""
    print(
        f'[{self.username}] Simulating organic feed scrolling via proxy:'
        f' {self.proxy_url}'
    )
    self.human_jitter(15, 45)

  def execute_task(self):
    """Main execution loop for the specific account workflow."""
    print(f'\n--- Initializing Session for: {self.username} ---')

    # 1. Load Session Cookies
    cookies = self.load_session_state()

    # 2. Emulate Human Pre-action Behavior
    self.simulate_organic_browsing()

    # 3. Perform Target Operation with Pacing
    print(f'[{self.username}] Executing target account operation...')
    self.human_jitter(45, 120)

    print(f'--- Completed Session Safely for: {self.username} ---\n')


if __name__ == '__main__':
  # --- Configuration & Fleet Execution ---
  account_fleet = [
      {
          'username': 'Account_Alpha_01',
          'proxy': 'socks5://user:pass@residential_proxy_1:port',
          'session': 'session_alpha.json',
      },
      {
          'username': 'Account_Beta_02',
          'proxy': 'socks5://user:pass@residential_proxy_2:port',
          'session': 'session_beta.json',
      },
  ]

  print('=== Starting Reddit Automation Fleet Manager ===')
  for acc in account_fleet:
    bot = RedditAutomationBot(acc['username'], acc['proxy'], acc['session'])
    bot.execute_task()

    # Stagger execution time between different accounts to prevent velocity spikes
    stagger_delay = random.randint(180, 360)
    print(
        f'[System] Staggering next account start by {stagger_delay} seconds...\n'
    )
    time.sleep(stagger_delay)
