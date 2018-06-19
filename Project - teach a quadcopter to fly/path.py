import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np
from physics_sim import PhysicsSim

def plot3d(self, x, y, z, **kwargs):
    self.scatter([x], [y], [z], **kwargs)
    self.text(x, y, z, "({:.1f}, {:.1f}, {:.1f})".format(x, y, z), ha = 'right')


def flight_path(results, target=None):
    results = np.array(results)
    
    fig = plt.figure(figsize=(10,10))
    self = fig.gca(projection='3d')
    self.set_xlabel('Lateral Axis (m)')
    self.set_ylabel('Longitudinal Axis (m)')
    self.set_zlabel('Vertical Axis (m)')

    self.plot3D(results[:, 0], results[:, 1], results[:, 2])
    
    if target is not None:
        plot3d(self, *target[0:3], c='y', marker='*', s=100, label='target_end_pos')
        plot3d(self, *results[0, 0:3], c='b', marker='o', s=50, label='start_pos')
        plot3d(self, *results[-1, 0:3], c='r', marker='o', s=50, label='actual_end_pos')
    
    self.legend()