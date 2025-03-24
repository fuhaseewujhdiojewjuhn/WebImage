import os
from flask import Flask, render_template, request, jsonify
from PIL import Image, ImageEnhance, ImageDraw, ImageFont
 
app = Flask(__name__)
 
UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
 
def process_image(image_path, operation, *args):
    img = Image.open(image_path).convert("RGB")
   
    if operation == 'resize':
        width, height = map(int, args)
        img = img.resize((width, height))
    elif operation == 'rotate':
        angle = int(args[0])
        img = img.rotate(angle)
    elif operation == 'brightness':
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(float(args[0]))
    elif operation == 'contrast':
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(float(args[0]))
    elif operation == 'text':
        text = args[0]
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("arial.ttf", 20)
        except:
            font = ImageFont.load_default()
        draw.text((10, 10), text, font=font, fill="white")
   
    return img
 
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
   
    img_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(img_path)
 
    return render_template('editor.html', image_url=file.filename)
 
@app.route('/edit', methods=['POST'])
def edit_image():
    image_filename = request.form['image_path']
    operation = request.form['operation']
    args = request.form.getlist('args[]')
   
    original_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
    base_name, ext = os.path.splitext(image_filename)
    edited_filename = f'edited_{base_name[:10]}{ext}'
    edited_path = os.path.join(app.config['UPLOAD_FOLDER'], edited_filename)
   
    # Se a imagem já foi editada antes, use a versão editada como base
    image_path = edited_path if os.path.exists(edited_path) else original_path
   
    img = process_image(image_path, operation, *args)
    img.save(edited_path)
   
    # Remove versões antigas da imagem editada para economizar espaço
    if 'edited_' in image_filename and os.path.exists(original_path):
        os.remove(original_path)
   
    return jsonify({'image': edited_filename})
 
if __name__ == '__main__':
    app.run(debug=True)