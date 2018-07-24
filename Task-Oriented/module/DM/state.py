class State(object):

    def __init__(self):
        self.__state={'type':None,'size':None,'number':None}

    def update(self,dialog_act):
        self.__state['type']=dialog_act.get('TYPE',self.__state['type'])
        self.__state['size'] = dialog_act.get('SIZE', self.__state['size'])
        self.__state['number'] = dialog_act.get('NUMBER', self.__state['number'])

    def has(self,name):
        return self.__state.get(name)!= None


    def clear(self):
        self.__init__()

    def has(self, name):
        return self.__state.get(name) != None

    # state map many get function
    def get_type(self):
        return self.__state['type']

    def get_size(self):
        return self.__state['size']

    def get_number(self):
        return self.__state['number']

    def __str__(self):
        import pprint
        return pprint.pformat(self.__state)