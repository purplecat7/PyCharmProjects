import os.path as op
import yaml

protection_file = "../config/permissions.yaml"
with open(protection_file, 'r') as the_file:
    permissions = yaml.load(the_file)
# save the list of datasets which require specific access
# these are uniquely named product/sub-product combinations
protected_prods = permissions['protected']
print(protected_prods)
print(permissions)



#
# # Put everything in one dictionary to write to yaml
# dict_to_write = {"users": ['user_details'],
#                  "orgs": ['org_details'],
#                  "comments": 'comments'
#                  }
# with open(op.join(op.dirname(op.abspath(__file__)), 'db_data.yaml'), 'w') as outfile:
#     yaml.dump(dict_to_write, outfile, default_flow_style=False)