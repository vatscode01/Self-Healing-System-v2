import psutil as ps
import json

def get_data_according_function(function_name):
    func = getattr(ps,function_name)
    data = func()
    return json.dumps(data._asdict(), indent = 4)

def get_stats():
    data = {
        "cpu" : ps.cpu_percent(1),
        "memory" : ps.virtual_memory().percent,
        "disk" : ps.disk_usage('/').percent,
        "tasks" : len(ps.pids()),

    }
    return json.dumps(data, indent=4)

print(get_stats())

