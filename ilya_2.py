#Вариант 4
def flatten_dict(nested_dict, parent_key = "", separator = "."):
	items = []
	for k,v in nested_dict.items():
		new_key = f"{parent_key}{separator}{k}" if parent_key else k
		if isinstance(v, dict):
			items.extend(flatten_dict(v, new_key, separator).items())
		else:
			items.append((new_key,v))
	return dict(items)

dict_1 = {"a":{"b":{"c":1}}}

print(flatten_dict(dict_1))
	