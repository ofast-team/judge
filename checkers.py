import subprocess
import constants

def diff_check(user_file, expected_file):
    run = ["diff", user_file, expected_file]
    diff_result = subprocess.run(run, capture_output=True)
    if bytes.decode(diff_result.stdout) == "":
        return constants.Verdict.accepted
    return constants.Verdict.wrong_answer

def token_check(user_file, expected_file, case_sensitive=True):

    try:
        user = open(user_file, "r")
    except:
        print("Unable to open file for reading user output")
        return constants.Verdict.system_error
    
    try:
        expected = open(expected_file, "r")
    except:
        print("Unable to open file for reading system output")
        return constants.Verdict.system_error

    user_tokens = []
    for line in user:
        user_tokens += line.split()
    user.close()

    expected_tokens = []
    for line in expected:
        expected_tokens += line.split()
    expected.close()

    print(user_tokens, expected_tokens)
    if len(user_tokens) != len(expected_tokens):
        return constants.Verdict.wrong_answer
    
    for (user_token, expected_token) in zip(user_tokens, expected_tokens):
        if not case_sensitive:
            user_token = user_token.lower()
            expected_token = expected_token.lower()
        
        if user_token != expected_token:
            return constants.Verdict.wrong_answer

    return constants.Verdict.accepted