# Defining the variables that will set up our optimization problem. Each
# variable has a markdown describing what is its purpose and how it will
# be assessed.
days = 28
workers = 5
shifts = 3

# Defining the number of workers needed for each one of the 3 shifts out of the 28 days.
# During the weekends there is only one shift per day.
workers_per_shift = [2, 1, 1, 1, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 0, 1, 0, 0, 1, 0, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 2, 1,
                     2, 1, 1, 0, 1, 0, 0, 1, 0, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 2, 0, 1, 0, 0, 1, 0, 2, 1, 1,
                     2, 1, 2, 1, 2, 1, 1, 1, 2, 2, 1, 1, 0, 1, 0, 0, 1, 0]

# Defining the preferences of each worker. The value 1 means that the worker would prefer to work in
# that specific shift, the value 0 means that the worker doesn't show any preference for working or
# not in that specific shift. The value -1 means that the worker would prefer not to work in that
# specific shift.
preferences = {0: [-1, 0, 0, 1, 0, -1, 1, 0, 1, 0, 0, 1, -1, 1, 0, -1, 0, 1, 0, 0, 1, 1, 0, -1, 0, 0, 1, 0, 1, 0, 0, -1,
                   1, 0, 0, 1, 0, 1, 0, 0, -1, 0, 0, 1, -1, -1, 0, 1, 0, 1, 1, 0, -1, 0, -1, 0, 1, 0, 1, 0, 1, -1, 0, 1,
                   1, 0, -1, 0, -1, -1, 0, 1, 1, 0, -1, 0, -1, -1, 1, 0, 0, 1, 0, 0],

               1: [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, -1, -1, 0, 1, 0, 1,
                   0, 0, 1, 0, -1, 0, -1, 0, 1, 1, 1, 0, 0, -1, 0, 1, 0, 0, -1, 0, -1, 0, -1, 0, 1, 0, 1, 0, -1, 0, 0,
                   0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, -1, 0, 1, 0, 0, -1, 0, 0],

               2: [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, -1, 0, -1, 0, 1, 0, -1, 0, 0, 1, 0,
                   -1, -1, 0, 0, 0, -1, 0, 0, 0, 0, 1, 0, 1, -1, 0, -1, 0, 0, -1, 0, 1, 0, -1, 0, -1, 0, 0, 1, 0, 0, 0,
                   0, -1, 0, 0, -1, 0, 0, 1, 0, 0, -1, 0, 0, -1, 0, -1, 1, 0, 1, 0, 1],

               3: [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, -1, 0, 0, -1, 0, 0, 1,
                   0, 1, 0, -1, 0, -1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, -1, 0, 1, 0, 0, 0, 1, 0, 1, 0, -1, 0, 1, 1, 0,
                   0, -1, 0, 1, 0, 1, 0, -1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],

               4: [0, 0, 1, 0, -1, 0, -1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, -1, 0, 1, 0, 1, 0, 1, 0, -1, 0, 1,
                   0, -1, 0, -1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, -1, 0, 0, 1, 0, -1, 0, 1, 0, 0, -1, 0, 0, 1, 0, -1, 0,
                   0, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, -1, 0, 0, 1, 0, 0, 1, 0, 0, 0]}

# Each worker have the right to rest 2 days a week.
holidays = {0: [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1,
                1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],

            1: [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],

            2: [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0,
                0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],

            3: [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0,
                0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

            4: [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1]}

# Defining the skills each worker has.
skills = {0: ["skill1", "skill3", "skill5", "skill6"],
          1: ["skill2", "skill7"],
          2: ["skill1", "skill4"],
          3: ["skill1", "skill2", "skill3"],
          4: ["skill3", "skill4", "skill7", "skill8"]}

# Defining the required skills for each specific shift. The majority of the shifts don't require
# a specific skill, but sometimes maybe one or two skills be requires for more specific tasks.
skilled_shifts = {3: ["skill1"], 7: ["skill4"], 14: ["skill2"], 21: ["skill2", "skill3"],
                  25: ["skill7"], 29: ["skill1", "skill5"], 35: ["skill5"], 40: ["skill6"],
                  50: ["skill3"], 54: ["skill3", "skill4"], 63: ["skill8"], 70: ["skill1"],
                  77: ["skill7", "skill8"]}

