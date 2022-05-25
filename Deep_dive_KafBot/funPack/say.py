import pyttsx3
class sayfunc():
    def __init__(self,):

        self.engine = pyttsx3.init()  # 创建pyttsx对象，并初始化对象
        self.engine.setProperty('voice', 'zh')
        self.engine.setProperty('rate', 150)
    def say(self,msg):
        self.engine.say(msg)
        self.engine.runAndWait()