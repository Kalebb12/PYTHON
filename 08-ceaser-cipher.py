alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(start_text, shift_amount, cipher_direction):
  if shift_amount > 26:
    shift_amount = shift_amount % 26
  end_text = ""
  for letter in start_text:
    if letter not in alphabet:
      end_text += letter
      continue
    position = alphabet.index(letter)
    if cipher_direction == "encode":
      new_position = position + shift_amount
    elif cipher_direction == "decode":
      new_position = position - shift_amount
    if new_position >= len(alphabet):
      new_position = new_position - len(alphabet)
    elif new_position < 0:
      new_position = len(alphabet) + new_position
    end_text += alphabet[new_position]
  print(f"The {cipher_direction}d text is {end_text}")

ceasar(start_text=text, shift_amount=shift, cipher_direction=direction)