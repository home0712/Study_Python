## leap year: 윤년 계산하기
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.

# 4로 나누어 떨어짐: 윤년
# 4로 나눠짐 && 100으로 나눠지면: 평년
# 4로 나눠짐 && both 100과 400 으로 나눠지면: 윤년


def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            leap = True
        elif year % 100 != 0 and year % 400 != 0:
            leap = True

    return leap
