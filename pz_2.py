def pz_2():
    file = open("pzlin.txt", encoding='utf-8')











def pz_3():
    listOut = []
    while True:
        fileName = input("enter name file")
        if fileName == "quit":
            break
        else:
            try:
                file = open(fileName, encoding='utf-8')
                strFile = file.read()
                listOut.append(strFile)
            except:
                print("file not found")
            finally:
                fileOut = open("result.txt", "w", encoding='utf-8')