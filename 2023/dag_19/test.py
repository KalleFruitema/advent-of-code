from pprint import pprint


wf_dict_global = {}
total = 0


def input():
    with open("2023/dag_19/input.txt", 'r') as file:
        wfs, objs = file.read().split("\n\n")
        wfs = wfs.split("\n")
        objs = objs.split("\n")
    wf_dict = {}
    for line in wfs:
        wf_name, conds = line.strip("}").split("{")
        conds = conds.split(",")
        cond_lst = []
        for cond in conds:
            if ":" in cond:
                cond, result = cond.split(":")
                cond_dict = {
                    "condition": cond,
                    "result": result
                }
            else:
                cond_dict = {
                    "result": cond
                }
            cond_lst.append(cond_dict)
        dic = {
            wf_name: cond_lst
        }
        wf_dict.update(dic)
    
    obj_lst = []
    for line in objs:
        obj_lst.append(line.strip("}{").replace(",", ";"))
        
    return wf_dict, obj_lst
    
    
def get_result(obj, wf_name="in"):
    exec(obj)
    for cond in wf_dict_global[wf_name]:
        if "condition" in cond and eval(cond["condition"]):
            new_name = cond["result"]
            break
        else:
            new_name = cond["result"]
    return new_name

    
def main():
    global wf_dict_global
    wf_dict, obj_lst = input()
    wf_dict_global = wf_dict
    results = []
    for obj in obj_lst:
        new_name = get_result(obj)
        while new_name not in ["A", "R"]:
            new_name = get_result(obj, new_name)
        results.append(new_name)
    total = 0
    for i, obj in enumerate(obj_lst):
        if results[i] == "A":
            exec(obj)
            total += eval("x + m + a + s")
    print(total)
    
    
if __name__ == "__main__":
    main()
    