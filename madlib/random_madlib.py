from sample_madlibs import developer_nightmare, life_of_developer, overconfident_developer
import random

if __name__ == '__main__':
    m = random.choice(
        [developer_nightmare, life_of_developer, overconfident_developer])
    m.madlib()
