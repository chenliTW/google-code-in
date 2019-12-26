 #!/usr/bin/python3
from ansible.module_utils.basic import *
import requests

def main():
  module = AnsibleModule(argument_spec={'url': {'type': 'str', 'required': True}})
  status=requests.get(module.params['url'])
  response = {"return_code": str(status.status_code)}
  module.exit_json(changed=True,meta=response) 
  
if __name__ == "__main__":
  main()
