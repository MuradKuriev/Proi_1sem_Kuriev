magnit = {'молоко','соль', 'сахар', 'печенья','сыр'}
pyaterochka = {'мясо', 'молоко','сыр'}
perekrestok = {'молоко', 'творог', 'сыр','сахар','печенья'}
lenta = {'печенья', 'молоко', 'сыр', 'сметана'}

stores = {'magnit':['молоко','соль', 'сахар', 'печенья','сыр'],
          'pyaterochka':['мясо', 'молоко','сыр'],
          'perekrestok':['молоко', 'творог', 'сыр','сахар','печенья'],
          'lenta':['печенья', 'молоко', 'сыр', 'сметана'],}
total = set()
for i in stores:
    if 'сметана' not in stores [i]:
        total.add(i)
print('Нельзя купить сметану в этих магазинах :' , *total)
print(' товары из магазина Магнит отсутствуют в магазине Перекресток :',*(magnit - perekrestok))
print(' товары из магазина Лента отсутствуют в магазине Магнит :',*(lenta - magnit))
