import json

json_string = "hello world"
json_int = '541'
json_float = '45.128'
json_dict = '{"name":"dz", "age":"11"}'
json_list = '["farhan","saif"]'

py_int = json.loads(json_int)
py_float = json.loads(json_float)
py_dict = json.loads(json_dict)
py_list = json.loads(json_list)


print('python interger: ',py_int)
print('python float :', py_float)
print('python dictionary: ',py_dict)
print('python list :',py_list)