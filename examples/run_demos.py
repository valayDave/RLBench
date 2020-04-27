from rlbench.environment import Environment
from rlbench.action_modes import ArmActionMode, ActionMode
from rlbench.observation_config import ObservationConfig
from rlbench.tasks.left_target import LeftTarget
from rlbench.tasks.right_target import RightTarget
from rlbench.tasks.pick_and_lift import PickAndLift
from rlbench.tasks.reach_and_drag import ReachAndDrag
from rlbench.tasks.put_groceries_in_cupboard import PutGroceriesInCupboard
from rlbench.tasks.pick_up_cup import PickUpCup
from rlbench.tasks.hit_ball_with_queue import HitBallWithQueue
from rlbench.tasks.all_target import AllTarget
# To use 'saved' demos, set the path below, and set live_demos=False
live_demos = True
DATASET = '' if live_demos else '/home/vicky/rlbench_data/'

obs_config = ObservationConfig()
obs_config.set_all(True)

action_mode = ActionMode(ArmActionMode.ABS_JOINT_VELOCITY)
env = Environment(
    action_mode, DATASET, obs_config, False)
env.launch()

task = env.get_task(AllTarget)

demos = task.get_demos(5, live_demos=live_demos)  # -> List[List[Observation]]

print('Done')
env.shutdown()
