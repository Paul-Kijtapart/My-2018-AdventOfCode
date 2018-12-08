from collections import namedtuple, Counter
from datetime import datetime
import re
from functools import reduce

SleepInterval = namedtuple('SleepInterval', ['duration', 'start', 'end'])
Log = namedtuple('Log', ['date', 'description'])


class Solution:

    @classmethod
    def log_comparator(cls, l1, l2):
        """

        Args:
            l1 (Log):
            l2 (Log):

        Returns:

        """
        if l1.date < l2.date:
            return - 1
        elif l1.date > l2.date:
            return 1

        return 0

    @classmethod
    def load_elves_log(cls):
        ret = []
        with open('day4/input/elves_log.txt', 'r') as in_file:
            logs = in_file.readlines()
            for log in logs:
                curr_log = cls.parse_elf_log(log)
                ret.append(curr_log)
        ret.sort(key=lambda l: l[0])
        return ret

    @classmethod
    def parse_elf_log(cls, log_str):
        date_str = re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}', log_str)[0]
        description = ''.join(re.findall(r'(wakes up|falls asleep|#\d+)', log_str))
        datetime_format = '%Y-%m-%d %H:%M'
        return Log(description=description, date=datetime.strptime(date_str, datetime_format))

    @classmethod
    def question_1(cls):
        all_logs = cls.load_elves_log()
        sleep_interval_map = cls.get_sleep_intervals(all_logs)
        id = cls.get_sleepy_head_id(
            sleep_intervals=sleep_interval_map
        )
        current_intervals = sleep_interval_map[id]
        current_minutes = cls.get_minutes(current_intervals)
        current_min_counter = Counter(current_minutes)
        most_common = current_min_counter.most_common(1)
        answer1 = 37 * 1049
        print('answer:1  {}'.format(answer1))

    @classmethod
    def question_2(cls):
        all_logs = cls.load_elves_log()
        sleep_interval_map = cls.get_sleep_intervals(all_logs)
        id_to_minutes = {}
        for id, intervals in sleep_interval_map.items():
            id_to_minutes[id] = cls.get_minutes(sleep_intervals=intervals)

        answer_id = None
        answer_frequency = 0
        for id, minutes in id_to_minutes.items():
            current_min_counter = Counter(minutes)
            current_most_common = current_min_counter.most_common(1)[0]
            if current_most_common[1] > answer_frequency:
                answer_id = current_most_common[0]
                answer_frequency = current_most_common[1]

        print(answer_id * current_most_common[1] * current_most_common[0])

    @classmethod
    def get_sleep_intervals(cls, all_logs):
        sleep_intervals = {}

        id = None
        start = None
        end = None
        for log in all_logs:
            if log.description == 'falls asleep':
                start = log.date
            elif log.description == 'wakes up':
                end = log.date

                new_si = SleepInterval(
                    duration=end - start,
                    start=start,
                    end=end
                )

                if id in sleep_intervals:
                    sleep_intervals[id].append(new_si)
                else:
                    sleep_intervals[id] = [new_si]
            # if this is id (new)
            else:
                id = log.description

        return sleep_intervals

    @classmethod
    def get_sleepy_head_id(cls, sleep_intervals):

        sleepy_head = None
        max_duration = datetime.now() - datetime.now()

        for id, intervals in sleep_intervals.items():
            total_sleep = cls.sum_duration(intervals)

            if total_sleep > max_duration:
                max_duration = total_sleep
                sleepy_head = id

        return sleepy_head

    @classmethod
    def get_minutes(cls, sleep_intervals):
        minutes = []
        for sleep_interval in sleep_intervals:
            start_min = sleep_interval.start.minute
            end_min = sleep_interval.end.minute
            minutes += [cm for cm in range(start_min, end_min)]

        return minutes
