import chardet

some_string = '陈秉祺' #.encode('utf-8') # encode方法返回一个bytes
# b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe4\xb8\x96\xe7\x95\x8c\xe3\x80\x82'

result = chardet.detect(some_string) # 调用检测接口

print(result)
# {'encoding': 'utf-8', 'confidence': 0.99}
