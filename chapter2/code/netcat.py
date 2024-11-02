import argparse
import socket
import shlex
import subbprocess
import sys
import textwrap
import threading

def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subbprocess.check_output(shlex.split(cmd), stderr=subbprocess.STDOUT)
    return output.decode()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="BHP Net Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""
                               Example:
                               netcat.py -t 192.168.1.108 -p 5555 -l -c # command shell
                               netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt #upload to file
                               netcat.py -t 192.168.1.108 -p 5555 -l-e=\"cat /etc/passwd\" # execute command
                               echo 'ABC' | ./netcat.py -t 192.168.1.108 -p 135 # echo text to servrer port 135
                               netcat.py -t 192.168.1.108 -p 5555 # connect to server
                               """)
    )
