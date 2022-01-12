import sqlite3
import typing


class QueryHandler:
    """
    Класс инструмента для взаимодействия с базой данных
    """
    db_link: str

    def __init__(self, db_link):
        self.con = sqlite3.connect(db_link)
        self.cur = self.con.cursor()

    def query(self, sys_from: str, sys_to: str, category: str) -> typing.List[str]:
        """
        Функция, переводящая количество УВ из одной кассификации в другую

        :param sys_from: исходная классификация
        :param sys_to: классификация, в которую необходимо перевести данные из исходной
        :param category: категория в исходной классификации
        :return: результат перевода
        """
        if sys_from == sys_to:
            return [category]
        s1, s2 = '"%' + category + '%"', '"%' + category + '*%"'

        query = 'select distinct ' + sys_to + ' from categories where ' + sys_from + ' like ' + s1 + \
                ' and ' + sys_from + ' not like ' + s2

        res = [val[0] for val in self.cur.execute(query).fetchall()]
        return res
