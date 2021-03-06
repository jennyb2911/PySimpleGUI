import PySimpleGUI as sg
"""
Demonstrates using a "tight" layout with a Dark theme.
Shows how button states can be controlled by a user application.  The program manages the disabled/enabled
states for buttons and changes the text color to show greyed-out (disabled) buttons
"""

sg.ChangeLookAndFeel('Dark')
sg.SetOptions(element_padding=(0,0))

layout = [[sg.T('User:', pad=((3,0),0)), sg.OptionMenu(values = ('User 1', 'User 2'), size=(20,1)), sg.T('0', size=(8,1))],
          [sg.T('Customer:', pad=((3,0),0)), sg.OptionMenu(values=('Customer 1', 'Customer 2'), size=(20,1)), sg.T('1', size=(8,1))],
          [sg.T('Notes:', pad=((3,0),0)), sg.In(size=(44,1), background_color='white', text_color='black')],
          [sg.ReadFormButton('Start', button_color=('white', 'black'), key='Start'),
           sg.ReadFormButton('Stop', button_color=('white', 'black'), key='Stop'),
           sg.ReadFormButton('Reset', button_color=('white', 'firebrick3'), key='Reset'),
           sg.ReadFormButton('Submit', button_color=('white', 'springgreen4'), key='Submit')]
          ]

form = sg.FlexForm("Time Tracker", default_element_size=(12,1), text_justification='r', auto_size_text=False, auto_size_buttons=False,
                   default_button_element_size=(12,1))
form.Layout(layout)
form.Finalize()
form.FindElement('Stop').Update(disabled=True)
form.FindElement('Reset').Update(disabled=True)
form.FindElement('Submit').Update(disabled=True)
recording = have_data = False
while True:
    button, values = form.Read()
    print(button)
    if button is None:
        exit(69)
    if button is 'Start':
        form.FindElement('Start').Update(disabled=True)
        form.FindElement('Stop').Update(disabled=False)
        form.FindElement('Reset').Update(disabled=False)
        form.FindElement('Submit').Update(disabled=True)
        recording = True
    elif button is 'Stop' and recording:
        form.FindElement('Stop').Update(disabled=True)
        form.FindElement('Start').Update(disabled=False)
        form.FindElement('Submit').Update(disabled=False)
        recording = False
        have_data = True
    elif button is 'Reset':
        form.FindElement('Stop').Update(disabled=True)
        form.FindElement('Start').Update(disabled=False)
        form.FindElement('Submit').Update(disabled=True)
        form.FindElement('Reset').Update(disabled=False)
        recording = False
        have_data = False
    elif button is 'Submit' and have_data:
        form.FindElement('Stop').Update(disabled=True)
        form.FindElement('Start').Update(disabled=False)
        form.FindElement('Submit').Update(disabled=True)
        form.FindElement('Reset').Update(disabled=False)
        recording = False

