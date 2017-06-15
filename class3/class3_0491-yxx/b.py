d = {'lizi': 116, 'xxx': 114, 'daiceng': 113, 'xx': 112, 'wangxingxing': 115}
d_new={value:key for key,value in d.items()}
Keys=d_new.keys()
employee_id = 117
if employee_id in Keys:
    print 'exist'
else:
    print 'the employee does not exist'
