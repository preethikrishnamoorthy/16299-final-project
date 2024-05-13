from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))

system_message = "You are a robot navigating a house"

START = "Basement"
GOAL = "Bedroom"
locations = ["Kitchen", "Living room", "Dining room", "Basement", "Bedroom"]
actions = ["Find stairs", "Go down stairs", "Go up stairs", "Open door", "Go inside [room name]"]

LOCATIONS = locations[0]
for loc in locations[1:]:
    LOCATIONS += (", " + loc)

ACTIONS = actions[0]
for act in actions[1:]:
    ACTIONS += (", " + act)


prompt = """
You are in a two-story house with a basement. Using what you know about the layout of a standard two-story house, say the next action needed to go from your start position to the goal. Only use actions in the action list.
START: {START}
GOAL: {GOAL}

LOCATIONS: {LOCATIONS}
ACTIONS: {ACTIONS}

Format the response as follows: 
ACTION: [name of action]
REASON: why you are taking this action in one sentence.

Then, I will send you the following:
RESPONSE: the result of the action
SIGHT: what you see after completing the action.

Use the response and sight information when generating the next action. Use information about the standard layout of a house when deciding actions.
You can only go inside of rooms you can see.

Once the goal has been reached, say DONE
""".format(START=START, GOAL=GOAL, LOCATIONS=LOCATIONS, ACTIONS=ACTIONS)

print(prompt)
print("-----------------------")

messages = [{"role": "system", "content": system_message}, 
            {"role": "user", "content": prompt}]

completion = client.chat.completions.create(
        model="gpt-4",
        max_tokens=30,
        messages=messages
    )
response = completion.choices[0].message.content
print(response)

while ("DONE" not in response.upper()):
# while(False):
    messages.append({"role": "assistant", "content": response})

    user_response = input("RESPONSE: ")
    user_sight = input("SIGHT: ")
    print("")

    messages.append({"role": "user", "content": "RESPONSE: {response}\nSIGHT: {sight}".format(response=user_response, sight=user_sight)})

    completion = client.chat.completions.create(
        model="gpt-4",
        max_tokens=30,
        messages=messages
    )
    response = completion.choices[0].message.content
    print(response)

    

    # break