from zeep import Client

# Create a Zeep client pointing to the SOAP service WSDL
client = Client('http://localhost:10000/?wsdl')

# Call the add_numbers method of the CalculatorService
result = client.service.add_numbers(5, 10)

print(f"Result from the SOAP service: {result}")  # Corrected the formatting for displaying the result
