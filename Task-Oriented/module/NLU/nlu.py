from copy import copy
from .dialog_act_type.rule_based_estimator import *
from .slot_extract.rule_based_extractor import *
class RuleBasedNLU(object):

    def __init__(self):
        self.__estimator=Estimator()
        self.__extractor=RuleBaseExtrator()

    def execute(self,sent):
        slot=self.__extractor.execute(sent)
        act_type=self.__estimator.estimator(slot)
        dialog_act={'user_act_type':act_type}

        slot_cp=copy(slot)
        for k,v in slot_cp.items():
            if v=='':
                del slot[k]
        dialog_act.update(slot)
        return  dialog_act


