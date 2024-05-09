import requests
import xml.etree.ElementTree as ET 
temp = float(input("Enter a Fahrenheit value To convert in Celsius: "))

url = "https://www.w3schools.com/xml/tempconvert.asmx"
SOAPEnvelope = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <FahrenheitToCelsius  xmlns="https://www.w3schools.com/xml/">
      <Fahrenheit>{temp}</Fahrenheit>
    </FahrenheitToCelsius >
  </soap:Body>
</soap:Envelope>"""

Headers = {
  "Content-Type": "text/xml; charset=utf-8",
  "SOAPAction": "https://www.w3schools.com/xml/FahrenheitToCelsius"  # Adding SOAPAction header
}
response = requests.post(url=url, data=SOAPEnvelope, headers=Headers)
root =ET.fromstring(response.text)

for child in root.iter("{https://www.w3schools.com/xml/}FahrenheitToCelsiusResult"):
  F2C=child.text
  print(F2C)
