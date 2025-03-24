name = input('Name: ')
adjective = input('Adjective: ')
tech_task = input('Tech Task: ')
platform = input('Platform: ')
error_message = input('Error Message: ')
manager_name = input('Manager Name: ')
reaction = input('Reaction: ')
random_deadline = input('Random Deadline: ')
funny_fix = input('Funny Fix: ')
lesson = input('Lesson: ')

overconfident_developer = f'{name} thought they were a {adjective} coder and decided to {tech_task} without testing.  \
Confidently, they pushed their code to {platform}, only to get an email saying **"{error_message}"**.  \
Their manager, {manager_name}, was {reaction} and demanded a fix by {random_deadline}.  \
{name} finally fixed the issue by {funny_fix} and learned that {lesson}.  \
'

print(overconfident_developer)
