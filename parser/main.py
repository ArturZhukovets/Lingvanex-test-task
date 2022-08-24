

def parse_words(path):
    """
    Парсим построчно для того, чтобы не занимать место в оперативной памяти.
    Имеется две валидации: в первом случае проверяем, что у каждого набора английских слов есть свой перевод.
    Во втором случае если одному английскому слову соответствует одно слово на русском - сразу добавляем их в файлы
    """
    with open(path, 'r', encoding='utf-8') as file_obj:
        for line in file_obj:
            line = line.replace("\n", '').split("\t")
            eng_words:list = line[0].strip().split(";")
            rus_words:list = line[1].strip().split(';')
            if len(line) != 2:
                continue
            if len(eng_words) == len(rus_words) == 1:
                writer_one_value('eng_words.txt', 'rus_words.txt', eng_words, rus_words)
            else:
                eng_writer('eng_words.txt', eng_words, rus_words)
                rus_writer('rus_words.txt', eng_words, rus_words)


def writer_one_value(path_eng, path_rus, eng_words:list, rus_words:list):
    """Функция записывает в файлы значения, когда одному слову соответствует одно слово с переводом"""
    try:
        with open(path_eng, 'a', encoding='utf-8') as f:
            f.write(eng_words[0]+'\n')
        with open(path_rus, 'a', encoding='utf-8') as f:
            f.write(rus_words[0]+'\n')
    except:
        print("Failed to spell this word")


def rus_writer(path, eng_words:list, rus_words:list):
    """Функция записывает русский перевод на каждое альтернативное английское слово"""
    try:
        with open(path, 'a', encoding='utf-8') as f:
            for i in range(len(eng_words)):
                for word in rus_words:
                    f.write(word.strip()+'\n')
    except:
        print("Failed to spell this word")



def eng_writer(path, eng_words:list, rus_words:list):
    """Функция записывает английское слово на каждый экземпляр русского слова."""
    try:
        with open(path, 'a', encoding='utf-8') as f:
            [f.write(word.strip()+"\n") for word in eng_words for i in range(len(rus_words))]
    except:
        print("Failed to spell this word")


if __name__ == '__main__':
    parse_words('content.txt')
