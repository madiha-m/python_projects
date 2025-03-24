
adjective = input('Adjective: ')
name = input('Name: ')
project_type = input('Project Type: ')
device = input('Device: ')
error_message = input('Error Message: ')
verb = input('Verb: ')
random_number = input('Random Number: ')
desperate_action = input('Desperate Action: ')
random_fix = input('Random Fix: ')
funny_lesson = input('Funny Lesson: ')

developer_nightmare = f'It was a {adjective} day when {name} sat down to work on a {project_type} project.  \
    Suddenly, their {device} displayed a {error_message} error!  \
    {name} tried {verb}, but the bug refused to go away.  \
    After {random_number} hours of {desperate_action}, {name} finally fixed it by adding {random_fix}.  \
    \
    Moral of the story: Always {funny_lesson} before coding!  \
    '
print(developer_nightmare)
