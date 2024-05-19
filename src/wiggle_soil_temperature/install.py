import os
import sys

SERVICE_NAME = 'wiggle-soil-temperature'
SERVICE_FILE = f"{SERVICE_NAME}.service"
SERVICE_DESCRIPTION = 'WiggleSoilTemperature service'

def install():
    # Construct the path to the virtual environment
    python_path = sys.executable
    venv_path = os.path.dirname(python_path)
    script_path = os.path.dirname(os.path.abspath(__file__))

    # Define the content of the service file
    service_content = f"""[Unit]
    Description={SERVICE_DESCRIPTION}
    After=network.target

    [Service]
    WorkingDirectory={script_path}
    ExecStart={python_path} {script_path}/main.py
    Environment="PATH={venv_path}:{os.environ['PATH']}"
    TimeoutStartSec=10min

    [Install]
    WantedBy=default.target
    """

    # Write the content to the service file
    service_file_path = os.path.expanduser(f"~/.config/systemd/user/{SERVICE_FILE}")
    os.makedirs(os.path.dirname(service_file_path), exist_ok=True)
    with open(service_file_path, 'w') as f:
        f.write(service_content)

    os.system(f"systemctl --user enable {SERVICE_FILE}")
    os.system(f"systemctl --user start {SERVICE_FILE}")
