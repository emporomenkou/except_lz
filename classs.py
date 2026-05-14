import pandas as pd
from enum import Enum

b = 'var7.csv'
class Data():
    def __init__(self, a : str):
        try:
            self._df = pd.read_csv(a, sep=',')
        except FileNotFoundError as e:
            print(f"Возникла следующая ошибка: {str(e)}")
        except pd.errors.EmptyDataError:
            print(f"Возникла следующая ошибка: Датафрейм пуст")
        else:

            try:
                self._df = pd.read_csv(a, sep=',')                
                cols = ['Участники гражданского оборота',
                        'Тип операции',
                        'Сумма операции',
                        'Вид расчета',
                        'Место оплаты',
                        'Терминал оплаты',
                        'Дата оплаты',
                        'Время оплаты',
                        'Результат операции',
                        'Cash-back',
                        'Сумма cash-back']
                if list(self._df.columns) != cols:
                    raise ValueError(f"Названия стобцов не совпадают. \n Ожидаемые: {cols} \n Фактические: {list(self._df.columns)}")
                cols_type = {'Участники гражданского оборота' : 'str',
                             'Тип операции' : 'str',
                             'Сумма операции' : 'float64',
                             'Вид расчета' : 'str',
                             'Место оплаты' : 'str',
                             'Терминал оплаты' : 'str',
                             'Дата оплаты' : 'str',
                             'Время оплаты' : 'str',
                             'Результат операции' : 'str',
                             'Cash-back' : 'str',
                             'Сумма cash-back' : 'float64'}
                k = 0
                errors = []
                for c, type in cols_type.items():
                    if self._df[c].dtype != type:
                        k = 1
                        errors += [f"- В столбце '{c}' тип данных не соответствует ожидаемому. \n Ожидается: {cols_type[c]}, Фактически - {self._df[c].dtype} \n", ]
                if k == 1:
                    raise TypeError
            except ValueError as e:
                print(str(e))
            except TypeError :
                print(*(i for i in errors))
            else:
                self._df = pd.read_csv(a, sep=',')
                print("Датафрейм обработан успешно")          
def main():
    df = Data(b)
if __name__ == "__main__":
    main()
