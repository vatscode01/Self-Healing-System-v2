import psutil as ps
import json

# print(psutil.cpu_count(False))
# print(ps.cpu_times())
# print(ps.cpu_percent(None))
# print(ps.virtual_memory())


def get_cpu_times():
    cpu_times =  ps.cpu_times()
    return json.dumps(cpu_times._asdict(), indent=4)

def get_data(function_name):
    func = getattr(ps,function_name)
    data = func()
    return json.dumps(data._asdict(), indent = 4)

print(get_data("cpu_times"))
print(get_data("virtual_memory"))
print(get_data("disk_io_counters"))


# print(get_cpu_times())

