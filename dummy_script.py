import sys
import time
import Python

def flush_then_wait():
    sys.stdout.flush()
    sys.stderr.flush()
    time.sleep(0.5)

sys.stdout.write("Script stdout 1\n")
sys.stdout.write("Script stdout 2\n")
sys.stdout.write("Script stdout 3\n")
sys.stderr.write("Total time: 00:05:00\n")
sys.stderr.write("Total complete: 10%\n")
flush_then_wait()

sys.stdout.write("name=Sebastian\n")
sys.stdout.write("Script stdout 4\n")
sys.stdout.write("Script stdout 5\n")
sys.stderr.write("Total complete: 30%\n")
flush_then_wait()

sys.stderr.write("Elapsed time: 00:00:10\n")
sys.stderr.write("Elapsed time: 00:00:50\n")
sys.stderr.write("Total complete: 50%\n")
sys.stdout.write("country=Argentina\n")
flush_then_wait()

sys.stderr.write("Elapsed time: 00:01:10\n")
sys.stderr.write("Total complete: 100%\n")
sys.stdout.write("Script stdout 6\n")
sys.stdout.write("Script stdout 7\n")
sys.stdout.write("website=www.blancseba.com\n")
flush_then_wait()