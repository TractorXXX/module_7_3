class WordsFinder:


    def __init__(self, *files):

        self.file_names = files


    def get_all_words(self):

        all_words = {}
        for n in self.file_names:
            with open(n, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                for m in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(m, '')
                words_list = text.split()
            all_words[n] = words_list
        return all_words


    def find(self, word):

        words = self.get_all_words()
        word = word.lower()
        words_dict = {}

        for n in self.file_names:
            words_list = words[n]
            if word in words_list:
                words_dict[n] = words_list.index(word) + 1
            else:
                words_dict[n]= f'Слова {word} в этом тексте нет'

        return words_dict


    def count(self, word):

        words = self.get_all_words()
        word = word.lower()
        words_dict = {}

        for n in self.file_names:
            words_list = words[n]
            if word in words_list:
                words_dict[n] = words_list.count(word)
            else:
                words_dict[n] = f'Слова {word} в этом тексте нет'

        return words_dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))

finder1 = WordsFinder('Rudyard Kipling - If.txt',)
print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))