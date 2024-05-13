import locations

def get_vision_system_message():
    return "You are a robot navigating a house"

def get_vision_prompt(start_loc, goal_loc, actions):
    ACTIONS = actions[0]
    for act in actions[1:]:
        ACTIONS += (", " + act)
    
    location_list = locations.get_location_names()
    LOCATIONS = location_list[0]
    for loc in location_list[1:]:
        LOCATIONS += (", " + loc)

    prompt = """
    You are in a two-story house with a basement. Using what you know about the layout of a standard two-story house, say the next action needed to go from your start position to the goal. Only use actions in the action list.
    START: {START}
    GOAL: {GOAL}

    LOCATIONS: {LOCATIONS}
    ACTIONS: {ACTIONS}

    Format the response as follows: 
    LOCATION: where you are based on the image input
    ANALYSIS: anything of note you see that will help reach the goal
    ACTION: [name of action]
    REASON: why you are taking this action in one sentence.

    Then, I will send you the following:
    IMAGE: your visual input after completing the action

    Use the response and sight information when generating the next action. Use information about the standard layout of a house when deciding actions.
    You can only go inside of rooms you can see.

    Once the goal has been reached, say DONE
    """.format(START=start_loc, GOAL=goal_loc, LOCATIONS=LOCATIONS, ACTIONS=ACTIONS)

    return prompt

