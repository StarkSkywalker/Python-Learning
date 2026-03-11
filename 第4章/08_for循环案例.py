text = input('请输入要加密的文字：')
secret = ''
for t in text:
    secret += chr(ord(t)+1)
print(f'经过加密后的文字：{secret}')

secret = input('请输入要解密的文字：')
text = ''
for s in secret:
    text += chr(ord(s)-1)
print(f'经过解密后的文字：{text}')