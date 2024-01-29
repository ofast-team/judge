import compile
import constants
import pytest

# flip this to True to avoid doing the TLE tests so testing goes faster
fast = False

class Test:
    # Testing to ensure that the AC verdict works properly with the c file
    def test_diff_AC_c(self):
        result = compile.compile_and_run("./tests/AC/hello.c", "./tests/AC/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.accepted
    
    # Testing to ensure that the AC verdict works properly with the cpp file
    def test_diff_AC_cpp(self):
        result = compile.compile_and_run("./tests/AC/hello.cpp", "./tests/AC/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.accepted

    # Testing to ensure that the AC verdict works properly with the java file
    def test_diff_AC_java(self):
        result = compile.compile_and_run("./tests/AC/hello.java", "./tests/AC/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.accepted
    
    # Testing to ensure that the AC verdict works properly with the python file
    def test_diff_AC_py(self):
        result = compile.compile_and_run("./tests/AC/hello.py", "./tests/AC/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.accepted

    # Testing to ensure that the WA verdict works properly with the c file
    def test_diff_WA_c(self):
        result = compile.compile_and_run("./tests/WA/hello.c", "./tests/WA/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.wrong_answer

    # Testing to ensure that the WA verdict works properly with the cpp file
    def test_diff_WA_cpp(self):
        result = compile.compile_and_run("./tests/WA/hello.cpp", "./tests/WA/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.wrong_answer

    # Testing to ensure that the WA verdict works properly with the java file
    def test_diff_WA_java(self):
        result = compile.compile_and_run("./tests/WA/hello.java", "./tests/WA/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.wrong_answer

    # Testing to ensure that the WA verdict works properly with the python file
    def test_diff_WA_py(self):
        result = compile.compile_and_run("./tests/WA/hello.py", "./tests/WA/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.wrong_answer

    # Testing to ensure that the TLE verdict works properly with the c file
    @pytest.mark.skipif(fast, reason="takes too long")
    def test_diff_TLE_c(self):
        result = compile.compile_and_run("./tests/TLE/hello.c", "./tests/TLE/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.time_limit
   
    # Testing to ensure that the TLE verdict works properly with the cpp file
    @pytest.mark.skipif(fast, reason="takes too long")
    def test_diff_TLE_cpp(self):
        result = compile.compile_and_run("./tests/TLE/hello.cpp", "./tests/TLE/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.time_limit
   
    # Testing to ensure that the TLE verdict works properly with the java file
    @pytest.mark.skipif(fast, reason="takes too long")
    def test_diff_TLE_java(self):
        result = compile.compile_and_run("./tests/TLE/hello.java", "./tests/TLE/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.time_limit
   
    # Testing to ensure that the TLE verdict works properly with the python file
    @pytest.mark.skipif(fast, reason="takes too long")
    def test_diff_TLE_py(self):
        result = compile.compile_and_run("./tests/TLE/hello.py", "./tests/TLE/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.time_limit
   
    # Testing to ensure that the RTE verdict works properly with the c file
    def test_diff_RTE_c(self):
        result = compile.compile_and_run("./tests/RTE/hello.c", "./tests/RTE/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.runtime_error
   
    # Testing to ensure that the RTE verdict works properly with the cpp file
    def test_diff_RTE_cpp(self):
        result = compile.compile_and_run("./tests/RTE/hello.cpp", "./tests/RTE/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.runtime_error
   
    # Testing to ensure that the RTE verdict works properly with the cpp file
    def test_diff_RTE_java(self):
        result = compile.compile_and_run("./tests/RTE/hello.java", "./tests/RTE/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.runtime_error
   
    # Testing to ensure that the RTE verdict works properly with the cpp file
    def test_diff_RTE_py(self):
        result = compile.compile_and_run("./tests/RTE/hello.py", "./tests/RTE/hello", constants.Checker.diff)
        for res in result:
            assert res == constants.Verdict.runtime_error