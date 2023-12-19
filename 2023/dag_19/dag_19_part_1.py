from pprint import pprint


wf_dict_global = {}
total = 0


def input():
    with open("2023/dag_19/input_test1.txt", 'r') as file:
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
                    "category": cond[0],
                    "operator": cond[1],
                    "targetval": cond[2:],
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
        obj_lst.append(eval(line.replace("{", "{'").replace(",", ",'").replace("=", "':")))
        
    return wf_dict, obj_lst
    
    
def get_result(obj, wf_name="in"):
    

    
def main():
    global wf_dict_global
    wf_dict, obj_lst = input()
    wf_dict_global = wf_dict
    for obj in obj_lst:
        
    
    
if __name__ == "__main__":
    main()
    