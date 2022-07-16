def mergeSort(array, lenght):
    if lenght > 1:
        a = mergeSort(array[:lenght // 2], lenght // 2)
        b = mergeSort(array[lenght // 2:], lenght - lenght // 2)
        ia = 0
        ib = 0
        array = []
        while ia < lenght // 2 and ib < lenght - lenght // 2:
            if a[ia] < b[ib]:
                array.append(a[ia])
                ia += 1
            else:
                array.append(b[ib])
                ib += 1
        while ia < lenght // 2:
            array.append(a[ia])
            ia += 1   
        while ib < lenght - lenght // 2:
            array.append(b[ib])
            ib += 1
    return array