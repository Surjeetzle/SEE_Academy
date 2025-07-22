admins = {"Surjeet", "Musoiyan"}
editors = {"Vivian", "Surjeet"}

#commbine both groups
all_users = admins.union(editors)

print("All users:", all_users)

both_roles = admins.intersection(editors)
print("Users with both roles:", both_roles)

admin_only = admins.difference(editors)
print("Admins only:", admin_only)