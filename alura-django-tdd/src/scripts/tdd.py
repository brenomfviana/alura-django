# TDD guidelines
# 1. Write a test to fail;
# 2. Do what is needed for the test to pass;
# 3. Refactor the code to the test to pass.


def calculate_age(birth_year, year):
    return year - birth_year


assert calculate_age(1995, 2050) == 55

print(calculate_age(1995, 2050))

# TDD Advantages
# 1. More objective code;
# 2. Less occurrence of errors;
# 3. Facilitates code refactoring and maintenance;
# 4. Higher productivity in less time;
# 5. Meets system requirements;
# 6. incremental improvement.
