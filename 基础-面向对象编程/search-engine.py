class SearchEngineBase:
    def __init__(self):
        pass

    def add_corpus(self, file_path):
        with open(file_path, 'r') as file:
            text_content = file.read()
        self.process_corpus(file_path, text_content)

    def process_corpus(self, index, text_content):
        raise Exception('process_corpus not implemented.')

    def search(self):
        raise Exception('search not implemented.')


class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super().__init__()
        self.__index_to_texts = {}

    def process_corpus(self, index, text_content):
        self.__index_to_texts[index] = text_content

    def search(self, query):
        results = []
        for index, text_content in self.__index_to_texts.items():
            if query in text_content:
                results.append(index)
        return results


def main(engine):
    #  迭代读取每个txt文本内容，文件相对路径为key, 文本内容为value，存储于字典容器
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        engine.add_corpus(file_path)

    #  无限循环搜索每一个容器
    while True:
        query = input()
        results = engine.search(query)
        print('found {} result(s):'.format(len(results)))
        for result in results:
            print(result)


if __name__ == '__main__':
    search_engine = SimpleEngine()
    main(search_engine)
