# White-Line-Remover
**white-line-remover.py** is a small script that reads in emails from a file with formatting errors and then creates a new file with the correct formatting. The script only fixes files formatted with blank lines as shown below. 

* emails.txt
```
someone@example.com
someone@example.com

someone@example.com
someone@example.com
someone@example.com

someone@example.com

someone@example.com
```

It reads in each line in the file, stores it in a list, reformats the data by removing the newline character `\n` and filtering out blank strings `""`. It then creates a new file with the emails formatted correctly.

* formatted_emails.txt
```
someone@example.com
someone@example.com
someone@example.com
someone@example.com
someone@example.com
someone@example.com
someone@example.com
```
