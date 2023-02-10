# import words from linux dictionary
dicts = []
with open('/usr/share/dict/words') as f:
    dicts = f.readlines()
    
    
class Item:
    def __init__(self, word, point, key):
        self.word = word
        self.point = point
        self.key = key
        

def is_charachter(ch):
    return ch.upper() != ch.lower()


def caesar(word, key=3):
    if key < 0:
        key += 26
    if key > 26:
        key = key % 26
        
    encrypted = ''
    A = ord('A')
    
    for ch in word.upper():
        if is_charachter(ch):
            code = ord(ch) - A
            encrypted += chr(((code + key)%26)+A)
        else:
            encrypted += ch
            
    return encrypted

def in_dict(word):
    if word.lower()+"\n" in dicts:
        return True

def decrypt(words):
    result = []
    
    for i in range(25):
        decrypted = caesar(words, i)
        sentense = decrypted.split(' ')
        point = 0
        for word in sentense:
            if in_dict(word):
                point+=1000 + len(word)
                
        result.append( Item(decrypted, point, 26 - i))
        
    return result
            
        
            
result = decrypt(caesar("This is a very cool message", 17))
#or result = decrypt('KYZJ ZJ R MVIP TFFC DVJJRXV')


#return top 10 result
for item in sorted(result, key=lambda x: x.point, reverse=True )[:10]:
    print( "Message: ", item.word ,  " => Point: ",item.point," => Key{1..25}: " , item.key)

# OUTPUT
# >> Message:  THIS IS A VERY COOL MESSAGE  => Point:  6022  => Key{1..25}:  17
```PYTHON
