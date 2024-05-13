## Set up

### Package installation
`pip install -r requirements.txt`

### OpenAI API key
1. Follow this link here to create an API key: https://www.maisieai.com/help/how-to-get-an-openai-api-key-for-chatgpt
2. Create a .env file with `OPENAI_API_KEY = {your API key}`

## File structure
- `text_based.py`: contains basic functionality for text-based inputs (i.e., the user has to enter text-based information of the robot's current location)
- `image_based.py`: contains functionality for image-based inputs (i.e., the user enters what the robot sees, and the model is fed an image of that location)
    - `locations.py`: contains all location names and image urls for each location, as well as functions to interact with the locations
    - `prompts.py`: contains the initial prompt given to the model

## Using text-based navigation
**File: `text_based.py`**
### Updating the robot's environment
- Update `START` and `GOAL` to change the start and end points
- Update `locations` to change the rooms & locations available
- Update `actions` to change what the robot can do
- Update `prompt` to change the initial prompt the model is given

### Running the code
**Run `python text_based.py`**

The model will output an *ACTION* and a *REASON*. *ACTION* is the step the model takes based on the list of actions provided. *REASON* is the model's reasoning behind the action taken.

You will then be prompted with two fields: *RESPONSE* and *SIGHT*. Both fields are meant to simulate the robot recieving some sort of visual input of its surroundings.
- *RESPONSE* is the robot's response to the action. Was it successful? Was it able to move to the location specified?
- The *SIGHT* field is a text-based description of what the robot sees. Does it see the correct room? Are there any doors the robot should be aware of?

Once the robot has reached its goal, the model will respond with *DONE* and the program will exit.


## Using image-based navigation
**Files: `image_based.py`, `locations.py`, `prompts.py`**
### Updating the robot's environment
- `image_based.py`: Update `START`, `GOAL`, and `actions` to change the start and end points and actions available for the robot to take
- `locations.py`: Add or remove locations and image URLs to `location_images` to change the  locations available and what they look like
- `prompts.py`: Update the prompt in `get_vision_prompt` to change the initial prompt the model is given

### Running the code
**Run `python image_based.py`**

The model will output a list of four things:
- *LOCATION*: What the model has determined as the current location given the image provided
- *ANALYSIS*: Any other important information the model gets from the image
- *ACTION*: the step the model takes based on the list of actions provided
- *REASON*: the model's reasoning behind the action taken.

You will then be prompted with a list of locations. These correspond to images the model will be fed to make its next decision. Enter the number of the location the model is at based on the model's latest action.

Once the robot has reached its goal, the model will respond with *DONE* and the program will exit.