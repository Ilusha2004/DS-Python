# Дана строка символов, среди которых есть одна
# открывающаяся и одна закрывающаяся скобки. Вывести на экран все
# символы, расположенные внутри этих скобок
def removeScopes(string: str):
     return ")".join(string.split("(", 1)[1].split(")")[:-1])

print(removeScopes("test(SymbolsInSide)hkjhk)dfs)fdssd)enjoy"))

# Пользователь вводит текст. На основе этого текста создается
# словарь. Ключами словаря служат символы из текста, а значениями
# элементов словаря являются количества вхождений соответствующих
# символов в текст. Например, если пользователь вводит текст "ABBCAB", то
# словарь будет состоять из трех элементов с ключами "A", "B" и "C", а
# значения элементов соответственно равны 2 (в тексте 2 буквы "A"), 3 (в
# тексте 3 буквы "B") и 1 (в тексте 1 буква "C").
def dictionaryCounter(string: str):
     dictionary = dict()
     for sym in list(string):
          if dictionary.get(sym) is None:
               dictionary[sym] = 1
          else:
               dictionary[sym] = dictionary.get(sym) + 1

     return dictionary

# Напишите программу, в которой на основе текста,
# введенного пользователем, создается новый текст. По сравнению с исходным
# в нем слова расположены в обратном порядке
def reverseSentenses(string: str):
     temp = string.split(" ")
     return  " ".join([temp[len(temp) - i - 1] for i in range(len(temp))])

print(reverseSentenses("creates an array whose initial content is random"))

# if __name__ == "__main__":
#      input = str(input())
#      print(dictionaryCounter(input))