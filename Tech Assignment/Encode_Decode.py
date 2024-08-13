def caesar_cipher_encode(message, shift):
    encoded_message = ""
    
    for char in message:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_position = (ord(char) - start + shift) % 26 + start
            encoded_message += chr(new_position)
        else:
            encoded_message += char
    
    return encoded_message

def caesar_cipher_decode(encoded_message, shift):
    return caesar_cipher_encode(encoded_message, -shift)

message = "Hello, World!"
shift = 3

encoded_message = caesar_cipher_encode(message, shift)
decoded_message = caesar_cipher_decode(encoded_message, shift)

print(f"Original Message: {message}")
print(f"Encoded Message: {encoded_message}")
print(f"Decoded Message: {decoded_message}")
