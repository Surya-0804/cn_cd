def charStuff(flagbyte, escbyte, payload):
    x = payload.replace(escbyte, escbyte * 2)  # Escaping escape bytes
    y = x.replace(flagbyte, escbyte + flagbyte)  # Escaping flag bytes
    return flagbyte + y + flagbyte  # Adding flag bytes at the start and end

def charDestuff(flagbyte, escbyte, payload):
    x = payload.replace(escbyte + flagbyte, flagbyte)  # Unescaping flag bytes
    y = x.replace(escbyte * 2, escbyte)  # Unescaping escape bytes
    return y[1:-1]  # Removing the flag bytes from the start and end

# Example of usage
msg = input('Enter some message: ')
fb = input('Enter flag byte: ')
eb = input('Enter escape byte: ')

print('Original message:', msg)
stf = charStuff(fb, eb, msg)
print('Message after character stuffing:', stf)
dstf = charDestuff(fb, eb, stf)
print('Message after character destuffing:', dstf)

