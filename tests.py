import compile
import constants
import pytest

# flip this to True to avoid doing the TLE tests so testing goes faster
fast = False

class Test:
    # Diff checker tests

    def test_diff_AC_c(self):
        result = compile.compile_and_run("./tests/diff/AC/hello.c", "./tests/diff/AC/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.accepted
    
    def test_diff_AC_cpp(self):
        result = compile.compile_and_run("./tests/diff/AC/hello.cpp", "./tests/diff/AC/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.accepted

    def test_diff_AC_java(self):
        result = compile.compile_and_run("./tests/diff/AC/hello.java", "./tests/diff/AC/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.accepted
    
    def test_diff_AC_py(self):
        result = compile.compile_and_run("./tests/diff/AC/hello.py", "./tests/diff/AC/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.accepted

    def test_diff_WA_c(self):
        result = compile.compile_and_run("./tests/diff/WA/hello.c", "./tests/diff/WA/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.wrong_answer

    def test_diff_WA_cpp(self):
        result = compile.compile_and_run("./tests/diff/WA/hello.cpp", "./tests/diff/WA/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.wrong_answer

    def test_diff_WA_java(self):
        result = compile.compile_and_run("./tests/diff/WA/hello.java", "./tests/diff/WA/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.wrong_answer

    def test_diff_WA_py(self):
        result = compile.compile_and_run("./tests/diff/WA/hello.py", "./tests/diff/WA/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.wrong_answer

    # General Tests

    @pytest.mark.skipif(fast, reason="takes too long")
    def test_TLE_c(self):
        result = compile.compile_and_run("./tests/general/TLE/hello.c", "./tests/general/TLE/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.time_limit
   
    @pytest.mark.skipif(fast, reason="takes too long")
    def test_TLE_cpp(self):
        result = compile.compile_and_run("./tests/general/TLE/hello.cpp", "./tests/general/TLE/hello", constants.Checker.diff, 5)
        for res in result:
            assert res == constants.Verdict.time_limit
   
    @pytest.mark.skipif(fast, reason="takes too long")
    def test_TLE_java(self):
        result = compile.compile_and_run("./tests/general/TLE/hello.java", "./tests/general/TLE/hello", constants.Checker.diff, 5)
        for res in result:
            assert res == constants.Verdict.time_limit
   
    @pytest.mark.skipif(fast, reason="takes too long")
    def test_TLE_py(self):
        result = compile.compile_and_run("./tests/general/TLE/hello.py", "./tests/general/TLE/hello", constants.Checker.diff, 5)
        for res in result:
            assert res == constants.Verdict.time_limit
   
    def test_RTE_c(self):
        result = compile.compile_and_run("./tests/general/RTE/hello.c", "./tests/general/RTE/hello", constants.Checker.diff, 5)
        for res in result:
            assert res == constants.Verdict.runtime_error
   
    def test_RTE_cpp(self):
        result = compile.compile_and_run("./tests/general/RTE/hello.cpp", "./tests/general/RTE/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.runtime_error
   
    def test_RTE_java(self):
        result = compile.compile_and_run("./tests/general/RTE/hello.java", "./tests/general/RTE/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.runtime_error
   
    def test_RTE_py(self):
        result = compile.compile_and_run("./tests/general/RTE/hello.py", "./tests/general/RTE/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.runtime_error
    
    # Token Checker tests
    
    def test_token_AC_c(self):
        result = compile.compile_and_run("./tests/token/AC/hello.c", "./tests/token/AC/hello", constants.Checker.token)
        for res in result:
            assert res == constants.Verdict.accepted
    
    def test_token_AC_cpp(self):
        result = compile.compile_and_run("./tests/token/AC/hello.cpp", "./tests/token/AC/hello", constants.Checker.token)
        for res in result:
            assert res == constants.Verdict.accepted

    def test_token_AC_java(self):
        result = compile.compile_and_run("./tests/token/AC/hello.java", "./tests/token/AC/hello", constants.Checker.token)
        for res in result:
            assert res == constants.Verdict.accepted

    def test_token_AC_py(self):
        result = compile.compile_and_run("./tests/token/AC/hello.py", "./tests/token/AC/hello", constants.Checker.token)
        for res in result:
            assert res == constants.Verdict.accepted

    def test_token_WA_c(self):
        result = compile.compile_and_run("./tests/token/WA/hello.c", "./tests/token/WA/hello", constants.Checker.token)
        for res in result:
            assert res == constants.Verdict.wrong_answer

    def test_token_WA_cpp(self):
        result = compile.compile_and_run("./tests/token/WA/hello.cpp", "./tests/token/WA/hello", constants.Checker.token)
        for res in result:
            assert res == constants.Verdict.wrong_answer

    def test_token_WA_java(self):
        result = compile.compile_and_run("./tests/token/WA/hello.java", "./tests/token/WA/hello", constants.Checker.token)
        for res in result:
            assert res == constants.Verdict.wrong_answer

    def test_token_WA_py(self):
        result = compile.compile_and_run("./tests/token/WA/hello.py", "./tests/token/WA/hello", constants.Checker.token)
        for res in result:
            assert res == constants.Verdict.wrong_answer
