@echo off
set "CurDir="
for %%a in ("%cd%") do set "CurDir=%%~nxa"
if NOT "%CurDir%" == "assignment4" exit

if exist %CD%\src\test\testcases\ (
    echo "Cleaning testcases"
	rmdir /Q /S %CD%\src\test\testcases\
)
    echo "Creating testcases"
    mkdir %CD%\src\test\testcases\

if exist %CD%\src\test\solutions\ (
    echo "Cleaning solutions"
	rmdir /Q /S %CD%\src\test\solutions\
)
    echo "Creating solutions"
    mkdir %CD%\src\test\solutions\

@REM if exist %CD%\src\test\solutionsSample (
@REM     echo "Cleaning solutions sample"
@REM 	rmdir /Q /S %CD%\src\test\solutionsSample
@REM )

if exist %CD%\output\ (
    echo "Cleaning Output..."
    rmdir /Q /S %CD%\output\
)
    echo "Creating Output..."
    mkdir %CD%\output\
    mkdir %CD%\output\test

@REM if exist %CD%\test\solutions\ (
@REM     echo "Copying solution sample"
@REM     mkdir %CD%\src\test\solutionsSample
@REM     robocopy %CD%\test\solutions %CD%\src\test\solutionsSample /NFL /NDL /NJH /NJS /nc /ns /np
@REM )

@REM if exist %CD%\src\test\CheckSuite_old.py (
@REM     echo "Deleting CheckSuite_old.py"
@REM     del %CD%\src\test\CheckSuite_old.py /f /q
@REM )

if exist %CD%\src\test\CodeGenSuite_old.py (
    echo "Deleting CodeGenSuite_old.py"
    del %CD%\src\test\CodeGenSuite_old.py /f /q
)

@REM if exist %CD%\test\check.py (
@REM     echo "Copying check.py"
@REM     robocopy %CD%\test\ %CD%\src\ check.py /NFL /NDL /NJH /NJS /nc /ns /np
@REM )

@REM if exist %CD%\test\LexerSuite.py (
@REM     echo "Rename old LexerSuite.py to LexerSuite_old.py"
@REM     ren %CD%\src\test\LexerSuite.py LexerSuite_old.py
@REM     echo "Copying LexerSuite.py"
@REM     robocopy %CD%\test\ %CD%\src\test\ LexerSuite.py /move /NFL /NDL /NJH /NJS /nc /ns /np
@REM )

@REM if exist %CD%\test\ParserSuite.py (
@REM     echo "Rename old ParserSuite.py to ParserSuite_old.py"
@REM     ren %CD%\src\test\ParserSuite.py ParserSuite_old.py
@REM     echo "Copying ParserSuite.py"
@REM     robocopy %CD%\test\ %CD%\src\test\ ParserSuite.py /move /NFL /NDL /NJH /NJS /nc /ns /np
@REM )

if exist %CD%\test\TestUtils.py (
    echo "Rename old TestUtils.py to TestUtils_old.py"
    ren %CD%\src\test\TestUtils.py TestUtils_old.py
    echo "Copying TestUtils.py"
    robocopy %CD%\test\ %CD%\src\test\ TestUtils.py /NFL /NDL /NJH /NJS /nc /ns /np
)

if exist %CD%\test\AST.py (
    echo "Rename old AST.py to AST_old.py"
    ren %CD%\src\main\bkit\utils\AST.py AST_old.py
    echo "Copying AST.py"
    robocopy %CD%\test\ %CD%\src\main\bkit\utils\ AST.py /NFL /NDL /NJH /NJS /nc /ns /np
)

if exist %CD%\test\CodeGenError.py (
    echo "Rename old CodeGenError.py to CodeGenError_old.py"
    ren %CD%\src\main\bkit\codegen\CodeGenError.py CodeGenError_old.py
    echo "Copying CodeGenError.py"
    robocopy %CD%\test\ %CD%\src\main\bkit\codegen\ CodeGenError.py /NFL /NDL /NJH /NJS /nc /ns /np
)

@REM if exist %CD%\test\StaticError.py (
@REM     echo "Rename old StaticError.py to StaticError_old.py"
@REM     ren %CD%\src\main\bkit\checker\StaticError.py StaticError_old.py
@REM     echo "Copying StaticError.py"
@REM     robocopy %CD%\test\ %CD%\src\main\bkit\checker\ StaticError.py /NFL /NDL /NJH /NJS /nc /ns /np
@REM )

@REM if exist %CD%\src\test\testLexer.py (
@REM     del %CD%\src\test\testLexer.py /f /q
@REM )

@REM if exist %CD%\src\test\testParser.py (
@REM     del %CD%\src\test\testParser.py /f /q
@REM )

cd src

@REM echo "Cleaning and Generatting..."
@REM python run.py clean
@REM python run.py gen

@REM echo.
@REM echo "=============================================="
@REM echo "Testing Lexer..."
@REM python run.py test LexerSuite

@REM cd ..
@REM if exist %CD%\src\test\LexerSuite.txt (
@REM     robocopy %CD%\src\test\ %CD%\output\ LexerSuite.txt /move /NFL /NDL /NJH /NJS /nc /ns /np
@REM     del %CD%\src\test\ParserSuite.txt /f /q
@REM )
@REM cd src

@REM echo.
@REM echo "=============================================="
@REM echo "Testing Parser..."
@REM python run.py test ParserSuite

@REM echo.
@REM echo "=============================================="
@REM echo "Testing ASTGen..."
@REM python run.py test ASTGenSuite

@REM echo.
@REM echo "=============================================="
@REM echo "Testing Check..."
@REM python run.py test CheckSuite

echo.
echo "=============================================="
echo "Testing Code Generation..."
python run.py test CodeGenSuite

@REM cd ..
@REM if exist %CD%\src\test\CheckSuite.txt (
@REM     robocopy %CD%\src\test\ %CD%\output\ CheckSuite.txt /move /NFL /NDL /NJH /NJS /nc /ns /np
@REM )
@REM cd src

@REM cd ..
@REM if exist %CD%\src\test\ParserSuite.txt (
@REM     robocopy %CD%\src\test\ %CD%\output\ ParserSuite.txt /move /NFL /NDL /NJH /NJS /nc /ns /np
@REM     del %CD%\src\test\LexerSuite.txt /f /q
@REM )
@REM cd src

@REM if exist %CD%\test\CheckSuite.py (
@REM     echo "Rename old CheckSuite.py to CheckSuite_old.py"
@REM     ren %CD%\test\CheckSuite.py CheckSuite_old.py
@REM )

@REM if exist %CD%\test\CheckSuite.txt (
@REM     ren %CD%\test\CheckSuite.txt CheckSuite.py
@REM )

if exist %CD%\test\CodeGenSuite.py (
    @REM echo "Rename old CodeGenSuite.py to CodeGenSuite_old.py"
    ren %CD%\test\CodeGenSuite.py CodeGenSuite_old.py
)

if exist %CD%\test\CodeGenSuite.txt (
    ren %CD%\test\CodeGenSuite.txt CodeGenSuite.py
)

@REM if exist %CD%\test\solutionsSample\ (
@REM     if exist %CD%\check.py (
@REM         echo.
@REM         echo "=============================================="
@REM         echo "Checking solution..."
@REM         echo.
@REM         python check.py
@REM     )
@REM )
cd ..

@echo off

@REM if exist %CD%\src\check.txt (
@REM     robocopy %CD%\src\ %CD%\output\ check.txt /move /NFL /NDL /NJH /NJS /nc /ns /np
@REM     start %CD%\output\check.txt
@REM )

@REM if exist %CD%\src\test\LexerSuite_old.py (
@REM     robocopy %CD%\src\test\ %CD%\output\test\ LexerSuite.py /move /NFL /NDL /NJH /NJS /nc /ns /np
@REM     ren %CD%\src\test\LexerSuite_old.py LexerSuite.py
@REM )

@REM if exist %CD%\src\test\ParserSuite_old.py (
@REM     robocopy %CD%\src\test\ %CD%\output\test\ ParserSuite.py /move /NFL /NDL /NJH /NJS /nc /ns /np
@REM     ren %CD%\src\test\ParserSuite_old.py ParserSuite.py
@REM )

if exist %CD%\src\main\bkit\utils\AST_old.py (
    robocopy %CD%\src\main\bkit\utils\ %CD%\output\test\ AST.py /move /NFL /NDL /NJH /NJS /nc /ns /np
    ren %CD%\src\main\bkit\utils\AST_old.py AST.py
)

@REM if exist %CD%\src\main\bkit\checker\StaticError_old.py (
@REM     robocopy %CD%\src\main\bkit\checker\ %CD%\output\test\ StaticError.py /move /NFL /NDL /NJH /NJS /nc /ns /np
@REM     ren %CD%\src\main\bkit\checker\StaticError_old.py StaticError.py
@REM )

if exist %CD%\src\test\TestUtils_old.py (
    robocopy %CD%\src\test\ %CD%\output\test\ TestUtils.py /move /NFL /NDL /NJH /NJS /nc /ns /np
    ren %CD%\src\test\TestUtils_old.py TestUtils.py
)

if exist %CD%\src\main\bkit\codegen\CodeGenError_old.py (
    robocopy %CD%\src\main\bkit\codegen\ %CD%\output\test\ CodeGenError.py /move /NFL /NDL /NJH /NJS /nc /ns /np
    ren %CD%\src\main\bkit\codegen\CodeGenError_old.py CodeGenError.py
)

@REM if exist %CD%\src\check.py (
@REM     robocopy %CD%\src\ %CD%\output\test\ check.py /move /NFL /NDL /NJH /NJS /nc /ns /np
@REM )

@REM if exist %CD%\src\test\solutionsSample\ (
@REM     robocopy %CD%\src\test\solutionsSample\ %CD%\output\test\solutions /move /NFL /NDL /NJH /NJS /nc /ns /np
@REM )

pause >nul