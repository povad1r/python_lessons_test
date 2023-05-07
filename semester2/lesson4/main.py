from googletrans import Translator
import pandas as pd


# translator = Translator()
# file = open('semester2\\lesson4\\file.txt', 'w+')
# file.write('I won kahoot.\nOur teacher is the best.\n Today is the 7 May')
# file.seek(0)
# lines = file.readlines()
# file.close()

# a = translator.translate(lines, src='en', dest = 'uk')
# for trans in a:
#     print(trans.text)


translator = Translator()
data = pd.read_excel('semester2\lesson4\Grades.xlsx', usecols=['Subject', 'Task'])
to_translate = data
a = translator.translate(text=to_translate, src='en', dest='uk')
print(a.text)