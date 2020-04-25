from rlbench.environment import Environment
from rlbench.action_modes import ArmActionMode, ActionMode
from rlbench.observation_config import ObservationConfig
from rlbench.tasks.left_target import LeftTarget


# To use 'saved' demos, set the path below, and set live_demos=False
live_demos = False
DATASET = '' if live_demos else '/home/vicky/rlbench_data/'

obs_config = ObservationConfig()
obs_config.set_all(True)

action_mode = ActionMode(ArmActionMode.ABS_JOINT_VELOCITY)
env = Environment(
    action_mode, DATASET, obs_config, False)
env.launch()

task = env.get_task(LeftTarget)

demos = task.get_demos(10, live_demos=live_demos)  # -> List[List[Observation]]

print('Done')
env.shutdown()
