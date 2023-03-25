import subprocess

# Define the command to run
command = 'tar -czf /tmp/user_backup.tar.gz /home/user && scp /tmp/user_backup.tar.gz user@192.168.1.100:/remote/backup/folder/'

result = subprocess.run(command, shell=True, capture_output=True)

if result.returncode == 0:
    print('Backup created and sent successfully')
else:
    print('Backup creation and sending failed. Error message: ')
    print(result.stderr.decode())