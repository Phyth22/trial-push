# overiding refers to when a class has multiple methods with the same name , but diff implimentations

class SetAlarm(set):
    def run_Alarm(self):
      return "i will run at 10"
    def run_Alarm(self):
           return"i will run at 11"
    def run_Alarm(self):
           return"I will run at 12"
time_object = SetAlarm()
print(time_object.run_Alarm()) # in this case , the last method definition (run_Alarm)overrides the previous ones

class set