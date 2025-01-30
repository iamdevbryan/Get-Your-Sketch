import cv2
import numpy as np

def generer_croquis(image_path, output_path="Static/images/croquis.png"):
    # Charger l'image et la convertir en niveaux de gris
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Appliquer un filtre bilatéral pour réduire le bruit tout en conservant les contours
    filtered = cv2.bilateralFilter(gray, 9, 75, 75)

    # Détecter les contours avec Canny
    edges = cv2.Canny(filtered, 50, 150)

    # Trouver les contours et les simplifier
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Créer une image blanche pour le croquis
    croquis = np.ones_like(image) * 255

    for contour in contours:
        # Approximations des contours pour obtenir des formes simples
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)

        # Dessiner les formes simplifiées sur le croquis
        cv2.drawContours(croquis, [approx], -1, (0, 0, 0), 2)

    # Enregistrer et afficher le croquis
    cv2.imwrite(output_path, croquis)

