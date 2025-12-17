from functions.get_file_content import get_file_content

#result for lorem.txt
result_from_func = get_file_content("calculator", "lorem.txt")
print("result for 'calculator', 'lorem.txt'")
print(result_from_func)

#result for main.py in calculator
result_from_func = get_file_content("calculator", "main.py")
print("result for 'calculator', 'main.py'")
print(result_from_func)

#result for pkg/calculator.py in calculator
result_from_func = get_file_content("calculator", "pkg/calculator.py")
print("result for 'calculator', 'pkg/calculator.py'")
print(result_from_func)

#result /bin/cat in calculator
result_from_func = get_file_content("calculator", "/bin/cat")
print("result for 'calculator', '/bin/cat'")
print(result_from_func)

#result for pkg/does_not_exist.py in calculator
result_from_func = get_file_content("calculator", "pkg/does_not_exist.py")
print("result for 'calculator', 'pkg/does_not_exist.py'")
print(result_from_func)