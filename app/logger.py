from monitor import get_stats
from pathlib import Path
import json

config_file = Path(Path(__file__).parent).parent / "config" / "config.json"

with open(config_file, 'r') as f:
    config = json.load(f)
stats = get_stats()

def check_cpu():
    if(stats['cpu'] > config['cpu_warning']):
        if(stats['cpu'] > config['cpu_critical']):
            return "Danger"
        else:
            return "Warning"
    return "Normal"

def check_memory():
    if(stats['memory'] > config['memory_warning']):
        if(stats['memory'] > config['memory_critical']):
            return "Danger"
        else:
            return "Warning"
    return "Normal"

def check_disk():
    if(stats['disk'] > config['disk_warning']):
        if(stats['disk'] > config['disk_critical']):
            return "Danger"
        else:
            return "Warning"
    return "Normal"

