from functions.get_files_info import get_files_info
import os

#print(f"current working directory: {os.getcwd()}")

# 1. get_files_info(calulator, .)
result_from_func = get_files_info("calculator", ".")
lines = result_from_func.split("\n")
indented_lines = []

for line in lines:
    indented_lines.append("  " + line)
final_string = "\n".join(indented_lines)

print("Result for current directory:")
print(final_string)

# 2. get_files_info(calulator, pkg)
result_from_func = get_files_info("calculator", "pkg")
lines = result_from_func.split("\n")
indented_lines = []

for line in lines:
    indented_lines.append("  " + line)
final_string = "\n".join(indented_lines)

print("Result for 'pkg' directory:")
print(final_string)

# 3. get_files_info(calulator, bin)
result_from_func = get_files_info("calculator", "/bin")
lines = result_from_func.split("\n")
indented_lines = []

for line in lines:
    indented_lines.append("  " + line)
final_string = "\n".join(indented_lines)

print("Result for '/bin' directory:")
print(final_string)

# 4. get_files_info(calulator, ../)
result_from_func = get_files_info("calculator", "../")
lines = result_from_func.split("\n")
indented_lines = []

for line in lines:
    indented_lines.append("  " + line)
final_string = "\n".join(indented_lines)

print("Result for '../' directory:")
print(final_string)