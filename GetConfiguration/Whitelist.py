from pathlib import Path

def Check(ip):
    if Path('.\\whitelist.cfg').is_file() == False:
        default_lines = ['#Examples','#','#127.0.0.1','#8.8.8.8']
        with open('.\\whitelist.cfg', "w") as file:
            for line in default_lines:
                file.write(line+'\n')
    with open('.\\whitelist.cfg', "r") as file:
        for line in file:
            if not line.startswith("#"):
                if ip in line:
                    return True
    return False