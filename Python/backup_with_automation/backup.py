import shutil
import datetime
import os

def backup_files(source, destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination, f"backup_{today}.tar.gz")
    shutil.make_archive(backup_file_name.replace('.tar.gz', ''), 'gztar', source)

source = "C:\\Users\\TANMOY\\OneDrive\\Documents\\DevOps\\Python\\Practice"
destination = "C:\\Users\\TANMOY\\OneDrive\\Documents\\DevOps\\Python\\backup_with_automation\\backups_practice"
backup_files(source, destination)