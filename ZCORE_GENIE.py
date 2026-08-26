from http.server import HTTPServer, BaseHTTPRequestHandler
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(b'{"status": "ZCORE_GENIE ONLINE", "mode": "NON-DEPENDANCE ZERO TRUST", "cloud": false}')
print("[ZCORE_GENIE] API Locale lancée sur http://localhost:8000")
HTTPServer(('0.0.0.0', 8000), Handler).serve_forever()
