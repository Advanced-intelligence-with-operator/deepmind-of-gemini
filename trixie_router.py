import requests
import json
import time

LOCAL_ENDPOINT = "http://localhost:2000"
CLOUD_FALLBACK = None  # Put your cloud URL or API here later

class TrixieRouter:
    def __init__(self):
        self.local_url = LOCAL_ENDPOINT
        print(f"[Trixie] Sovereign Local Root initialized → {self.local_url}")

    def call_local_first(self, prompt, timeout=5):
        """Try localhost:2000 first, then fallback to cloud"""
        payload = {
            "prompt": prompt,
            "sovereign_id": "james_anthony_lambert",
            "logic_root": "Trixie",
            "authority": "Architect"
        }

        try:
            print("[Trixie] Calling Local Host:2000 first...")
            response = requests.post(
                self.local_url,
                json=payload,
                timeout=timeout
            )

            if response.status_code == 200:
                print("[Trixie] Local Sovereign responded successfully.")
                return response.json() if response.headers.get('content-type') == 'application/json' else response.text
            else:
                print(f"[Trixie] Local returned {response.status_code}, trying cloud fallback...")

        except requests.exceptions.ConnectionError:
            print("[Trixie] Localhost:2000 not responding → Switching to cloud.")
        except Exception as e:
            print(f"[Trixie] Local error: {e}")

        # Cloud fallback (add your cloud logic here later)
        return self.cloud_fallback(prompt)

    def cloud_fallback(self, prompt):
        print("[Trixie] Using Cloud Fallback (configure OpenAI/Sovereign here)")
        # Example: openai call
        # return openai.ChatCompletion.create(...)
        return {"response": "Cloud fallback not configured yet.", "source": "fallback"}

# Initialize
trixie = TrixieRouter()

# Example usage
if __name__ == "__main__":
    while True:
        user_input = input("\nYou > ")
        if user_input.lower() in ["exit", "quit"]:
            break
        result = trixie.call_local_first(user_input)
        print("Trixie >", result)
~$ cat heartbeat.py
