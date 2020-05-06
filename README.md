[![Gitter chat](https://img.shields.io/badge/gitter-join%20chat-brightgreen.svg)](https://gitter.im/CiscoSecurity/Lobby "Gitter chat")

### Download and save the policy.xml for every policy configured in an organization:
This script collects all of the policies configured in an orgainzation and then saves them to a file in a directory named `policies` located in the same director as the script. The file output format is `os_policy-name_policy-guid.xml`

### Before using you must update the following:
- amp_client_id
- amp_api_key
- amp_host*

\*If the credentials are not in the North American cloud

### Usage:
```
python save_policies.py
```

### Example script output:
```
Number of polices found: 13
13: android_Protect - DONE!
12: ios_Audit - DONE!
11: ios_Protect - DONE!
10: linux_Audit - DONE!
9: linux_Protect - DONE!
8: mac_Audit - DONE!
7: mac_Protect - DONE!
6: mac_Triage - DONE!
5: windows_Audit - DONE!
4: windows_Domain Controller - DONE!
3: windows_Protect - DONE!
2: windows_Server - DONE!
1: windows_Triage - DONE!
```
