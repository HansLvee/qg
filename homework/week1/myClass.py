import numpy as np

class myClass:
    def __init__(self, vec, axis):
        self.vec = np.array(vec, dtype=float)
        self.axis = np.array(axis, dtype=float)
        self._dis_patch = {
            "axis_projection": self._axis_proj,
            "axis_angle": self._axis_angle,
            "change_axis": self._change_axis,
            "area": self._area
        }

    def do_task(self, task): 
        task_type = task["type"]
        return self._dis_patch[task_type](task)

    def _is_valid_axis(self, axis):
        return np.linalg.det(axis) != 0
    
    def _change_axis(self, task):
        new_axis = np.array(task["obj_axis"])

        #判断坐标系合法性
        if not self._is_valid_axis(new_axis):
            print(f"[{task["group_name"]}]invalid axis\n")

        inv = np.linalg.inv(new_axis)
        self.vec = self.vec @ inv.T
        self.axis = new_axis
        return self.vec
    
    def _axis_proj(self, task=None):
        results = []
        for v in self.vec:
            proj = []
            for a in self.axis:
                proj.append(np.dot(v, a) / np.linalg.norm(a))
            results.append(proj)
        return np.array(results)
    
    def _axis_angle(self, task=None):
        results = []

        for v in self.vec:
            angles = []
            v_norm = np.linalg.norm(v)

            for a in self.axis:
                a_norm = np.linalg.norm(a)
                cos_t = np.dot(v, a) / (v_norm * a_norm)
                angles.append(np.arccos(cos_t))
            results.append(angles)
        return np.array(results)
    
    def _area(self, task=None):
        return abs(np.linalg.det(self.axis))