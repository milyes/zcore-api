from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import subprocess

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        if self.path == '/bench':
            # LANCEMENT AGENT MONITOR
            print("[AGENT MONITOR] Lancement Benchmark Z-CORE G7...")
            try:
                result = subprocess.run(
                    ["python", "scripts/benchmark_g7_monitor.py"],
                    capture_output=True,
                    text=True
                )
                data = {
                    "status": "BENCH_COMPLETE", 
                    "agent": "MONITOR",
                    "cycles": 50000, 
                    "mode": "NON-DEPENDANCE ZERO TRUST",
                    "cloud": False,
                    "logs": result.stdout
                }
            except Exception as e:
                data = {"status": "ERROR", "message": str(e)}
                
        else:
            # ENDPOINT RACINE
            data = {
                "status": "ZCORE_GENIE ONLINE", 
                "mode": "NON-DEPENDANCE ZERO TRUST", 
                "cloud": False,
                "version": "V10.6",
                "endpoints": ["/", "/bench"]
            }
        
        self.wfile.write(json.dumps(data, indent=2).encode())

print("[ZCORE_GENIE] API Locale lancée sur http://0.0.0.0:8000")
print("[AGENT MONITOR] Disponible sur /bench")
HTTPServer(('0.0.0.0', 8000), Handler).serve_forever()
