import webbrowser

class IncorrectFileException(Exception):
    def __init__(self):
        super().__init__()

try:
    f = open('aboutMe.html','w')

    message = """<!DOCTYPE html>
    <html>
        <head>
            <title>About myself</title>
        </head>
    <body>
        <center>
            <h1>Personal Information</h1>
        </center>
        <div id = "Content1" align ="left">
            <p><b>a. Full name: </b>Maratuly Temirbolat</p>
        </div>
	   <p><b>b. Photo: </b>  </p> <img src ="C:/Users/temir/OneDrive/Рабочий стол/KBTU/Programming on Python/Labs/Lab11/myPhoto.jpg" width = "300" > 
        <div id = "Content2" align = "left">
	   <p><b>c. Age:</b> 20 years old <br/>
	       <b>d. Brief information about yourself: </b> Sometimes quite selfish, from time to time kind and friendly enough:)<br/>
	       <b>e. <ins>Email</ins>: </b>t_maratuly@kbtu.kz<br/>
	       <b>f. Birth country: </b>Kazakhstan<br/>
	       <b>g. Hobbies:</b> Overstudying,playing computer games, going to the gym etc.<br/>
	       <b>h. Study interests</b> All the Programming subjects, Theory of Linear and Non-linear systems, all the Math courses.<br/>
	       <b>i. Knowledge of languages:</b> English (B2 level),Russian (C1 level), Kazakh(A2 level)<br/>
	       <b>j. Programming/IT skills:</b> Knowlendge of Java, C++,C#,Python,ST,LD languages<br/></p>
        </div>
    </body>
    </html>"""

    f.write(message)
    pathFile = input('Please, type the name of the folder to the file: ')
    if (pathFile != 'aboutMe.html'):
        raise IncorrectFileException()
    filename = 'C:/Users/temir/OneDrive/Рабочий стол/KBTU/Programming on Python/Labs/Lab13/' + pathFile
    webbrowser.open_new_tab(filename)

except IncorrectFileException:
    print('That is not file which you needed to open in browser!')
except:
    print('Unexpected Error!')
else:
    print('Work is done successfully! Good job!')
finally:
    print('Good buy!')
    f.close()