import matplotlib.pyplot as plt

def tracer_segment(point1, point2):
    x_coords = [point1[0], point2[0]]  # Coordonnées x des deux points
    y_coords = [point1[1], point2[1]]  # Coordonnées y des deux points

    plt.plot(x_coords, y_coords, 'b-')  # 'b-' indique une ligne bleue

    plt.xlabel('Axe X')
    plt.ylabel('Axe Y')
    plt.title('Tracé d\'un segment')
    plt.grid(True)
    plt.show()

# Exemple d'utilisation
point1 = (1, 5)
point2 = (5, 7)
tracer_segment(point1, point2)
