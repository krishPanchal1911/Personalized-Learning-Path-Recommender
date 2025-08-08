from .data.courses import course_data, youtube_links

def generate_learning_path(skill, goal):
    """Generate a learning path based on skill and goal"""
    courses = course_data.get(skill, [])
    return courses

def get_youtube_links(skill, goal):
    return youtube_links.get(skill, [])
