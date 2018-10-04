# VCFtoSQL
VCF to SQL Query Generator with Python

## Getting Started
This script read your .vcf file and generate sql insert row code.


### How to use
* Copy your .vcf file as Phonebook.vcf on the project directory
* Open index.php, and modify 19. line for your table
* Run this script on command prompt or with Python IDE

##### Example Output
```
> python index.php
INSERT INTO d8_members (name, mobil_telefon, address, member_type) VALUES ('John Doe', '0711 89 87 41', 'Empty', 'Member');
INSERT INTO d8_members (name, mobil_telefon, address, member_type) VALUES ('Max Mustermann', '04557 13 32 79', 'Empty', 'Member');
INSERT INTO d8_members (name, mobil_telefon, address, member_type) VALUES ('Ahmet Mehmet', '06569 45 18 61', 'Empty', 'Admin');
```

## License

This project is licensed under the D8L (D8 Developer Licence -  Free to Commercial/Personal use) License


