# Remove-White-Lines
**white-line-remover** is a small script that reads in a file with formatting errors for emails separated by new lines and blank new lines. It might look something like this: 

emails.txt
```
someone@example.com
someone@example.com

someone@example.com
someone@example.com
someone@example.com

someone@example.com

someone@example.com
```

It reads in each line in the file, stores it in a list, reformats the data by removing the newline character `\n` and filtering out blank strings `""`. It then creates a new file with the emails formatted correctly:

formatted_emails.txt
```
someone@example.com
someone@example.com
someone@example.com
someone@example.com
someone@example.com
someone@example.com
someone@example.com
```
