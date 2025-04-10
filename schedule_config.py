from datetime import datetime, timedelta


class ScheduleConfig:
    def __init__(self, message, receiver, firs_send_time, period, n_times_send):
        self.message = message
        self.receiver = receiver
        self.firs_send_time = firs_send_time
        self.period = period
        self.n_times_send = n_times_send

    def to_dict(self):
        return {
            "message": self.message,
            "receiver": self.receiver,
            "firs_send_time": self.firs_send_time,
            "period": self.period,
            "n_times_send": self.n_times_send,
        }
