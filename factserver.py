from flask import Flask, jsonify, request
app=Flask("Factorials...app")

@app.route('/facty', methods=['POST'])
def find_factorials():
   try:
      data = request.get_json()
      fact_n = data['num']
      fact = 1
      if fact_n >= 1:
         for i in range(1, fact_n+1):
            fact *= i
         return jsonify({"Factorial ":fact})
   except Exception as e:
      return jsonify({"Error... ":str(e)}), 500

if __name__=="__main__":
   app.run()
