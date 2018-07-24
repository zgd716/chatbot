from copy import copy

from .state import *
class Manager(object):

    def __init__(self):
        self.state=State()

    def update_state(self,dialog_act):
        self.state.update(dialog_act)

    def select_action(self,dialog_act):
        system_act=copy(dialog_act)
        if not self.state.has('type'):
            system_act['sys_act_type']='REQUEST_TYE'
        elif not self.state.has('size'):
            system_act['sys_act_type']='REQUEST_SIZE'
        elif not self.state.has('number'):
            system_act['sys_act_type'] = 'REQUEST_NUMBER'
        else:
            coffee_type=self.state.get_type()
            coffee_size = self.state.get_size()
            coffee_number = self.state.get_number()

            system_act['coffee']={'type':coffee_type,'size':coffee_size,'number':coffee_number}
            system_act['sys_act_type']='INFORM_COFFEE'
            self.state.clear()

        return system_act
