d={'lizi': 116, 'xxx': 114, 'daiceng': 113, 'xx': 112, 'wangxingxing': 115}
employee_id = 117
e={value:key for key,value in d.items()}
f=e.keys()
g=e.values()
if employee_id in f:
    print e[employee_id]
else:
    print 'the employee does not exist'
