import random


class BehaviorEngine:

  def __init__(self, username):
    self.username = username

  def human_jitter(self, page, min_seconds=3, max_seconds=7):
    wait_time = random.uniform(min_seconds, max_seconds)
    print(
        f"[BehaviorEngine] ({self.username}) Pausing for {wait_time:.2f}s"
        " (Jitter active)..."
    )
    page.wait_for_timeout(wait_time * 1000)

  def simulate_scroll_and_read(self, page):
    print(
        f"[BehaviorEngine] ({self.username}) Simulating organic feed scrolling..."
    )
    try:
      for _ in range(3):
        scroll_amount = random.randint(300, 700)
        page.evaluate(f"window.scrollBy(0, {scroll_amount});")
        self.human_jitter(page, 2, 5)
    except Exception as e:
      print(f"[BehaviorEngine] Scroll simulation error: {e}")
      
