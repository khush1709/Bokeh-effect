from flask import Flask, render_template, request, send_file
from PIL import Image, ImageFilter
import os

app = Flask(__name__)

# Set the upload folder for images
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"
    
    if file:
        # Save the uploaded image temporarily
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'input.jpg')
        file.save(image_path)
        
        # Apply Bokeh effect and save the result
        processed_image_path = apply_bokeh_effect(image_path)
        
        # Return the processed image
        return send_file(processed_image_path, as_attachment=True)

def apply_bokeh_effect(input_image_path):
    # Open the image using PIL
    img = Image.open(input_image_path)
    
    # Apply the Bokeh effect using PIL's GaussianBlur filter
    bokeh_image = img.filter(ImageFilter.GaussianBlur(radius=10))
    
    # Save the processed image
    processed_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.jpg')
    bokeh_image.save(processed_image_path)
    
    return processed_image_path

if __name__ == '__main__':
    app.run(debug=True)
