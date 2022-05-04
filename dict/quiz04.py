def groups_per_user(group_dictionary):
    user_groups = {}
    for grupo, usuario in group_dictionary.items():
        for y in usuario:
            if y not in user_groups:
                user_groups[y] = []
            if grupo not in user_groups[y]:
                user_groups[y].append(grupo)
          
    return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))



