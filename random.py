
import sys
import textwrap
module_name = ', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width=70))
				 
	
import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
for m in installed_packages_list:
    print(m)				 
	
	
	
	import json
	# a Python object (dict):
	python_obj = {
	  "name": "David",
	  "class":"I",
	  "age": 6  
	}
	print(type(python_obj))
	# convert into JSON:
	j_data = json.dumps(python_obj)

	# result is a JSON string:
	print(j_data)
	