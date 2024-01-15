import subprocess
import constants

def diff_check(user_file, expected_file):
    diff_result = subprocess.run(["diff", user_file, expected_file], capture_output=True)
    return bytes.decode(diff_result.stdout) == ""