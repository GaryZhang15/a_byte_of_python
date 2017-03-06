bri = set(['brazil','russia','india'])

if 'india' in bri:
    print('Find india in: ', bri)
else:
    pass

if 'usa' in bri:
    print('Find USA in: ', bri)
else:
    print('Not found usa in: ', bri)

bric = bri.copy()
bric.add('china')

bric.issuperset(bri)

bri.remove('russia')
bri & bric


