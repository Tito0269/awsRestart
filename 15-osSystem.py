import os
import subprocess
os.system("ls")
"""
subprocess.run(args, *, stdin=None, stdout=None, stderr=None, 
capture_output=False, cwd=None, timeout=None, check=False, encoding=None, 
errors=None, test=None, env=None, universal_newlines=None)
"""
print("-----------------------------------------------------------------------------------------")
subprocess.run(["ls"])
print("-----------------------------------------------------------------------------------------")
subprocess.run(["ls", "-l"])
print("-----------------------------------------------------------------------------------------")
subprocess.run(["ls","-l","README.md"])
print("-----------------------------------------------------------------------------------------")
command="uname"
commandArgument="-a"
print(f'Gardering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
print("-----------------------------------------------------------------------------------------")
command="ps"
commandArgument="-aux"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])
