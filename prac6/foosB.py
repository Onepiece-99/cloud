from flask import Flask, request, jsonify

app=Flask("PaaS")
Platform_sw = []

@app.route('/create_app', methods=['POST'])
def create_App():
   try:
      data = request.get_json()
      provider = 'Dee codig'
      name = data.get('app name')
      types = data.get('types')

      if not all([name, types]):
         raise ValueError("Name & types must be given")

      VM_sw = {
         "Provider":provider,
         "S/W Name":name,
         "Types of S/W":types
      }
      Platform_sw.append(VM_sw)
      return jsonify({"Msg ":"Successfully created a s/w...", "Details":VM_sw})
   except Exception as e:
      return jsonify({"Error...":str(e)}),400

@app.route('/lists', methods=['GET'])
def lists_app():
   return jsonify(Platform_sw)

if __name__=="__main__":
   app.run(debug=True, port=8573)
