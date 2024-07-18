alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q'
          'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encryption(plain_text, shift_key):
    for char in plain_text:
        position=alphabet.index(char)


what_to_do = input("Type 'encrypt' for encryption, type 'decrypt' for decryption")
text = input("Type your message:\n")
shift=int(input("Enter shift key:\n"))

if what_to_do == "encrypt":
    encryption(plain_text=text, shift_key=shift)
elif what_to_do == "decrypt":
    decryption(text, shift, )