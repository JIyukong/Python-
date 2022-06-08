from bwg_engine import BOWEngine
from search_engine import SimpleEngine


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

    bow = BOWEngine()
    main(bow)
