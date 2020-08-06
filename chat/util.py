import uuid


def create_rand_string():
    return uuid.uuid4().hex.upper()


class Colors:
    """
    색깔을 추가해주세요...
    https://wiki.ubuntu-kr.org/index.php/ANSI_%EC%BB%AC%EB%9F%AC_%EC%BD%94%EB%93%9C
    https://xinet.kr/?p=220
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    BACK_RED = '\033[41m'


# 헉 It's not recommend to use lamda, but use def.
# print_to_server = lambda color, msg, *args: print(color, msg, *args, Colors.ENDC)

def print_green(msg, *args):
    print(Colors.OKGREEN, msg, *args, Colors.ENDC)


def print_yellow(msg, *args):
    print(Colors.WARNING, msg, *args, Colors.ENDC)


def print_red(msg, *args):
    print(Colors.FAIL, msg, *args, Colors.ENDC)


def print_back_red(msg, *args):
    print(Colors.BACK_RED, msg, *args, Colors.ENDC)
