import pandas as pd
from myClass import myClass

data = pd.read_json("data1.json")

def tasks_calc(file_path):
    data = pd.read_json(file_path)
    
    for _, row in data.iterrows():
        mc = myClass(row["vectors"], row["ori_axis"])
        
        for task in row["tasks"]:
            result = mc.do_task(task)
            print(f"\ngroup:\t{row["group_name"]}\n \
                      task:\t{task["type"]}\n \
                      {result}")

if __name__ == "__main__":
    tasks_calc("data1.json")