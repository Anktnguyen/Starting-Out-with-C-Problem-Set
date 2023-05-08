"""11. Personal Web page Generator"""

def main():
    html_file = open('html_file.txt', 'w')

    name = input('Enter your name: ')
    desc_self = input('Describe yourself: ')

    #Writing the html script into the file with name and self description
    html_file.write(f'<html>\n'
                    f'<head>\n' 
                    f'</head>\n'
                    f'<body\n'
                    f'  <center>\n'
                    f'      <h1>{name}</h1>\n'
                    f'  </center>\n'
                    f'  <hr />\n'
                    f'  {desc_self}\n'
                    f'  <hr />'
                    f'</body>'
                    f'</html>')
    html_file.close()

    check_file = input('Open file to check yes (y) or no (n): ')

    #open file to check the content, do not use strip to see the indentation
    while check_file == "yes" or check_file == 'y':
        open_file = open('html_file.txt', 'r')
        for line in open_file:
            print(f'{line}')
        check_file = input('Check file one more time yes (y) or no (n): ')
    open_file.close()


if __name__ == "__main__":
    main()