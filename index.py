nameList = []
telefonList = []

with open('Phonebook.vcf', 'r') as lines:

    for line in lines:
        telefon = ""
        name = ""

        if "FN:" in line:
            name = line.split(':')[1].rstrip("\n")
            nameList.append(name)
        if "TEL;TYPE=CELL" in line:
            unformattedTelefon = line.split(':')[1]
            telefon = unformattedTelefon.replace('+49', '0').rstrip("\n")
            telefonList.append(telefon)

    for i in range(0, len(nameList)):
        sqlText = "INSERT INTO d8_members (name, mobil_telefon, address, member_type) VALUES ('{}', '{}', 'BOS', 'Sempatizan');".format(nameList[i], telefonList[i])
        print(sqlText)

