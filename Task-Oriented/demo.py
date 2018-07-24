from module.NLU.nlu  import *
from module.DM.manage import  *
from module.NLG.generate import  *

class Bot(object):
    def __init__(self):
        self.nlu=RuleBasedNLU()
        self.manager=Manager()
        self.generator=NLG()


    def reply(self,sent):
        dialog_act=self.nlu.execute(sent)
        self.manager.update_state(dialog_act)
        sys_act=self.manager.select_action(dialog_act)
        print(self.generator.generate_sentence(sys_act))










if __name__=="__main__":
    bot=Bot()
    print('您好，有什么可以为您服务的吗？')
    while True:
        sent=input('U:')
        if sent=='谢谢':
            break
        else:
            bot.reply(sent)





