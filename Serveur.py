import flask as fk
import cv2
import numpy as np
import projet
import os

app = fk.Flask(__name__)
app.config['UPLOAD_FOLDER'] = '.'
image_path = 'Static/images/croquis.png'


@app.route('/')
def home():
    if os.path.exists(image_path):
        os.remove(image_path)
        print(f"Le fichier {image_path} a été supprimé avec succès.")
    else:
        print(f"Le fichier {image_path} n'existe pas.")
    return fk.render_template('index.html')

@app.route('/traitement', methods=['POST'])
def traitement():
    image = fk.request.files['image']
    filename = 'sketch.png'  
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    # Sauvegarder l'image
    image.save(file_path)
    
    projet.generer_croquis('sketch.png')
    return fk.redirect('generated')

@app.route('/generated')
def generated():
    return fk.render_template('display.html')

    

if __name__ == '__main__':
    app.run(debug=True)