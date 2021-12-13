from application import salary as s
from application.db import people as p
from datetime import datetime

if __name__ == '__main__':
    current_time = datetime.now().date()
    print(current_time)
    s.calculate_salary('Саша', 200, 16)
    p.get_employees('Саша', 8, 'bugfixing')
