import base64

# Replace 'your-service-account-key.json' with the path to your JSON key file
with open('D:\plugin_development\client_key_ee.json', 'rb') as key_file:
    key_data = key_file.read()

# Encode the key in base64
base64_key = base64.b64encode(key_data).decode('utf-8')

# Print or store the base64-encoded key
print(base64_key)
