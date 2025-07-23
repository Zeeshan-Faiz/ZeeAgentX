import datetime

# Tool: Get current time
def get_current_time(*args, **kwargs):
    import datetime
    return datetime.datetime.now().strftime("%I:%M %p")