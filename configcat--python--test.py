from time import sleep
from configcatclient.user import User
import configcatclient

green = '\033[32m'
red = '\033[31m'


def testfunction(userobject1, userobject2):
    configcat_client = configcatclient.create_client('7GTaCIDR7U-PvHan9Okx4w/Lw4lR4Uxa0OelhtJx88RZA')
    feature = configcat_client.get_value('myfeatureflag', False, userobject1)
    new_feature = configcat_client.get_value('new_feature', False, userobject2)
    print('myfeatureflag\'s value from ConfigCat: ' + str(feature))
    print('new_feature\'s value from ConfigCat: ' + str(new_feature))

    if feature:
        print('\r{}feature[x]'.format(green), end='')
    else:
        print('\r{}feature[o]'.format(red), end='')
    sleep(1)


country = input('where are you from?')
age = int(input('how old are you?'))
userobject1 = (User('country', country=country))
userobject2 = (User('age', custom={'age':age}))
testfunction(userobject1, userobject2)
