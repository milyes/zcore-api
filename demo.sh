#!/bin/bash
echo "[DEMO] Lancement NetSecurePro v10.3"
python3 ZCORE_GENIE.py &
sleep 1
python3 AI_AUTO.py "Scan Complet Système"
echo "[DEMO] Terminé. Preuve Airgap."
