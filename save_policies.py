import os
import requests

# AMP for Endpoint API Credentials
amp_client_id = 'a1b2c3d4e5f6g7h8i9j0'
amp_api_key = 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'
amp_host = 'api.amp.cisco.com'

# Setup AMP for Endpoints session and auth
session = requests.session()
session.auth = (amp_client_id, amp_api_key)

# Policies URL
url = f'https://{amp_host}/v1/policies'

# Get First page of Polices
response = session.get(url)

# Decode JSON response
response_json = response.json()

# Store policy link, product, and name in a dict {'link' : 'product_name'}
policies = {
    policy["links"]["policy"]: f'{policy["product"]}_{policy["name"]}'
    for policy in response_json["data"]
}

# Paginate if needed
while 'next' in response_json['metadata']['links']:
    next_url = response_json['metadata']['links']['next']
    response = session.get(next_url)
    response_json = response.json()
    for policy in response_json['data']:
        # Store link, product, and name in existing dictionary
        policies[policy['links']['policy']] = f'{policy["product"]}_{policy["name"]}'

# Get script file path
path = os.path.dirname(os.path.realpath(__file__))

# Build absolute path for 'policies' dir
output_path = os.path.join(path, 'policies')

# Check if output_path exists, create if not
if not os.path.exists(f'{output_path}'):
    os.makedirs(f'{output_path}')

print(f'Number of polices found: {len(policies)}')

# Iterate over policies, download and save the XML to disk
for count, (policy_link, name) in enumerate(policies.items(), start=1):
    print(f'{(len(policies)+1)-count }: {name}', end=' ')
    guid = policy_link.split('/')[-1]
    response = session.get(f'{policy_link}.xml')
    with open(f'{output_path}/{name}_{guid}.xml', 'w') as f:
        f.write(response.text)
    print('- DONE!')

