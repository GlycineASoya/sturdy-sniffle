'''
Simple counter application
'''

from time import sleep

def count(start: int) -> int:
    '''
    Simple counter
    '''
    return start+1

def main():
    '''
    Main cycle
    '''
    start = 0
    timeout = 1 # in seconds
    while True:
        print(f"The counter is {start}")
        sleep(timeout)
        start = count(start)

if __name__ == "__main__":
    main()