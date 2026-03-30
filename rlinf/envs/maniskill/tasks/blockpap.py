import sys

# BlockPAP-v1 environment is defined in the RLinf repo.
# Add RLinf to sys.path so the registration import can resolve.
_RLINF_ROOT = "/workspace1/zhijun/RLinf"
if _RLINF_ROOT not in sys.path:
    sys.path.insert(0, _RLINF_ROOT)

import real_franka.real2sim_env.pick_and_place  # noqa: F401  registers BlockPAP-v1

# RL training: randomize block/coaster positions each episode.
# Default is "0" (fixed trajectory), but RL needs random initial states.
real_franka.real2sim_env.pick_and_place.TRAJ_ID = "random"
