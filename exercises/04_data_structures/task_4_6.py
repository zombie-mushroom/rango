# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

ospf_route = ospf_route.replace('O', 'OSPF')
table = ospf_route.split()
del table[3]
table = [i.split(',')[0] for i in table]
table = [i.strip('[]') for i in table]
table_prfx = ['Protocol:', 'Prefix:', 'AD/Metric:', 'Next-Hop:', 'Last update:', 'Outbound Inteface:']
for table_prfx, table in zip(table_prfx, table):
    print('{:24}{:24}'.format(table_prfx, table))
