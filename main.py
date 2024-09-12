from prefect import flow
import os

@flow
def main():
    os.system("uflash microbit.py")
