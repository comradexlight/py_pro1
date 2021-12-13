def calculate_salary(employee_name, payment_per_hour, hours):
    print(
        f'сотрудник {employee_name} заработал {payment_per_hour * hours} денег за {hours} часов \nсотрудник {employee_name} молодец')
    return


if __name__ == '__main__':
    calculate_salary('Влад', 200, 12)
