import queue
import random
import matplotlib.pyplot as plt
import os

# S'assurer que le dossier results existe
os.makedirs("results", exist_ok=True)

# Créer 3 files de priorité (0 = haute, 2 = basse)
queues = [queue.Queue() for _ in range(3)]
log = []

class Packet:
    def __init__(self, pid, priority):
        self.pid = pid
        self.priority = priority

# Génération de 20 paquets avec priorités aléatoires
for i in range(20):
    p = Packet(i, random.choice([0, 1, 2]))
    queues[p.priority].put(p)
    log.append(f"Arrivée paquet {p.pid} dans Q{p.priority}")

# Ordonnancement SPQ
served = []
while any(not q.empty() for q in queues):
    for prio, q in enumerate(queues):
        if not q.empty():
            pkt = q.get()
            served.append((pkt.pid, prio))
            log.append(f"Servi paquet {pkt.pid} de priorité Q{prio}")
            break

# Sauvegarde du log
with open("results/log.txt", "w") as f:
    f.write("\n".join(log))

# Graphe des paquets servis
priorities = [p[1] for p in served]
plt.plot(priorities, marker="o")
plt.title("Ordonnancement SPQ")
plt.xlabel("Ordre de service")
plt.ylabel("Priorité")
plt.savefig("results/graph.png")

print("✅ Simulation SPQ terminée. Résultats dans /results/")
