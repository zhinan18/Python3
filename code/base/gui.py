import easygui
user_response = easygui.msgbox("Hello there!")
print(user_response)

#flavor = easygui.buttonbox("What is your favorite ice cream flavor?",choices = ['Vanilla', 'Chocolate', 'Strawberry'] )

flavor = easygui.choicebox("What is your favorite ice cream flavor?",choices = ['Vanilla', 'Chocolate', 'Strawberry'] )
easygui.msgbox ("You picked " + flavor)