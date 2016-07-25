#!/usr/bin/env python
import json
import os

import requests
import urlparse

def main():
    module = AnsibleModule(
        argument_spec=dict(
	    ca_key_path=dict(required=True),
            cfssl_url=dict(default='http://localhost:8888'),
            label=dict(default='primary')
	),
        supports_check_mode=True,
    )

    ca_key_path = module.params['ca_key_path']
    cfssl_url = module.params['cfssl_url']
    label = module.params['label']
    changed = False

    if not os.path.exists(ca_key_path):
        if not module.check_mode:
            url = urlparse.urljoin(cfssl_url, '/api/v1/cfssl/info')

            data = {
                'request': {
	             'label': label,
                }
            }

            response = requests.post(url, data=json.dumps(data)).json()
            
	    with open(ca_key_path, 'w') as fp:
                fp.write(response['result']['certificate'])

        changed = True

    module.exit_json(changed=changed)

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
