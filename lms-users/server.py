import sys
import time

if __name__ == "__main__":
    sys.stdout.write("Starting lms-users...")

    while True:
        sys.stdout.write('|')
        sys.stdout.flush()

        time.sleep(0.5)
        
        sys.stdout.write('\b \b')
        sys.stdout.write('/')
        sys.stdout.flush()
        
        time.sleep(0.5)

        sys.stdout.write('\b \b')
        sys.stdout.write('-')
        sys.stdout.flush()
        
        time.sleep(0.5)
    
        sys.stdout.write('\b \b')
        sys.stdout.write('\\')
        sys.stdout.flush()

        time.sleep(0.5)
        
        sys.stdout.write('\b \b')




