import json
import os
from datetime import datetime
from http.server import BaseHTTPRequestHandler

TEAM_DB = [
    {
        "id": 1,
        "name": "Anant Chaudhary",
        "position": "President",
        "description": "Visionary leader | Market analysis expert",
        "email": "anant@accclub.com",
    },
    {
        "id": 2,
        "name": "Mohit Raj",
        "position": "Finance Head",
        "description": "Financial strategist | Budget specialist",
        "email": "mohit@accclub.com",
    },
]

PROJECTS_DB = [
    {
        "id": 1,
        "name": "Market Analysis 2024",
        "description": "Comprehensive analysis of market trends",
        "category": "Finance",
        "status": "In Progress",
        "team_lead": "Mohit Raj",
    }
]

REGISTRATIONS_DB = []


class handler(BaseHTTPRequestHandler):
    def _send_json(self, payload, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode("utf-8"))

    def _send_html(self, html, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            try:
                root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
                index_file = os.path.join(root_dir, "index.html")
                with open(index_file, "r", encoding="utf-8") as f:
                    self._send_html(f.read())
                return
            except Exception:
                self._send_json(
                    {
                        "success": False,
                        "message": "Homepage not found",
                        "time": datetime.utcnow().isoformat(),
                    },
                    status=500,
                )
                return

        if self.path == "/health":
            self._send_json({"status": "healthy", "service": "acc-club-api"})
            return

        if self.path == "/api/team":
            self._send_json({"success": True, "data": TEAM_DB, "count": len(TEAM_DB)})
            return

        if self.path == "/api/projects":
            self._send_json({"success": True, "data": PROJECTS_DB, "count": len(PROJECTS_DB)})
            return

        if self.path == "/api/registrations":
            self._send_json({"success": True, "data": REGISTRATIONS_DB, "count": len(REGISTRATIONS_DB)})
            return

        self._send_json({"success": False, "message": "Not found"}, status=404)

    def do_POST(self):
        if self.path != "/api/registrations":
            self._send_json({"success": False, "message": "Not found"}, status=404)
            return

        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode("utf-8") if content_length > 0 else "{}"

        try:
            payload = json.loads(body) if body else {}
        except json.JSONDecodeError:
            self._send_json({"success": False, "message": "Invalid JSON"}, status=400)
            return

        item = {
            "id": len(REGISTRATIONS_DB) + 1,
            **payload,
            "status": "pending",
            "created_at": datetime.utcnow().isoformat(),
        }
        REGISTRATIONS_DB.append(item)

        self._send_json(
            {"success": True, "message": "Registration submitted", "data": item},
            status=201,
        )
