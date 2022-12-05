text = input('Введите текст: ')
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
 
print(sorted([i for i in text.split() if i not in punctuations], key = len)[0])
