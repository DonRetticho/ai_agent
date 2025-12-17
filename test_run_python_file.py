from functions.run_python_file import run_python_file

#result for "calculator", "main.py"
result_from_func = run_python_file("calculator", "main.py")
print("result for 'calculator', 'main.py'")
print(result_from_func)

#result for "calculator", "main.py", [3 +5]
result_from_func = run_python_file("calculator", "main.py", ["3 + 5"])
print("result for 'calculator', 'main.py', ['3 + 5']")
print(result_from_func)

#result for "calculator", "tests.py"
result_from_func = run_python_file("calculator", "tests.py")
print("result for 'calculator', 'tests.py'")
print(result_from_func)

#result for "calculator", "../main.py"
result_from_func = run_python_file("calculator", "../main.py")
print("result for 'calculator', '../main.py'")
print(result_from_func)

#result for "calculator", "nonexistent.py"
result_from_func = run_python_file("calculator", "nonexistent.py")
print("result for 'calculator', 'nonexistent.py'")
print(result_from_func)

#result for "calculator", "lorem.txt"
result_from_func = run_python_file("calculator", "lorem.txt")
print("result for 'calculator', 'lorem.txt'")
print(result_from_func)