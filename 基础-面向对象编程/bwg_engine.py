from search_engine import SearchEngineBase
import re


class BOWEngine(SearchEngineBase):

    def __init__(self):
        super(BOWEngine, self).__init__()
        self.__id_to_words = {}

    def process_corpus(self, index, text):
        self.__id_to_words[index] = self.parse_text_to_words(text)

    def search(self, query):
        query_words = self.parse_text_to_words(query)
        print(query_words)
        results = []
        for index, words in self.__id_to_words.items():
            if self.query_match(query_words, words):
                results.append(index)
        return results

    @ staticmethod
    def parse_text_to_words(text):
        """输入文本内容,去除标点符号,生成单词列表,并将单词set"""

        # 将标点符号替换成空格
        text = re.sub(r'[^\w]', ' ', text)
        # 转为小写
        lower_text = text.lower()
        # 将所有单词转为列表
        list_text = lower_text.split(sep=' ')
        # 将列表去重
        list_unique_text = set(list_text)
        # 删除空白项
        word_list = list(filter(None, list_unique_text))

        return word_list

    @staticmethod
    def query_match(query_words, words):
        for query_word in query_words:
            if query_word not in words:
                return False
        return True


if __name__ == '__main__':
    test = ' i have dream'
    tests = 'i have a great dream'
    search_engine = BOWEngine()
    search_engine.parse_text_to_words(test)



