from enum import Enum

class Verdict(Enum):
    compilation_error = 1
    runtime_error = 2
    time_limit = 3
    memory_limit = 4
    wrong_answer = 5
    accepted = 6
    user_error = 98
    system_error = 99

class Checker(Enum):
    diff = 1
    token = 2
    epsilon = 3

MAX_TIME_LIMIT = 10

TIME_OUT = 124