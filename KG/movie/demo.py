from preprocess import *
import joblib
from kb import *
if __name__=="__main__":
    startJVM(getDefaultJVMPath(),
             "-Djava.class.path=D:\ProgramData\Anaconda3\envs\kbqa\Lib\site-packages\pyhanlp\static\hanlp-1.6.6.jar;D:\ProgramData\Anaconda3\envs\kbqa\Lib\site-packages\pyhanlp\static",
             "-Xms1g",
             "-Xmx1g")  # 启动JVM，Linux需替换分号;为冒号:
    while True:
        question=input('请输入你想查询的信息：')   #英雄这部电影讲的什么？
        index,params=analysis_quetion(question)
        answers=get_data(index,params)
        print('答案:')
        for ans in answers:
            print(ans[0])



