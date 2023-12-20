from pprint import pprint
from copy import deepcopy
from math import lcm


modules = {}
low_signals = 0
high_signals = 0
current_button = 0
coding_four = {}


def parse_inp():
    global modules
    with open("2023/dag_20/input.txt", 'r') as file:
        module_lst = [line.strip() for line in file]
    modules_to_update = []
    for module in module_lst:
        if module[0] in "%&":
            m_type, (m_name, output) = module[0], module[1:].split(" -> ")
        else:
            m_type, (m_name, output) = "bc", module.split(" -> ")
        output = output.split(", ")
        modules.update({
            m_name: {
                "type": m_type,
                "output": output,
            }
        })
        if m_type == "%":
            modules[m_name].update({
                "switch": False
            })
        elif m_type == "&":
            modules_to_update.append(m_name)
            modules[m_name].update({
                "last_inputs": {}
            })
    for m_name in modules_to_update:
        last_inputs = []
        for k, v in modules.items():
            if m_name in v["output"]:
                last_inputs.append(k)
        for last_input in last_inputs:
            modules[m_name]["last_inputs"].update({
                last_input: "low"
            })
  
        
def send_signal(m_name, s_type, prev_name):
    global low_signals
    global high_signals
    global modules
    signal_queue = []
    if s_type == "low":
        low_signals += 1
    else:
        high_signals += 1
    if m_name == "rx":
        return signal_queue
    m_type = modules[m_name]["type"]
    if m_type == "%":
        if s_type == "low":
            for out_m_name in modules[m_name]["output"]:
                signal_queue.append((out_m_name, "low" if modules[m_name]["switch"] else "high", m_name))
            modules[m_name]["switch"] = not modules[m_name]["switch"]
    elif m_type == "&":
        modules[m_name]["last_inputs"][prev_name] = s_type
        if all(1 if i == "high" else 0 for i in modules[m_name]["last_inputs"].values()):
            sendtype = "low"
        else:
            if m_name in coding_four and coding_four[m_name] == 0:
                coding_four[m_name] = current_button
            sendtype = "high"
        for out_m_name in modules[m_name]["output"]:
            signal_queue.append((out_m_name, sendtype, m_name))
    return signal_queue
    
        
def button():
    global low_signals
    low_signals += 1
    signal_queue = []
    for m_name in modules["broadcaster"]["output"]:
        signal_queue.extend(send_signal(m_name, "low", "broadcaster"))
    while signal_queue != []:
        n_signal_queue = []
        for m_name, sendtype, prev_name in signal_queue:
            n_signal_queue.extend(send_signal(m_name, sendtype, prev_name))
        signal_queue = deepcopy(n_signal_queue)


def find_rx_coding():
    global coding_four
    for name, vals in modules.items():
        if 'rx' in vals["output"]:
            rx_coding = name
    for name, vals in modules.items():
        if rx_coding in vals["output"]:
            coding_four.update({
                name: 0
            })
        
        
def main():
    global current_button
    parse_inp()
    find_rx_coding()
    
    while True:
        if all(coding_four.values()):
            break
        current_button += 1
        button()
    
    print(lcm(*coding_four.values()))
    
    
if __name__ == "__main__":
    main()
    