# 알람 시계
class Alarm:
    def __init__(self, hour, minute) -> None:
        self.hour = hour
        self.minute = minute

        self.set_time()

    def set_time(self):
        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1
        elif self.minute < 0:
            self.minute += 60
            self.hour -= 1
        if self.hour >= 24:
            self.hour -= 24
        elif self.hour < 0:
            self.hour += 24

    def set_earlier(self, early=45):
        self.minute -= early

        self.set_time()


h, m = map(int, input().split())
alarm = Alarm(h, m)

alarm.set_earlier()

print(alarm.hour, alarm.minute)
