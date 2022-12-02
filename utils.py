import subprocess

def shell(command: str):
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         shell=True)

    command_output = ""

    for line in iter(p.stdout.readline, b''):
        command_output += line.decode('utf-8')

    p.stdout.close()
    p.wait()

    return [command_output, p.returncode]