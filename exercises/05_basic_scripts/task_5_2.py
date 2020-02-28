# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip = input('Введите IP адрес: ')
mask = input('Введите маску: ')
ip_add = '{}/{}'.format(ip, mask)
ip = ip.split('.')
ip = ', '.join(ip)
mask_spl = '1'*int(mask) + '0'*(32-int(mask))
print(type(ip))

mask1 = int(mask_spl[:8])
mask2 = int(mask_spl[9:16])
mask3 = int(mask_spl[17:24])
mask4 = int(mask_spl[25:])

ip_template = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}

Mask:
'/' mask
int(mask1, 2) int(mask2, 2) int(mask3, 2) int(mask4, 2)
mask1 mask2 mask3 mask4
'''

print(ip_template.format(ip))
