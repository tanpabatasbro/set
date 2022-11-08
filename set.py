list_a = [1,2,3,4,5]
set_a = {19,99}

print('[sebelum]')
print(f" list\t:  {list_a}")
print(f" set\t: {set_a}")

list_a.append(6)
list_a.append(7)

set_a.add(100)
set_a.add(200)

print("[sesudah]")
print(f" list\t: {list_a}")
print(f" set\t: {set_a}")

print("="*10)

list_a = [1, 2, 3, 4]
set_a = {1, 2, 3, 4}

print('[Sebelum]')
print(f'  list\t: {list_a}')
print(f'  set\t: {set_a}')

list_a.remove(2)
#list_a.remove(4)

#set_a.remove(2)
set_a.remove(4)

print('[Sesudah]')
print(f'  list\t: {list_a}')
print(f'  set\t: {set_a}')
