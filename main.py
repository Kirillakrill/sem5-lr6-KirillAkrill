import requests
import json

# Создаем Мета Класс
class MetaSingleton(type):
    __instances = {} # Словарь, хранит экземпляр класс
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances: # Проверка объекта на наличие в словаре, при отсутствии добавляется в словарь
            cls.__instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class CurrenciesList(metaclass = MetaSingleton):

    def get_currencies(self, currencies_ids_lst = None):
        if currencies_ids_lst is None:

            currencies_ids_lst = [
                'R01239', 'R01235', 'R01035', 'R01815', 'R01585F', 'R01589',
                'R01625', 'R01670', 'R01700J', 'R01710A'
            ]

        cur_res_str = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")

        print(type(cur_res_str))
        result = {}
        

    
    
if __name__ == "__main__":
    c1 = CurrenciesList()
    c2 = CurrenciesList()
    print(id(c1))
    print(id(c2))
    print(type(CurrenciesList))
