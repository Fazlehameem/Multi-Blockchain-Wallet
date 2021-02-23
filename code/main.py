import subprocess
import json



command = 'php derive -g --mnemonic="wish mistake trumpet title tonight desert web cannon tumble pause lemon prepare" --cols=path,address,privkey,pubkey'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

(output, error) = p.communicate()
p_status = p.wait()

print(output)








