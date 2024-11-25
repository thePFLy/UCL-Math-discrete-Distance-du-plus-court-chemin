import numpy as np

def charger_matrice_csv(fichier: str) -> np.matrix:
    """
    Récupère la matrice csv et la convertir avec numpy.
    """
    C = np.genfromtxt(fichier, delimiter=',', dtype='float64', filling_values=np.inf)
    return C

def Dijkstra(C: np.matrix) -> np.matrix:
    """
    Algorithme de Dijkstra pour trouver les plus courts chemins entre toutes les paires de sommets.
    
    Paramètre:
        Matrice n x n des coûts d'un graphe pondéré, où C[i][j] est le coût de l'arête entre i et j. 
        
    Retourne:
        Une matrice n × n D contenant les distances des plus courts chemins entre toutes les paires de noeuds du graphe G.
    """
    
    # Nombre de sommets du graphe
    N = np.size(C, 0)
    # Initialiser la matrice des plus courts chemins avec l'infini
    D = np.full((N, N), np.inf)
    
    # Pour chaque sommet comme source
    for source in range(N):
        # Tableau des plus courts chemins
        dist_est = [[np.inf, False] for _ in range(N)]
        dist_est[source][0] = 0 
        dist_est[source][1] = True
        sommet_u = source
        dist_u = 0  # Distance initiale pour le sommet source
        
        # Nombre de sommets sélectionnés
        cpt = 1
        
        while cpt < N:
            minimum = np.inf  # Distance min à chaque itération
            
            # Relâchement (pour chaque sommet non visité)
            for k in range(N):
                if dist_est[k][1] == False:  # Si k n'a pas encore été sélectionné
                    dist_uv = C[sommet_u][k]  # Poids de l'arête (sommet_u, k)
                    dist_totale = dist_u + dist_uv  # Distance totale du chemin source -> ... -> u -> k
                    
                    # Mise à jour de la distance min pour k
                    if dist_totale < dist_est[k][0]:
                        dist_est[k][0] = dist_totale 
            
                    # Mise à jour de la solution min à cette étape
                    if dist_est[k][0] < minimum:
                        minimum = dist_est[k][0]
                        prochain_sommet_select = k  # Prochain sommet à sélectionner
            
            # Mise à jour du sommet sélectionné et de la distance
            sommet_u = prochain_sommet_select
            dist_est[sommet_u][1] = True  # Passer le sommet en True pour le marquer comme visité
            dist_u = dist_est[sommet_u][0]  # Mettre à jour la distance du sommet sélectionné
            
            cpt += 1  # Incrémenter le compteur des sommets sélectionnés
        
        # Stockage des distances minimales depuis le sommet source dans la matrice D.
        for i in range(N):
            D[source][i] = dist_est[i][0]
    
    return D

def Bellman_Ford(C: np.matrix) -> np.matrix:
    return

def Floyd_Warshall(C: np.matrix) -> np.matrix:
    return

def main():
    """
    Charger la matrice CSV, appliquer les algorithmes et afficher la matrice de cout et les résultats.
    """
    fichier = "graphe21.csv"
    # Convertir le csv en matrice np.array
    C = np.genfromtxt(fichier, delimiter=',', dtype='float64', filling_values=np.inf)
    C = np.where(C == "inf", np.inf, C).astype(float)
    
    print("Matrice des coûts :")
    print(C)
    
    D_dijkstra = Dijkstra(C)
    print("\nMatrice des plus courts chemins (Dijkstra) :")
    print(D_dijkstra)

    D_Bellman_ford = Bellman_Ford(C)
    print("\nMatrice des plus courts chemins (Bellman Ford) :")
    print(D_Bellman_ford)

    D_Floyd_Warshall = Floyd_Warshall(C)
    print("\nMatrice des plus courts chemins (Floyd Warshall) :")
    print(D_Floyd_Warshall)

# Appeler la fonction principale
if __name__ == "__main__":
    main()