from time import sleep

import configcatclient

configcat_client = configcatclient.create_client('7GTaCIDR7U-PvHan9Okx4w/Lw4lR4Uxa0OelhtJx88RZA')


myfeatureflag = configcat_client.get_value('myfeatureflag', False)
new_feature = configcat_client.get_value('new_feature', False)

print('myfeatureflag\'s value from ConfigCat: ' + str(myfeatureflag))
print('new_feature\'s value from ConfigCat: ' + str(new_feature))

green = '\033[32m'
red = '\033[31m'

while True:
    feature = configcat_client.get_value('myfeatureflag',False)
    if feature:
        print('\r{}feature[x]'.format(green), end='')
    else:
        print('\r{}feature[o]'.format(red), end='')
    sleep(1)
    