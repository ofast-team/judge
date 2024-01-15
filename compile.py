import subprocess
import constants
import checkers

# This is the diff_check function it takes in (as strings) two file names, and returns True if
# there are no differences between the two files, and false otherwise


# This function takes in (as strings) the path to the solution file and input folders along
# with which type of checker will be used
def compile_and_run(solution, input_folder, check_type, time_limit=constants.MAX_TIME_LIMIT):
    
    # setting up filename information:
    # name is the path/file name without the extension, and lang is the extension
    split_ind = solution.rfind(".")
    if split_ind == -1:
        print("Invalid solution file:", solution)
        return [constants.Verdict.user_error]
    lang = solution[split_ind + 1: len(solution)]
    name = solution[0 : split_ind]
    time_limit = min(time_limit, constants.MAX_TIME_LIMIT)

    # Compiles (if neccesary) and sets up run which stores how to run the user
    # program based on the language.
    run = ["timeout", f"{time_limit}s"]
    if lang == "py":
        run += ["python3", solution]
    elif lang == "cpp" or lang == "c++":
        result = subprocess.run(["g++", "-g", "-O2", "-std=c++17", "-o", "userprogram", solution, "-lm"], capture_output=True)
        if result.returncode != 0:
            print("Compilation Error!")
            return [constants.Verdict.compilation_error]
        run += ["timeout", f"{time_limit}s", "./userprogram"]
    elif lang == "c":
        result = subprocess.run(["gcc", "-g", "-O2", "-std=c11", "-o", "userprogram", solution, "-lm"], capture_output=True)
        if result.returncode != 0:
            print("Compilation Error!")
            return [constants.Verdict.compilation_error]
        run += ["./userprogram"]
    elif lang == "java":
        result = subprocess.run(["javac", "-d", "./", solution], capture_output=True)
        if result.returncode != 0:
            print("Compilation Error!")
            return [constants.Verdict.compilation_error]
        path = name.split("/")
        class_name = path[-1]
        run += ["java", "-Xss64m", "-Xmx2048m", class_name]
    else:
        print("Language", lang ,"not supported!")
        return [constants.Verdict.user_error]
    
    case_list = subprocess.run(["ls", input_folder], capture_output=True)
    if case_list.returncode == 2:
        print(input_folder, "does not exist!")
        return [constants.Verdict.user_error]

    is_directory = subprocess.run(["test", "-d", input_folder], capture_output=True)
    if is_directory.returncode == 1:
        print(input_folder, "is not a directory!")
        return [constants.Verdict.user_error]

    # Running each test case
    cases = bytes.decode(case_list.stdout).split('\n')
    verdict_arr = []
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

        if skip:
            verdict_arr.append(constants.Verdict.user_error)
            print("Skipping case...", case)
            continue

        try:
            input_file = open(path + input_file_string, "r")
        except:
            verdict_arr.append(constants.Verdict.system_error)
            print("Unable to open", input_file_string)
            skip = True

        if skip:
            print("Skipping case...", case)
            continue

        try:
            output_file = open("user.out", "w")
        except:
            verdict_arr.append(constants.Verdict.system_error)
            print("Unable to open file for outputting user data")
            skip = True

        if skip:
            print("Skipping case...", case)
            continue

        cur_result = subprocess.run(run, stdin=input_file, stdout=output_file)
        input_file.close()
        output_file.close()

        # Ensuring that there were no problems during the runtime
        if cur_result.returncode == constants.TIME_OUT:
            verdict_arr.append(constants.Verdict.time_limit)
            print(case, ": TLE")
            subprocess.run(["rm", "user.out"])
            break
        if cur_result.returncode != 0:
            verdict_arr.append(constants.Verdict.runtime_error)
            print(case, ": RTE")
            subprocess.run(["rm", "user.out"])
            break
        if check_type == constants.Checker.diff:
            if checkers.diff_check("user.out", path + output_file_string):
                verdict_arr.append(constants.Verdict.accepted)
                print(case, ": AC")
            else:
                verdict_arr.append(constants.Verdict.wrong_answer)
                print(case, ": WA")
        subprocess.run(["rm", "user.out"])

    return verdict_arr