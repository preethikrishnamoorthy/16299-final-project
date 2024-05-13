location_images = [
    {"name": "Basement" , "url": "https://www.nashvillesmls.com/uploads/agent-1/what-are-the-different-types-of-basements.jpg"},
    {"name": "Bedroom" , "url": "https://www.southernliving.com/thmb/_D9Bg0Owp7Jh6_V4kQoINDkKTSc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/27566_IdeaHouse15660F-1905e09febe248c4ab47eff5cdbf468d-62d993a843b24796aab125080d8482cf.jpg"},
    {"name": "Dining Room" , "url": "https://www.bhg.com/thmb/rvOm4fbrqM3Kv-tT2tqIn0VKljY=/3958x0/filters:no_upscale():strip_icc()/Midcentury-modern-dining-room-HGQ36597-E78HH53cq_eA6d2sgX1v8t-b8a6ea0f544f43d59feabcc6aba6a546.jpg"},
    {"name": "Kitchen" , "url": "https://hgtvhome.sndimg.com/content/dam/images/hgtv/fullset/2020/6/16/0/IO_Zoe-Feldman_Georgetown-Condo-18.JPG.rend.hgtvcom.1280.720.suffix/1592340091874.jpeg"},
    {"name": "Living Room" , "url": "https://media.architecturaldigest.com/photos/62f3c04c5489dd66d1d538b9/16:9/w_2560%2Cc_limit/_Hall_St_0256_v2.jpeg"},
    {"name": "Second Floor Hallway" , "url": "https://static1.squarespace.com/static/5c9fd52efd6793726b131b46/t/5ca3dfdf0cf24e5d5465da48/1554243551150/1000w/"},
    {"name": "Stairs down from 1st floor to basement" , "url": "https://cdn.treehouseinternetgroup.com/uploads/photo_gallery/medium/143370-594959b6e2fc4_cropped-2.jpg"},
    {"name": "Stairs up from basement to 1st floor" , "url": "https://www.effierow.com/wp-content/uploads/2017/03/IMG_4802-683x1024.jpg"},
    {"name": "Stairs down from 2nd floor to 1st floor" , "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.dreamstime.com%2Fstairs-house-leading-upstairs-going-down-staircase-image230287023&psig=AOvVaw3-525fWMxVP5EvB0dKFzNf&ust=1715642339661000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCKixo_ifiYYDFQAAAAAdAAAAABAJ"},
    {"name": "Stairs up from 1st floor to 2nd floor" , "url": "https://assets-global.website-files.com/573b7bd29e2dc7c46dee8d5b/60ac1f04b031874f07c9e5b5_Park%20moving%20stairs%20floorplan.jpg"},
]


def generate_user_location_prompt():
    print("What does the robot see?")
    for idx, loc in enumerate(location_images):
        print(idx, ":", loc["name"])

def find_url(name):
    for loc in location_images:
        if name.lower() in loc["name"].lower():
            return loc["url"]
        
def get_location_names():
    locations = []
    for loc in location_images:
        if "stairs" not in loc["name"].lower():
            locations.append(loc["name"])
    return locations