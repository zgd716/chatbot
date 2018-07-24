class Estimator(object):

    def __init__(self):
        pass

    def estimator(self,slot):

        if slot['TYPE']!='':
            return 'INFORM_TYPE'
        elif slot['SIZE']!='':
            return 'INFORM_SIZE'
        elif slot['NUMBER']!='':
            return  'INFORM_NUMBER'
        else:
            return 'OTHER'