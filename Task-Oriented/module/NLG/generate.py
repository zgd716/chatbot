import sys
class NLG(object):
    def __init__(self):
        pass

    def generate_sentence(self,sys_act):
        sent=''

        system_act_type = sys_act['sys_act_type']
        if system_act_type == "REQUEST_TYPE":
            sent += "请问您点什么类型的咖啡，我们有摩卡，拿铁和美式"
        elif system_act_type == "REQUEST_SIZE":
            sent += "大杯还是小杯呢？"
        elif system_act_type == "REQUEST_NUMBER":
            sent += "您要点几杯呢？"
        elif system_act_type == "INFORM_COFFEE":
            coffee = sys_act['coffee']
            sent += "已经为你预订成功。\n再次确认下你的订单：咖啡类型{0}，{1}，{2}杯。\n 希望再次可以为您服务！".format(coffee['type'],
                                                                                  coffee['size'],
                                                                                  coffee['number'])

        else:
            print("ERROR")
            sys.exit(1)

        return sent
