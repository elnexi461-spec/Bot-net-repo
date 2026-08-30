import json
import os


class SessionManager:

  def __init__(self, username, session_file):
    self.username = username
    self.session_file = session_file

  def load_session(self):
    if os.path.exists(self.session_file):
      try:
        with open(self.session_file, "r") as f:
          print(f"[SessionManager] ({self.username}) Loaded active cookies.")
          return json.load(f)
      except Exception as e:
        print(f"[SessionManager] ({self.username}) Error loading session: {e}")
    print(f"[SessionManager] ({self.username}) No session found.")
    return None

  def save_session(self, cookie_data):
    try:
      with open(self.session_file, "w") as f:
        json.dump(cookie_data, f, indent=4)
      print(f"[SessionManager] ({self.username}) Session state saved.")
    except Exception as e:
      print(f"[SessionManager] ({self.username}) Failed to save session: {e}")
      
