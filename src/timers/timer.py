from time import sleep


class Timer:
    def startTimer(self, waiting_time: int) -> None:
        self.startWorkingTimer(waiting_time)
        self.startRestingTimer()

    def startWorkingTimer(self, working_time_in_minutes: int) -> None:
        self.working_time = working_time_in_minutes * 60

        print(f"Sleeping for {self.working_time}")  # for testing only
        sleep(self.working_time)

    def startRestingTimer(self) -> None:
        resting_time = self.working_time // 3

        print(f"Resting for {resting_time}")  # for testing only
        sleep(resting_time)


class TimerFactory(Timer):
    def normalStamp(self):
        self.startTimer(25)

    def singleStamp(self):
        self.startTimer(60)

    def halfStamp(self):
        self.startTimer(30)

    def tripartiteStamp(self):
        self.startTimer(180)

    def quarterlyStamp(self):
        self.startTimer(180)
