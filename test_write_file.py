from functions.write_file import write_file

#result for lorem.txt
result_from_func = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print("result for 'calculator', 'lorem.txt', 'wait, this isn't lorem ipsum'")
print(result_from_func)

#result for pkg/morelorem.txt
result_from_func = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print("result for 'calculator', 'pkg/morelorem.txt', 'lorem ipsum dolor sit amet'")
print(result_from_func)

#result for /tmp/temp.txt
result_from_func = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print("result for 'calculator', '/tmp/temp.txt', 'this should not be allowed'")
print(result_from_func)