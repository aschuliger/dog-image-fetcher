import random

def select_topic(collections):
    return random.choice(collections)

def select_images(srcs):
    number_to_select = 12 if len(srcs) > 12 else len(srcs)
    return random.sample(srcs, number_to_select)