from zeep import Client

# Create a Zeep client pointing to the SOAP service WSDL
client = Client('http://localhost:10000/?wsdl')
#or client = Client("http://127.0.0.1:7567/?wsdl")
result_add = client.service.add_numbers(5, 10)
result_sub = client.service.sub_numbers(5, 10)
result_mul = client.service.mul_numbers(5, 10)
print(f"Adding number: {result_add}")
print(f"Subtracting number: {result_sub}")
print(f"Multiplying number: {result_mul}")
#print(f"Result from the SOAP service: {result}") 
