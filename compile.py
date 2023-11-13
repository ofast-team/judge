import subprocess
import constants

# This is the diff_check function it takes in (as strings) two file names, and returns True if
# there are no differences between the two files, and false otherwise
def diff_check(user_file, expected_file):
    diff_result = subprocess.run(["diff", user_file, expected_file], capture_output=True)
    if bytes.decode(diff_result.stdout) == "":
        return True
    else:
        return False

# This function takes in (as strings) the path to the solution file and input folders along
# with which type of checker will be used
def compile_and_run(solution, input_folder, check_type):
    
    # setting up filename information:
    # name is the path/file name without the extention, and lang is the extention
    arr = solution.split(".")
    if len(arr) < 2:
        print("Invalid solution file:", solution)
    lang = arr[len(arr) - 1]
    name = ""
    for i in range(len(arr) - 1):
        name += arr[i]
        if (i != len(arr) - 2):
            name += "."

    # Compiles (if neccesary) and sets up run which stores how to run the user
    # program based on the language.
    run = []
    if lang == "py":
        run = ["python3", solution]
    elif lang == "cpp" or lang == "c++" or lang == "c":
        result = subprocess.run(["g++", "-g", "-O2", "-std=c++17", "-o", "userprogram", solution, "-lm"], capture_output=True)
        if result.returncode != 0:
            print("Compilation Error!")
            exit(1)
        run = ["./userprogram"]
    elif lang == "java":
        result = subprocess.run(["javac", "-d", "./", solution], capture_output=True)
        if result.returncode != 0:
            print("Compilation Error!")
            exit(1)
        path = name.split("/")
        class_name = path[len(path) - 1]
        run = ["java", "-Xss64m", "-Xmx2048m", class_name]
    else:
        print("Language", lang ,"not supported!")
        exit(1)
    
    case_list = subprocess.run(["ls", input_folder], capture_output=True)
    if case_list.returncode == 2:
        print(input_folder, "does not exist!")
        exit(1)

    is_directory = subprocess.run(["test", "-d", input_folder], capture_output=True)
    if is_directory.returncode == 1:
        print(input_folder, "is not a directory!")
        exit(1)

    # Running each test case
    cases = bytes.decode(case_list.stdout).split('\n')
    for case in cases:
        if case == "":
            continue

        path = input_folder + "/" + case + "/"
        file_list = subprocess.run(["ls", path], capture_output=True)
        files = bytes.decode(file_list.stdout).split('\n')

        input_file_string = ""
        output_file_string = ""
        skip = False

        # Checks to ensure there's only one input and output file per test case and
        # ignores all other files.  If the test case is invalid it will skip over.
        for file in files:
            if file == "":
                continue

            try:
                file_name, file_ext = file.split(".")
            except:
                continue

            if file_ext == "in" and input_file_string == "":
                input_file_string = file
            elif file_ext == "out" and output_file_string == "":
                output_file_string = file
            elif file_ext == "in":
                print(case, "is invalid, multiple .in files")
                skip = True
                break
            elif file_ext == "out":
                print(case, "is invalid, multiple .out files")
                skip = True
                break

        if input_file_string == "":
            print("No input file found in", case)
            skip = True
        if output_file_string == "":
            print("No output file found in", case)
            skip = True

        try:
            input_file = open(path + input_file_string, "r")
        except:
            print("Unable to open", input_file_string)
            skip = True

        try:
            output_file = open("user.out", "w")
        except:
            print("Unable to open file for outputting user data")
            skip = True

        if skip:
            print("Skipping case...", case)
            continue

        cur_result = subprocess.run(run, stdin=input_file, stdout=output_file)
        input_file.close()
        output_file.close()

        # TODO: pretty sure this will cause problems if users don't return 0 in c but im not
        # dealing with that rn
        if cur_result.returncode != 0:
            print(case, ": RTE")
            break
        if check_type == constants.Checker.diff:
            if diff_check("user.out", path + output_file_string):
                print(case, ": AC")
            else:
                print(case, ": WA")
