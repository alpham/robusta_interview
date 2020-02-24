from string import ascii_lowercase, ascii_uppercase

# it's the same thing here, but I'm just dealing with abstract variables.
LEN_UPPER = len(ascii_uppercase)
LEN_LOWER = len(ascii_lowercase)
SHIFT = 3

def _convert(char, ascii_):
  ochar = ord(char)
  if ord(char) in [ord(i) for i in ascii_[SHIFT*-1:]]:
    return ascii_[SHIFT + (ochar - ord(ascii_[-1])) - 1]
  return chr((ord(char) + SHIFT) % (LEN_LOWER + ord(ascii_[0])))


def run(text):
  result = ""
  # transverse the plain text
  for char in text:
    if char in (ascii_lowercase + ascii_uppercase):
      # Encrypt uppercase characters in plain text
      if (char.isupper()):
        result += _convert(char, ascii_uppercase)
      # Encrypt lowercase characters in plain text
      else:
        result += _convert(char, ascii_lowercase)
    else:
      result += char
  return result
