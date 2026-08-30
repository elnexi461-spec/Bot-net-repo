import random
import time
from account_manager import AccountInstance
import json

# Load fleet configuration from config.json
with open("config.json", "r") as f:
  config_data = json.load(f)

ACCOUNT_FLEET = config_data.get("accounts", [])


def run_fleet_automation():
  print("=== Starting Multi-Account Reddit Automation Fleet ===")

  for config in ACCOUNT_FLEET:
    bot = AccountInstance(config)
    bot.initialize_instance()

    # Execution Staggering: Prevent artificial velocity spikes across accounts
    stagger_delay = random.randint(180, 300)
    print(
        f"[System] Staggering next account activation by {stagger_delay}"
        f" seconds...\n"
    )
    time.sleep(stagger_delay)

  print("=== Fleet Automation Run Completed Successfully ===")


if __name__ == "__main__":
  run_fleet_automation()
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
