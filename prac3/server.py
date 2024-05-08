from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_currency():
   try:
      data = request.json
      amount_in_rs = data['amount_in_rs']
      conversion_rate = 0.012  # Replace with the actual conversion rate

      amount_in_usd = amount_in_rs * conversion_rate
      return jsonify({'amount_in_usd': format(amount_in_usd, '.4f')})

   except Exception as e:
      return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
   app.run(debug=True)
