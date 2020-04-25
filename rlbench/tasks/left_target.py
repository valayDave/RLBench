from typing import List
from rlbench.backend.task import Task
from typing import List, Tuple
import numpy as np
from pyrep.objects.shape import Shape
from pyrep.objects.proximity_sensor import ProximitySensor
from rlbench.const import colors
from rlbench.backend.task import Task
from rlbench.backend.spawn_boundary import SpawnBoundary
from rlbench.backend.conditions import DetectedCondition


class LeftTarget(Task):

    def init_task(self) -> None:
        self.target = Shape('target')
        self.boundary = [Shape('boundary')]
        self.boundary1 = Shape('boundary')
        success_sensor = ProximitySensor('success')
        print(self.target.get_position())
        self.workspace=Shape('workspace0')
        self.register_success_conditions(
            [DetectedCondition(self.robot.arm.get_tip(), success_sensor)])


    def init_episode(self, index: int) -> List[str]:
        self._variation_index = index
        color_name, color_rgb = colors[0]
        self.target.set_color(color_rgb)

        self.boundary1.set_position([+1.1921e-07, +2.0000e-01, +1.7500e-01], relative_to=self.workspace)

        b = SpawnBoundary(self.boundary)
        for ob in [self.target]:
            b.sample(ob, min_distance=0.2,
                     min_rotation=(0, 0, 0), max_rotation=(0, 0, 0))

        return ['reach the %s target' % color_name,
                'touch the %s ball with the panda gripper' % color_name,
                'reach the %s sphere' % color_name]



    def variation_count(self) -> int:
        return len(colors)



    def base_rotation_bounds(self) -> Tuple[List[float], List[float]]:
        return [0.0, 0.0, 0.0], [0.0,0.0,0.0]

    def get_low_dim_state(self) -> np.ndarray:
        # One of the few tasks that have a custom low_dim_state function.
        return np.array(self.target.get_position())
