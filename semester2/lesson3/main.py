from googletrans import Translator

translator = Translator()
to_translate = '私たちは皆、宿題に 10 点満点を求めています'
a = translator.translate(text=to_translate, src='ja', dest='uk')
c = translator.translate(text=to_translate, src='ja', dest='zh-cn')
b = translator.translate(text=to_translate, dest='de')
print(f'{a.text}, {b.text}, {c.text}')

