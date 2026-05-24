import subprocess

def terraform_run(command):
    process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(process.stdout.decode())

directory = r"C:\Users\TANMOY\OneDrive\Documents\DevOps\Python\project_terra_python\ec2_instance_by_terraform"
# command = f"terraform -chdir={directory} init"
# command = f"terraform -chdir={directory} plan"
# command = f"terraform -chdir={directory} apply -auto-approve"
command = f"terraform -chdir={directory} destroy -auto-approve"

terraform_run(command)
