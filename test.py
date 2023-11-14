import sys
import compile
import constants

n = len(sys.argv)
if n != 3:
    print("Incorrect call of program.  Use", sys.argv[0] ,"<userprogram> <inputfolder>")
    exit(1)
solution = sys.argv[1]
input_folder = sys.argv[2]

compile.compile_and_run(solution, input_folder, constants.Checker.diff)