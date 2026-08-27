class Agent_MONITOR:
    def __init__(self):
        self.name = "MONITOR"
        self.role = "Telemetry / Temps Reel"
        self.status = "ONLINE"
    
    def run(self):
        print("[MONITOR] Lancement du Benchmark Z-CORE G7...")
        import subprocess
        subprocess.run(["python", "scripts/benchmark_g7_monitor.py"])
        print("[MONITOR] Rapport Telemetry termine")

agent = Agent_MONITOR()
print(f"[{agent.name}] Charge - Role: {agent.role}")
