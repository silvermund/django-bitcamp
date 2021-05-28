import pandas as pd


class Conversion(object):


    @staticmethod
    def create_tuple() -> ():
        return (1,2,3,4,5,6,7,8,9)

    @staticmethod
    def tuple_to_list(tp) -> []:
        return list(tp)

    @staticmethod
    def int_to_float(ls) -> []:
        return [float(i) for i in ls]

    @staticmethod
    def float_to_int(ls) -> []:
        return [int(i) for i in ls]

    @staticmethod
    def list_to_dictionary(ls) -> {}:
        return dict(zip([str(i) for i in ls], ls))

    @staticmethod
    def hello_to_tuple(st) ->():
        return tuple(list(st))

    @staticmethod
    def dictionary_to_dataframe(dt) -> object:
        return pd.DataFrame.from_dict(dt, orient='index')

    @staticmethod
    def main():
        c = Conversion()
        tp = ()
        ls = []
        while 1:
            m = input('0-exit 1-create tuple\n'
                      '2-convert list\n'
                      '3-convert float-list\n'
                      '4-convert int-list\n'
                      '5-list convert dictionary\n'
                      '6-str convert tuple\n'
                      '7-str tuple convert list\n'
                      '8-dictionary to dataframe')
            if m == '0':
                break
            elif m == '1':
                tp = c.create_tuple()
                print(f'tp의 타입 : {type(tp)}')
                print(tp)
            elif m == '2':
                ls = c.tuple_to_list(tp)
                print(f'ls의 타입 : {type(ls)}')
                print(ls)
            elif m == '3':
                ls = c.int_to_float(ls)
                print(f'ls의 타입 : {type(ls)}')
                print(ls)
            elif m == '4':
                ls = c.float_to_int(ls)
                print(f'ls의 타입 : {type(ls)}')
            elif m == '5':
                dt = c.list_to_dictionary(ls)
                print(f'dt의 타입 : {type(dt)}')
                print(dt)
            elif m == '6':
                tp = c.hello_to_tuple('hello')
                print(f'tp의 타입 : {type(tp)}')
                print(tp)
            elif m == '7':
                ls = c.tuple_to_list(tp)
                print(f'ls의 타입 : {type(ls)}')
                print(ls)
            elif m == '8':
                tp = c.create_tuple()
                ls = c.tuple_to_list(tp)
                dt = c.list_to_dictionary(ls)
                print(dt)
                df = c.dictionary_to_dataframe(dt)
                print(f'df의 타입 : {type(df)}')
                print(df)

            else:
                continue

Conversion.main()
