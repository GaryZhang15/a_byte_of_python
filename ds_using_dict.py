# 'ab' is short for 'a'ddress'b'ook

ab = {
    'Gary': 'gary@live.com',
    'Zanjoy': 'zanjoy@contoso.com',
    'Lily': 'lily@126.com',
    'Judy': 'judy@qq.com'
}

print("Gary's address is", ab['Gary'])

# delete one key-value pair
del ab['Zanjoy']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at "{}".'.format(name, address))

# add a key-value pair
ab['Joy'] = 'chen@live.com'

if 'Joy' in ab:
    print("\nJoy's address is {}".format(ab['Joy']))
