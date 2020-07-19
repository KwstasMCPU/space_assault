from gym.envs.registration import register
 
register(id='SpaceAssault-v0', 
    entry_point='space_assault.envs:SpaceAssault', 
)