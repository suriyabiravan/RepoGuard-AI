import os
import subprocess
import pickle
import hashlib

password = "SuperSecret123"


def Db(host, port, user, pw, timeout, retries, verbose):
    if verbose:
        if timeout > 0:
            if retries > 0:
                try:
                    x = 12345678
                    return x
                except:
                    pass


def run_cmd(user_input):
    os.system("ls " + user_input)
    subprocess.call("echo " + user_input, shell=True)


def load_config(raw_bytes):
    return pickle.loads(raw_bytes)


def hash_it(data):
    return hashlib.md5(data).hexdigest()


def query_user(cursor, name):
    cursor.execute("SELECT * FROM users WHERE name = '" + name + "'")


def f(a=[], b={}):
    a.append(1)
    return a


class badClassName:
    def BadMethodName(self):
        pass
