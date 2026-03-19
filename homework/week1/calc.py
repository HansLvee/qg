import numpy as np

def to_array(x):
    return np.array(x)

def axis_angle(vec, axis, deg=False):
    # clip用以消除可能的浮点误差
    dot = vec @ axis.T
    v_norm = np.linalg.norm(vec, axis=1, keepdims=True)
    a_norm = np.linalg.norm(axis)

    if np.isclose(v_norm, 0):
        raise ValueError("zero vec exists")

    cos_t = dot / (v_norm * a_norm)
    rad = np.arccos(np.clip(cos_t, -1.0, 1.0))
    if deg:
        return np.rad2deg(rad)
    return rad

def change_axis(vec, new_axis):
    return vec @ np.linalg.inv(new_axis).T

def area(vec):
    cov = np.cov(vec.T)
    return np.sqrt(np.linalg.det(cov))

def axis_proj(vec, axis):
    axis = axis / np.linalg.norm(axis, axis=1, keepdims=True)
    return vec @ axis.T

