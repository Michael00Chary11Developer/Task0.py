def calculator(n, m, li):
    """
    n = تعداد کل اعضای لیست
    m = تقسیم لیست به لیست چند تایی
    li = اعدادی که وارد لیست می کنیم
    """
    # _________________
    groups = [li[i:i + m] for i in range(0, n, m)]

    # groups = []
    # for i in range(0, n, m):
    #     groups.append(li[i:i+m])

    # print(groups)
    """
    li = i to i+m =>slice and create list
    list comprehention
    """
    # _________________
    sums = [sum(gp) for gp in groups]
    """
    باید بیاد هر لیست گروه رو جمع کنه بندازه داخله لیست جدید که جمع هر عضو را در یک لیست ذخیره کرد
    """
    # sums = []
    # for gp in groups:
    #     sums.append(sum(gp))
    # __________________

    """
     این بخش پایینی تقسیم میکن
    """
    valve = 0
    for vl in range(len(sums)):
        if vl % 2 == 0:
            valve += sums[vl]
        else:
            # mean if vl % 2 !=0
            valve -= sums[vl]
            # valve = valve-sum[vl]
    return valve


c1 = calculator(8, 2, [1, 2, 3, 4, 5, 6, 7, 8])
c2 = calculator(8, 3, [1, 2, 3, 4, 5, 6, 7, 8])
print(c1)
print(c2)
