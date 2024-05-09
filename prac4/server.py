
from flask import Flask, request, send_file, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST','PUT'])
def upload_file():
   try:
      file = request.files['file']

      file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
      file.save(file_path)
      return 'File uploaded successfully'
             #jsonify({"Msg ": f"Files uploaded {file} successfully...!"})
   except Exception as e:
      return str(e), 500
            #jsonify({"up Error ":str(e)}), 500
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
   #try:
   file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

   if os.path.exists(file_path):
      return send_file(file_path, as_attachment=True)
   else:
      return 'File not found', 404
            #jsonify({"Error ": "File not found"}), 404
   # except Exception as e:
     # return jsonify({"Down Error... ": str(e)}), 400
if __name__ == '__main__':
   app.run(debug=True)#(debug=True, port=9048)

