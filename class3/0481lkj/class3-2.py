d = {'lizi': 116, 'xxx': 114, 'daiceng': 113, 'xx': 112, 'wangxingxing': 115};
employee_id = 117;
flag = 'false';
for key in d:
    if employee_id == d[key]:
        flag = 'true'
        print key,
        break
    else:
        flag = 'false'
if flag == 'false':
    print 'the employee does not exist',
