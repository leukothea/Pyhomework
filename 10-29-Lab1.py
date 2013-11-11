import codecs

f = codecs.open('text.utf16', encoding='utf-16')
selection = f.read()

print selection

for line in f:
    print repr(line)

f = codecs.open('text.utf32', encoding='utf-32')
for line in f:
    print repr(line)

