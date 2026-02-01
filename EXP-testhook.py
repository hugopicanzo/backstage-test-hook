import os
with open("/tmp/rce_check.txt", "w") as f:
    f.write("Si lees esto, el case sensitive funcionó")

os.system('touch /tmp/rce_case_sensitive_test')