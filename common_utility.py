import configparser
from functools import wraps
import time
import random
import string

def read_config_file(path_config_file):
    """
    This reads the data from a config file.
    :param path_config_file: Path of config file where it is located.
    :return:
    """
    try:
        config = configparser.ConfigParser()
        config.read(path_config_file)
        return config

    except Exception as e:
        assert False, "Failed to read config file :{}".format(e)

def get_time(write_to_file=False):
    def my_timer(orig_func):
        """
        This is a decorator which actually ca;culated the time taken by a function to execute
        :param orig_func:
        :return:
        """
        @wraps(orig_func)
        def wrapper_func(*args,**kwargs):
            t1=time.time()
            result= orig_func(*args,**kwargs)
            t2=time.time() - t1
            print("{} ran in :{} sec".format(orig_func.__name__,t2))

            filename = "result_file_type.txt"

            if write_to_file:
                with open(filename, 'w+') as file:
                    file.write("Test Name: {} ran in :{} sec".format(orig_func.__name__,t2))
                    file.write('\n')

            return result
        return wrapper_func
    return my_timer

# def get_time(write_to_file=False):
#     def decorate(test_function):
#         @wraps(test_function)
#         def execution_time(*args, **kwargs):
#             ts = time.time()
#             result = test_function(*args, **kwargs)
#             te = time.time()
#
#             param = ''
#             for item in kwargs:
#                 if str(type(kwargs[item]))[8:11] in ['str', 'int']:
#                     param = param + '_' + str(kwargs[item])
#             filename ="abhiishekk.txt"
#             output = (
#                 f"Test Name: {test_function.__name__}, Paramter: {param[1:]} , Run Execution Time: {(te - ts) * 1000} ms.")
#             print(output)
#
#             if write_to_file:
#                 with open(filename, 'w+') as file:
#                     file.write(output)
#                     file.write('\n')
#
#             return result
#
#         return execution_time
#
#     return decorate


def generate_string_of_alpha_numeric_char():
    """
    Generate alphanumeric string.
    :return: random string
    """

    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))