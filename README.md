# SPQ Scheduler Simulation

Implémentation simple de **Strict Priority Queuing (SPQ)** en Python.  
Ce projet montre comment les paquets IP sont servis en fonction de leur priorité.

## 🚀 Fonctionnement
- Trois files d’attente : Q0 (haute priorité), Q1, Q2 (basse priorité).
- Les paquets arrivent avec une priorité aléatoire.
- L’ordonnancement SPQ sert toujours d’abord Q0, puis Q1, puis Q2.

## 📊 Résultats
Quand tu pousses du code :
1. GitHub Actions exécute `src/spq.py`.
2. Les résultats sont générés dans `results/` :
   - `log.txt` → journal des événements.
   - `graph.png` → graphique de l’ordonnancement.
3. Les fichiers sont disponibles dans **Artifacts** de GitHub Actions.

## ▶️ Lancer en local
```bash
pip install -r requirements.txt
python src/spq.py
