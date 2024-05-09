
from flask import Flask, request, jsonify

app = Flask(__name__)

new_application=[]

@app.route('/create_application', methods=['POST'])
def create_application():

   try:
      data = request.get_json()
      app_name = data.get('app_name')
      app_type = data.get('app_type')
      
      if not all([app_name, app_type]):
         raise ValueError("Invalid data, App name and app type required.")

      new_application.append(new_application)

      return jsonify({"message": "Application created successfully", "application":new_application})

   except Exception as e:
      return jsonify({"error": str(e)}), 400

@app.route('/list_application', methods=['GET'])
def list_application():
   return jsonify({"application": new_application})

if __name__ == '__main__':
   app.run(debug=True)
