phones_list = [
    {'name': 'Ivan', 'city': 'Moscow', 'phones': ['232-19-55', '+7 (916) 230-00-75']},
    {'name': 'Anna', 'city': 'Samara', 'phones': ['200-11-15']},
    {'name': 'Anna', 'city': 'Vologda', 'phones': ['+7 (931) 711-00-75']},
    {'name': 'Nikolay', 'city': 'Moscow', 'phones': ['+7 (916) 778-71-05', '331-66-11', '783-33-85']},
    {'name': 'Ivan', 'city': 'Moscow', 'phones': ['+7 (916) 205-41-05', '232-19-55']},
    {'name': 'Anna', 'city': 'Samara', 'phones': ['+7 (916) 105-13-56']}
]

def merge_contacts(contacts):
    merged_contacts = {}
    for contact in contacts:
        key = (contact['name'], contact['city'])
        if key in merged_contacts:
            merged_contacts[key]['phones'].extend([phone for phone in contact['phones'] if phone not in merged_contacts[key]['phones']])
        else:
            merged_contacts[key] = contact
    return list(merged_contacts.values())

unique_contacts = merge_contacts(phones_list)
print(unique_contacts)