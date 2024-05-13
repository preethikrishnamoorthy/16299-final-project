from openai import OpenAI
import os
import locations
import prompts
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))

#Set start and end locations as well as actions available for the model to take
START = "Basement"
GOAL = "Bedroom"
actions = ["Find stairs", "Go down stairs", "Go up stairs", "Go inside [room name]"]

#Generate prompt
prompt = prompts.get_vision_prompt(START, GOAL, actions)

print("Start location: ", START)
print("Goal location: ", GOAL)
print("=============================================")

#Create array of messages and get the first model response
messages = [{"role": "system", "content": prompts.get_vision_system_message()}, 
            {"role": "user", "content": prompt}]

completion = client.chat.completions.create(
        model="gpt-4-vision-preview",
        max_tokens=100,
        messages=messages
    )
response = completion.choices[0].message.content
print("Model response: ")
print(response)
print("")

#Loop until the model is at the goal location
while ("DONE" not in response.upper()):
    messages.append({"role": "assistant", "content": response})

    #ask the user for what the model sees
    locations.generate_user_location_prompt()
    user_sight = input("LOCATION: ")
    print("=============================================")

    #get the url of the location's image
    url = locations.location_images[int(user_sight)]

    messages.append({"role": "user", "content": "IMAGE: {image_url}".format(image_url=url)})

    completion = client.chat.completions.create(
        model="gpt-4-vision-preview",
        max_tokens=100,
        messages=messages
    )
    response = completion.choices[0].message.content
    print(response)
    print("")
