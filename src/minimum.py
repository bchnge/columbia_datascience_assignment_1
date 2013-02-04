def compute_minimum(infile):
        import csv
        file = csv.reader(infile)
        headers = file.next()
        listofnum=[]
        for num in file:
                listofnum.append(float(num[0]))
        return min(listofnum)
