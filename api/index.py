from http.server import BaseHTTPRequestHandler
import json
import urllib.request
import re

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        try:
            # Cricbuzz se data lana
            url = "https://www.cricbuzz.com/cricket-match/live-scores"
            headers = {'User-Agent': 'Mozilla/5.0'}
            req = urllib.request.Request(url, headers=headers)
            
            with urllib.request.urlopen(req) as response:
                html = response.read().decode('utf-8')

            # Score dhundna
            match = re.search(r'<title>(.*?)</title>', html)
            if match:
                clean_score = match.group(1).split('|')[0].strip()
                msg = clean_score
            else:
                msg = "Match shuru nahi hua."

            data = {
                "status": "success",
                "score": msg,
                "credit": "Mankibuzz API"
            }

        except Exception as e:
            data = {"status": "error", "message": str(e)}

        self.wfile.write(json.dumps(data).encode('utf-8'))
        return
