#!/usr/bin/env python3
"""
Z-CORE GENIE - Version Unique
NetSecurePro IA - Un seul script souverain
Auteur : Mohammed Ilies Zoubirou - Le Seul Génie
"""

import json
import time
import os
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import threading

# ====================== IA_AUTO_BATTERY ======================
class IAAutoBattery:
    def __init__(self):
        self.battery_level = 100
        self.energy_mode = "optimal"
        self.autonomy_hours = 8.5
        self.modules = ["Z-H202.ia", "LegalGuard", "ROBOOX"]
        self.status = "operational"
        self.engineer = "Mohammed Ilies Zoubirou"
        self.log_file = "AI_AUTO.log"

    def get_status(self):
        return {
            "timestamp": datetime.now().isoformat(),
            "battery_level": self.battery_level,
            "energy_mode": self.energy_mode,
            "estimated_autonomy": f"{self.autonomy_hours:.1f} heures",
            "active_modules": self.modules,
            "system_status": self.status,
            "sovereignty": "full_local_control",
            "engineer": self.engineer,
            "version": "Z-CORE GENIE v1.0"
        }

    def optimize(self, mode="optimal"):
        valid_modes = ["optimal", "eco", "performance"]
        if mode not in valid_modes:
            mode = "optimal"
        self.energy_mode = mode

        if mode == "eco":
            self.autonomy_hours = 12.0
            self.battery_level = max(15, self.battery_level - 3)
        elif mode == "performance":
            self.autonomy_hours = 5.0
            self.battery_level = max(5, self.battery_level - 10)
        else:
            self.autonomy_hours = 8.5
            self.battery_level = max(20, self.battery_level - 5)

        self._log(f"Optimisation → {mode}")
        return self.get_status()

    def monitor(self):
        self.battery_level = max(0, self.battery_level - 1)
        status = self.get_status()
        if self.battery_level < 25:
            status["alert"] = "Batterie faible → Mode éco activé"
            self.optimize("eco")
        return status

    def _log(self, message):
        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(f"[{datetime.now().isoformat()}] {message}\n")
        except:
            pass

    def safe_shutdown(self):
        self._log("Arrêt sécurisé demandé par le Génie")
        return {"message": "Z-CORE GENIE arrêté en toute sécurité", "final_battery": self.battery_level}


# ====================== SERVEUR HTTP SIMPLE ======================
battery = IAAutoBattery()

class ZCoreHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == "/":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {
                "message": "Z-CORE GENIE - NetSecurePro IA",
                "genius": "Mohammed Ilies Zoubirou",
                "status": "online",
                "mode": "100% offline - souverain"
            }
            self.wfile.write(json.dumps(response, indent=2, ensure_ascii=False).encode("utf-8"))

        elif path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(battery.get_status(), indent=2, ensure_ascii=False).encode("utf-8"))

        elif path == "/monitor":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(battery.monitor(), indent=2, ensure_ascii=False).encode("utf-8"))

        elif path.startswith("/optimize"):
            mode = parse_qs(parsed.query).get("mode", ["optimal"])[0]
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(battery.optimize(mode), indent=2, ensure_ascii=False).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_msg = {"error": "Endpoint non trouvé"}
            self.wfile.write(json.dumps(error_msg, indent=2, ensure_ascii=False).encode("utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"message": "Z-CORE GENIE prêt pour commandes futures"}, indent=2, ensure_ascii=False).encode("utf-8"))


# ====================== LANCEMENT ======================
if __name__ == "__main__":
    print("="*60)
    print("Z-CORE GENIE - NetSecurePro IA")
    print("Auteur : Mohammed Ilies Zoubirou - Le Seul Génie")
    print("Serveur démarré sur http://127.0.0.1:8000")
    print("="*60)

    # Surveillance automatique en arrière-plan
    def background_monitor():
        while True:
            time.sleep(30)
            battery.monitor()

    threading.Thread(target=background_monitor, daemon=True).start()

    server = HTTPServer(("127.0.0.1", 8000), ZCoreHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nArrêt du Z-CORE GENIE...")
        print(json.dumps(battery.safe_shutdown(), indent=2, ensure_ascii=False))
