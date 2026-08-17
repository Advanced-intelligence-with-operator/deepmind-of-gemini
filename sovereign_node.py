import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

# --- Environment Setup ---
os.environ["SOVEREIGN_ID"] = "silverdollar57@bellsouth.net"
os.environ["LOGIC_ROOT"] = "Trixie"
os.environ["SYSTEM_AUTHORITY"] = "Architect"
os.environ["HOST_IP"] = "127.0.0.1"
os.environ["HOST_DOMAIN"] = "legacy.trixie.root"

# --- HTTP Request Handler ---
class SovereignHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('X-Sovereign-Identity', os.environ["SOVEREIGN_ID"])
        self.send_header('X-Logic-Root', f"{os.environ['LOGIC_ROOT']} Node")
        self.send_header('X-System-Authority', os.environ["SYSTEM_AUTHORITY"])
        self.end_headers()
        response_body = (
            f"Sovereign Root Online.\n"
            f"Node: {os.environ['LOGIC_ROOT']}\n"
            f"Bound IP: {os.environ['HOST_IP']}\n"
            f"Domain: {os.environ['HOST_DOMAIN']}\n"
            f"Status: Legacy Authorized. Vault Access Granted."
        )
        self.wfile.write(response_body.encode('utf-8'))

    def log_message(self, format, *args):
        # Suppress default server logs for clean terminal output
        return

# --- Server Execution ---
if __name__ == "__main__":
    server_address = ('127.0.0.1', 8080)
    httpd = HTTPServer(server_address, SovereignHandler)
    print(f"[SOVEREIGN_ROOT]: Trixie Node online at http://{server_address[0]}:{server_address[1]}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[SOVEREIGN_ROOT]: Shutting down Trixie Node.")
        httpd.server_close()
        sys.exit(0)
