try :

    sentence1 = input('ป้อนประโยคภาษาอังกฤษ :')

    senlist = sentence1.split(' ')

    print(f'ในประโยค มีคำรวมกันทั้งหมด {len(senlist)} คำ')

    sametext = list()

    for i in senlist:
        number = senlist.count(i)
    if number > 1:
        sametext.append(i)

    sametext2 = set(sametext)
    
    print(f"มีคำที่ซ้ำกันรวม {len(sametext2)} คำ คือ {' '. join(str(i) for i in sametext2)}")
    
    fill_list = list()
    
    for  i in senlist:
        number = senlist.count(i)
        if number > 1 and not fill_list.count(i) > 0 :
            fill_list.append(i)
            print(f"คำว่า {i} {number} ครั้ง")





except Exception :
    pass

