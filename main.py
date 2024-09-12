from prefect import flow
import os

@flow
def microbit_test():
    os.system("uflash microbit.py")