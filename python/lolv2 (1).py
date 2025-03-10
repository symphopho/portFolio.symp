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

minimap_image_path = "minimap (1).png"
try:
    minimap_img = mpimg.imread(minimap (1)_image_path)
except FileNotFoundError:
    print(f"Erreur : l'image '{minimap (1)_image_path}' est introuvable.")
    minimap_img = None

def interactive_display():
    fig, ax = plt.subplots(figsize=(8, 8))

    if minimap_img is not None:
        ax.imshow(minimap (1)_img, extent=[0, grid.shape[1], 0, grid.shape[0]], origin='upper')

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
        plt.imshow(minimap (1)_img, extent=[0, grid.shape[1], 0, grid.shape[0]], origin='upper')

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
    """
    Implémentez ici l'algorithme de Dijkstra.
    - grid : matrice numpy représentant la grille (1 = accessible, 0 = obstacle).
    - start : tuple (x, y) représentant le point de départ.
    - end : tuple (x, y) représentant le point d'arrivée.
    Retour :
        - Une liste des nœuds visités.
        - Une liste du chemin optimal.
    """
    visited = []  # Liste des nœuds visités (pour visualisation)
    path = []     # Chemin optimal (si trouvé)

    # TODO: Implémentez Dijkstra ici

    return visited, path

interactive_display()
