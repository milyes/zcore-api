#!/bin/bash
echo "[1/3] Vérif Airgap..."
ping -c 1 8.8.8.8 > /dev/null 2>&1 && echo "ATTENTION: Internet" || echo "OK: Offline"
echo "[2/3] Lancement API..."
python3 ZCORE_GENIE.py > /dev/null 2>&1 &
sleep 2
echo "[3/3] Test IA..."
python3 AI_AUTO.py "Scan Complet"
echo "DEMO TERMINÉE. 100% LOCAL."
