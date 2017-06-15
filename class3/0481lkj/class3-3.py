d = {'lizi': 116, 'xxx': 114, 'daiceng': 113, 'xx': 112, 'wangxingxing': 115}
def findnamebyid ( int ):
    for (k,v) in d.items():
        if v == int:
            return k
            break
employee_id = findnamebyid( 116 )
if employee_id == None:
    print 'the employee does not exist'
else:
    print(employee_id)