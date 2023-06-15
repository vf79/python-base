#!/usr/bin/env python3
import time
import logging

log = logging.Logger("errors")

# EAFP - Easy to ASK Forgiveness than permission
# (É mais fácil pedir perdão do que permissão)


#try:
#    names = open("names.txt").readlines() # FileNotFoundError
#    1 / 1 # ZeroDivisionError
#    print(names.append) # AttibuteError
#except FileNotFoundError:
#    print("[Error]: File names.txt not found.")
#    sys.exit(1)
#except FileNotFoundError as e:
#    print(f"{str(e)}.")
#    sys.exit(1)
#except ZeroDivisionError:
#    print("[Error]: You cant divide by zero.")
#    sys.exit(1)
#except AttributeError:
#    print("[Error]: List doesn't have banana.")
#    sys.exit(1)
#except: # Bare except
#    print("[Error]: Generic Error # Ex: Bare Exception.")
#    sys.exit(1)
#
#else:
#    print("Sucesso!!!")
#finally:
#    print("Execute isso sempre")

def try_to_open_a_file(filepath, retry=1)->list:
    """Tries to open a file, if erro, retries n times."""
    if retry > 999:
        raise ValueError("Retry cannot be above 999")
    try:
        return open(filepath).readlines() # FileNotFoundError
    except FileNotFoundError as e:
        log.error("ERRO: %s", e)
        time.sleep(2)
        if retry > 1:
            # recursao
            return try_to_open_a_file(filepath, retry=retry - 1)
    else:
        print("Sucesso!!!")
    finally:
        print("Execute isso sempre")
    return []


for line in try_to_open_a_file("names.txt", retry=10):
    print(line)

