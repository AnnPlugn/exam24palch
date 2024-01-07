phones_list = [{'name':'Ivan', 'city':'Moscow', 'phones':['232-19-55', '+7 (916) 230-00-75']},
{'name':'Anna', 'city':'Samara', 'phones':['200-11-15']}, {'name':'Anna', 'city':'Vologda',
'phones':['+7 (931) 711-00-75']}, {'name':'Nikolay', 'city':'Moscow', 'phones':['+7 (916) 778-71-05', '331-66-11', '783-33- 85']},
{'name':'Ivan', 'city':'Moscow', 'phones':['+7 (916) 205-41-05', '232-19-55']}, {'name':'Anna', 'city':'Samara', 'phones':['+7 (916) 105-13-56']}]

def convert_to_dict(contacts):
    result_dict = {}
    for contact in contacts:
        city = contact['city']
        if city in result_dict:
            for phone in contact['phones']:
                result_dict[city][phone] = contact['name']
        else:
            result_dict[city] = {phone: contact['name'] for phone in contact['phones']}
    return result_dict

contacts_dict = convert_to_dict(phones_list)
print(contacts_dict)