# Si vous avez un probleme avec les biblioteques :  
# pip install matplotlib
# pip install numpy 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import heapq

grid_size = (50, 50)

# Coordonnées de départ et d'arrivée
start = (45, 8)  # Spawn
end = (17, 35)    # Drake

# Création de la grille (1 = accessible, 0 = obstacle)
grid = np.ones(grid_size)

minimap_image_path = "minimap.png"
try:
    minimap_img = mpimg.imread(minimap_image_path)
except FileNotFoundError:
    print(f"Erreur : l'image '{minimap_image_path}' est introuvable.")
    minimap_img = None

def interactive_display():
    fig, ax = plt.subplots(figsize=(8, 8))

    if minimap_img is not None:
        ax.imshow(minimap_img, extent=[0, grid.shape[1], 0, grid.shape[0]], origin='upper')

    def on_click(event):
        if event.inaxes == ax:
            x, y = int(event.ydata), int(event.xdata)
            x = grid.shape[0] - 1 - x  # Inverser l'axe Y pour correspondre à la grille
            if 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]:
                grid[x, y] = 0 if grid[x, y] == 1 else 1
                color = 'black' if grid[x, y] == 0 else 'white'
                ax.add_patch(plt.Rectangle((y, grid.shape[0] - 1 - x), 1, 1, color=color, alpha=0.5))
                fig.canvas.draw()

    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            color = 'white' if grid[x, y] == 1 else 'black'
            ax.add_patch(plt.Rectangle((y, grid.shape[0] - 1 - x), 1, 1, color=color, alpha=0.5))

    ax.add_patch(plt.Rectangle((start[1], grid.shape[0] - 1 - start[0]), 1, 1, color='yellow'))
    ax.add_patch(plt.Rectangle((end[1], grid.shape[0] - 1 - end[0]), 1, 1, color='red'))

    ax.set_xlim(0, grid.shape[1])
    ax.set_ylim(0, grid.shape[0])
    ax.set_aspect('equal')
    ax.set_xticks(range(grid.shape[1]))
    ax.set_yticks(range(grid.shape[0]))
    ax.grid(True)

    fig.canvas.mpl_connect('button_press_event', on_click)

    from matplotlib.widgets import Button

    def run_dijkstra(event):
        visited_nodes, optimal_path = dijkstra(grid, start, end)
        display_grid(grid, path=optimal_path, visited=visited_nodes)

    ax_button = plt.axes([0.8, 0.01, 0.1, 0.05])
    button = Button(ax_button, 'Lancer')
    button.on_clicked(run_dijkstra)

    plt.show()

def display_grid(grid, path=None, visited=None):
    plt.figure(figsize=(8, 8))

    if minimap_img is not None:
        plt.imshow(minimap_img, extent=[0, grid.shape[1], 0, grid.shape[0]], origin='upper')

    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            color = 'white' if grid[x, y] == 1 else 'black'
            plt.gca().add_patch(plt.Rectangle((y, grid.shape[0] - 1 - x), 1, 1, color=color, alpha=0.5))

    if visited is not None:
        for node in visited:
            plt.gca().add_patch(plt.Rectangle((node[1], grid.shape[0] - 1 - node[0]), 1, 1, color='blue', alpha=0.3))

    if path is not None:
        for node in path:
            plt.gca().add_patch(plt.Rectangle((node[1], grid.shape[0] - 1 - node[0]), 1, 1, color='green', alpha=0.5))

    plt.gca().add_patch(plt.Rectangle((start[1], grid.shape[0] - 1 - start[0]), 1, 1, color='yellow'))
    plt.gca().add_patch(plt.Rectangle((end[1], grid.shape[0] - 1 - end[0]), 1, 1, color='red'))

    plt.xlim(0, grid.shape[1])
    plt.ylim(0, grid.shape[0])
    plt.gca().set_aspect('equal')
    plt.xticks(range(grid.shape[1]))
    plt.yticks(range(grid.shape[0]))
    plt.grid(True)
    plt.show()

def dijkstra(grid, start, end):
    visited = []  # Liste des nœuds visités (pour visualisation)
    path = []     # Chemin optimal (si trouvé)

    # Initialisation
    start_x, start_y = start
    end_x, end_y = end

    # Initialisation des distances
    distances = np.full(grid.shape, np.inf)
    distances[start_x, start_y] = 0

    # Initialisation de la file de priorité
    heap = [(0, start_x, start_y)]  # (distance, x, y)
    predecessors = {}  # Pour retracer le chemin

    while heap:
        current_dist, x, y = heapq.heappop(heap)

        # Si ce nœud a déjà été visité, on passe au suivant
        if (x, y) in visited:
            continue

        # Marquer le nœud comme visité
        visited.append((x, y))

        # Arrivée au drake
        if (x, y) == (end_x, end_y):
            break

        # Parcours des voisins
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            # Vérification que le voisin est dans les limites de la grille et accessible
            if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1] and grid[nx, ny] == 1:
                new_dist = current_dist + 1  # Chaque déplacement coûte 1

                if new_dist < distances[nx, ny]:
                    distances[nx, ny] = new_dist
                    heapq.heappush(heap, (new_dist, nx, ny))
                    predecessors[(nx, ny)] = (x, y)

    # Reconstruction du chemin
    current = end
    while current in predecessors:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()

    return visited, path
   