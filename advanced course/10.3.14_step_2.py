# Вам доступен список pets, содержащий информацию о собаках и их владельцах.
# Каждый элемент списка – это кортеж вида (кличка собаки, имя владельца, фамилия владельца, возраст владельца).
#
# Дополните приведенный код так, чтобы в переменной result хранился словарь,
# в котором для каждого владельца будут перечислены его собаки.
# Ключом словаря должен быть кортеж (имя, фамилия, возраст владельца),
# а значением – список кличек собак (сохранив исходный порядок следования).
#
# Примечание 1. Не забывайте: кортежи являются неизменяeмыми, поэтому могут быть ключами словаря.
#
# Примечание 2. Обратите внимание, что у некоторых владельцев по несколько собак.
#
# Примечание 3. Выводить содержимое словаря result не нужно.

pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}

for item in pets:
        key = tuple(item[1:])
        if key in result:
                result[key].append(item[0])
        else:
                result[key] = [item[0]]

# print(result)



# for pet in pets:
#     result.setdefault(pet[1:], []).append(pet[0])


