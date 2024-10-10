retry = True
while retry:
    retry = False
    
    month = input("Введите название месяца: ")
    match month.lower():
        case "январь":
            print("31")
        case "февраль":
            print("28 (29)")
        case "март":
            print("31")
        case "апрель":
            print("30")
        case "май":
            print("31")
        case "июнь":
            print("30")
        case "июль":
            print("31")
        case "август":
            print("31")
        case "сентябрь":
            print("30")
        case "октябрь":
            print("31")
        case "ноябрь":
            print("30")
        case "декарь":
            print("31")
        case _:
            retry = True
            print("Нет месяца с таким названием")
        