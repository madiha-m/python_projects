# string cancatenation

adjective = input('Adjective: ')
name = input('Name: ')
project_type = input('Project Type: ')
device = input('Device: ')
verb = input('Verb: ')
error_message = input('Error: ')
random_tech_tool = input('Random: ')
adjective2 = input('Adjective2: ')
random_symbol = input('Random Symbol: ')
snack = input('Snack: ')
funny_activity = input('Funny Activity: ')
random_number = input('Random Number: ')
beverage = input('Beverage: ')
manager_quote = input('Manager Quote: ')

madlib = f'\nOnce upon a time, a {adjective} developer named {name} was working on an important {project_type} project. \
    Everything was going well until suddenly, their {device} crashed!  \
    Panicked, {name} tried {verb} the code, but instead, they got {error_message}. \
        \
    Desperate, they turned to their {random_tech_tool} for help, but it only made things {adjective2}.  \
    After hours of debugging, they realized the issue was caused by a missing {random_symbol}!  \
    Frustrated, {name} took a break, grabbed some {snack}, and started {funny_activity} to calm down.  \
    \
    Finally, after {random_number} cups of {beverage}, they fixed the bug and deployed the project.  \
    But just as they celebrated, their manager walked in and said, **"{manager_quote}"**...  \
    And that’s how {name} learned **never to push code on a Friday!** \n \
'

print(madlib)
