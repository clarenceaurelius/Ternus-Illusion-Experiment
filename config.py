# Experiment Mode
DEV_MODE = True
DATA_DIR = "data/dev" if DEV_MODE else "data/trial"
EVENTS_DIR = "events/dev" if DEV_MODE else "events/trial"

# Colour config
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Size config
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 300
DOT_RADIUS = 20
RECTANGLE_SIZE = (35, 35)
CROSS_SIZE = (20, 20)
LINE_WIDTH = 4

# Position config
LEFT_OUTER = (-120, -50) # first element
LEFT_INNER = (-40, -50)  # second element
RIGHT_INNER = (40, -50)  # third element
RIGHT_OUTER = (120, -50) # fourth element

# Trial config
trial_latencies = [0, 50, 500, 1000] # interstimulus interval in milliseconds
trial_repetitions = 10 

# Variable names
condition = "condition"
trial = "trial"
isi = "isi_ms"
frame_duration = "frame_ms"
response = "response"
group_response = "group_response"
key = "key"
rt = "rt_ms"