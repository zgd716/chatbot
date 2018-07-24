import re
class RuleBaseExtrator(object):
    def __init__(self):
        self.__coffee_type=['拿铁','美式','摩卡']
        self.__coffee_size=['大杯','小杯']
        self.__coffee_number=['1','2','3','4']

    def __extract_type(self,text):
        coffee_type=[c_type for c_type in self.__coffee_type if c_type in text]
        c_type=coffee_type[0] if len(coffee_type)>0 else ''
        return c_type

    def __extract_size(self,text):
        coffee_size=[c_size for c_size in self.__coffee_size if c_size in text]
        size=coffee_size[0] if len(coffee_size)>0 else ''
        return size

    def __extract_number(self,text):
        pattern=re.compile('\d+|[一二三四五六七]')
        res=re.findall(pattern,text)
        if len(res)==1:
            return str(res)
        else:
            return ''

    def execute(self,text):
        slot={'TYPE':self.__extract_type(text),'SIZE':self.__extract_size(text),'NUMBER':self.__extract_number(text)}
        return slot
