import time
from random import randint
import PySimpleGUI as sg

# A simple blocking form.   Your best starter-form
def SourceDestFolders():
    with sg.FlexForm('Demo Source / Destination Folders') as form:
        form_rows = ([sg.Text('Enter the Source and Destination folders')],
                     [sg.Text('Source Folder', size=(15, 1), justification='right'), sg.InputText('Source', key='source'), sg.FolderBrowse()],
                     [sg.Text('Destination Folder', size=(15, 1), justification='right'), sg.InputText('Dest', key='dest'), sg.FolderBrowse()],
                     [sg.Submit(), sg.Cancel()])

        button, values = form.LayoutAndRead(form_rows)
    if button is 'Submit':
        sg.MsgBox('Submitted', values, 'The user entered source:', values['source'], 'Destination folder:', values['dest'], 'Using button', button)
    else:
        sg.MsgBoxError('Cancelled', 'User Cancelled')


def MachineLearningGUI():
    sg.SetOptions(text_justification='right')
    form = sg.FlexForm('Machine Learning Front End', font=("Helvetica", 12))  # begin with a blank form

    layout = [[sg.Text('Machine Learning Command Line Parameters', font=('Helvetica', 16))],
              [sg.Text('Passes', size =(15, 1)), sg.Spin(values=[i for i in range(1, 1000)], initial_value=20, size=(6, 1)),
               sg.Text('Steps', size=(18, 1)), sg.Spin(values=[i for i in range(1, 1000)], initial_value=20, size=(6, 1))],
              [sg.Text('ooa', size=(15, 1)), sg.In(default_text='6', size=(10, 1)), sg.Text('nn', size=(15, 1)), sg.In(default_text='10', size=(10, 1))],
              [sg.Text('q', size=(15, 1)), sg.In(default_text='ff', size=(10, 1)), sg.Text('ngram', size=(15, 1)), sg.In(default_text='5', size=(10, 1))],
              [sg.Text('l', size=(15, 1)), sg.In(default_text='0.4', size=(10, 1)), sg.Text('Layers', size=(15, 1)), sg.Drop(values=('BatchNorm', 'other'),auto_size_text=True)],
              [sg.Text('_' * 100, size=(65, 1))],
              [sg.Text('Flags', font=('Helvetica', 15), justification='left')],
              [sg.Checkbox('Normalize', size=(12, 1), default=True), sg.Checkbox('Verbose', size=(20, 1))],
              [sg.Checkbox('Cluster', size=(12, 1)), sg.Checkbox('Flush Output', size=(20, 1), default=True)],
              [sg.Checkbox('Write Results', size=(12, 1)), sg.Checkbox('Keep Intermediate Data', size=(20, 1))],
              [sg.Text('_' * 100, size=(65, 1))],
              [sg.Text('Loss Functions', font=('Helvetica', 15), justification='left')],
              [sg.Radio('Cross-Entropy', 'loss', size=(12, 1)), sg.Radio('Logistic', 'loss', default=True, size=(12, 1))],
              [sg.Radio('Hinge', 'loss', size=(12, 1)), sg.Radio('Huber', 'loss', size=(12, 1))],
              [sg.Radio('Kullerback', 'loss', size=(12, 1)), sg.Radio('MAE(L1)', 'loss', size=(12, 1))],
              [sg.Radio('MSE(L2)', 'loss', size=(12, 1)), sg.Radio('MB(L0)', 'loss', size=(12, 1))],
              [sg.Submit(), sg.Cancel()]]
    button, values = form.LayoutAndRead(layout)
    del(form)
    sg.SetOptions(text_justification='left')

    return button, values

# YOUR BEST STARTING POINT
# This is a form showing you all of the basic Elements (widgets)
# Some have a few of the optional parameters set, but there are more to choose from
# You want to use the context manager because it will free up resources when you are finished
# Use this especially if you are runningm multi-threaded
# Where you free up resources is really important to tkinter
def Everything():

    with sg.FlexForm('Everything bagel', auto_size_text=True, default_element_size=(40, 1)) as form:
        layout = [
            [sg.Text('All graphic widgets in one form!', size=(30, 1), font=("Helvetica", 25))],
            [sg.Text('Here is some text.... and a place to enter text')],
            [sg.InputText()],
            [sg.Checkbox('My first checkbox!'), sg.Checkbox('My second checkbox!', default=True)],
            [sg.Radio('My first Radio!     ', "RADIO1", default=True), sg.Radio('My second Radio!', "RADIO1")],
            [sg.Multiline(default_text='This is the default Text should you decide not to type anything',size=(35,3)),
             sg.Multiline(default_text='A second multi-line',size=(35,3))],
            [sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(20, 3)),
             sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],
            [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3', 'Listbox 4'), size=(30, 3)),
             sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25),
             sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
             sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),
             sg.Spin(values=('Spin Box 1', '2','3'), initial_value='Spin Box 1')],
            [sg.Text('_' * 80)],
            [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('Default Folder'), sg.FolderBrowse()],
            [sg.Submit(), sg.Cancel()] ]

        button, values = form.LayoutAndRead(layout)

    sg.MsgBox('Title', 'The results of the form.', 'The button clicked was "{}"'.format(button), 'The values are', values)

# Should you decide not to use a context manager, then try this form as your starting point
# Be aware that tkinter, which this is based on, is picky about who frees up resources, especially if
# you are running multithreaded
def Everything_NoContextManager():
    form = sg.FlexForm('Everything bagel', default_element_size=(40, 1))
    layout = [
        [sg.Text('All graphic widgets in one form!', size=(30, 1), font=("Helvetica", 25))],
        [sg.Text('Here is some text.... and a place to enter text')],
        [sg.InputText('This is my text')],
        [sg.Checkbox('My first checkbox!'), sg.Checkbox('My second checkbox!', default=True)],
        [sg.Radio('My first Radio!     ', "RADIO1", default=True), sg.Radio('My second Radio!', "RADIO1")],
        [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),
         sg.Multiline(default_text='A second multi-line', size=(35, 3))],
        [sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(20, 3)),
         sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],
        [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),
         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25),
         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),
         sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],
        [sg.Text('_' * 80)],
        [sg.Text('Choose A Folder', size=(35, 1))],
        [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),
         sg.InputText('Default Folder'), sg.FolderBrowse()],
        [sg.Submit(), sg.Cancel()]
         ]

    button, values = form.LayoutAndRead(layout)
    del(form)

    sg.MsgBox('Title', 'The results of the form.', 'The button clicked was "{}"'.format(button), 'The values are', values)


def ProgressMeter():
    for i in range(1,1000):
        if not sg.EasyProgressMeter('My Meter', i + 1, 1000, orientation='h'): break
        time.sleep(.01)

# Blocking form that doesn't close
def ChatBot():
    with sg.FlexForm('Chat Window', auto_size_text=True, default_element_size=(30, 2), default_button_element_size=(10,2)) as form:
        layout = [[(sg.Text('This is where standard out is being routed', size=(40, 1)))],
                  [sg.Output(size=(80, 20), font=('Courier 10'))],
                  [sg.Multiline(size=(70, 5), enter_submits=True), sg.ReadFormButton('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True), sg.SimpleButton('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]
        # notice this is NOT the usual LayoutAndRead call because you don't yet want to read the form
        # if you call LayoutAndRead from here, then you will miss the first button click
        form.Layout(layout)
        # ---===--- Loop taking in user input and using it to query HowDoI web oracle --- #
        while True:
            button, value = form.Read()
            if button is not 'SEND':
                break
            print(value[0])

# Shows a form that's a running counter
# this is the basic design pattern if you can keep your reading of the
# form within the 'with' block.  If your read occurs far away in your code from the form creation
# then you will want to use the NonBlockingPeriodicUpdateForm example
def NonBlockingPeriodicUpdateForm_ContextManager():
    with sg.FlexForm('Running Timer', auto_size_text=True) as form:
        text_element = sg.Text('', size=(15, 2), font=('Helvetica', 20), text_color='red', justification='center')
        layout = [[sg.Text('Non blocking GUI with updates', justification='center')],
                  [text_element],
                  [sg.T(' ' * 22), sg.Quit()]]
        form.LayoutAndRead(layout, non_blocking=True)

        for i in range(1,500):
            text_element.Update('{:02d}:{:02d}.{:02d}'.format((i // 100) // 60, (i // 100) % 60, i % 100))
            button, values = form.ReadNonBlocking()
            if values is None or button is 'Quit':      # if user closed the window using X
                break
            time.sleep(.01)
        else:
            # if the loop finished then need to close the form for the user
            form.CloseNonBlockingForm()

# Use this context-manager-free version if your read of the form occurs far away in your code
# from the form creation (call to LayoutAndRead)
def NonBlockingPeriodicUpdateForm():
    # Show a form that's a running counter
    form = sg.FlexForm('Running Timer', auto_size_text=True)
    text_element = sg.Text('', size=(10, 2), font=('Helvetica', 20), justification='center')
    form_rows = [[sg.Text('Stopwatch')],
                 [text_element],
                 [sg.T(' ' * 5), sg.ReadFormButton('Start/Stop', focus=True), sg.Quit()]]

    form.LayoutAndRead(form_rows, non_blocking=True)

    timer_running = True
    i = 0
    while True:
        i += 1 * (timer_running is True)
        button, values = form.ReadNonBlocking()
        if values is None or button is 'Quit':      # if user closed the window using X or clicked Quit button
            break
        elif button is 'Start/Stop':
            timer_running = not timer_running
        text_element.Update('{:02d}:{:02d}.{:02d}'.format((i//100)//60, (i//100)%60, i%100))

        time.sleep(.01)
        # if the loop finished then need to close the form for the user
    form.CloseNonBlockingForm()
    del(form)

def DebugTest():
    # SG.Print('How about we print a bunch of random numbers?', , size=(90,40))
    for i in range (1,300):
        sg.Print('Here are 300 random numbers', i, randint(1, 1000), sep='-')

# Change the colors and set borders to 0 for a flat look
def ChangeLookAndFeel(colors):
    sg.SetOptions(background_color=colors['BACKGROUND'],
                  text_element_background_color=colors['BACKGROUND'],
                  element_background_color=colors['BACKGROUND'],
                  text_color=colors['TEXT'],
                  input_elements_background_color=colors['INPUT'],
                  button_color=colors['BUTTON'],
                  progress_meter_color=colors['PROGRESS'],
                  border_width=0,
                  slider_border_width=0,
                  progress_meter_border_depth=0,
                  scrollbar_color=(colors['INPUT']),
                  element_text_color=colors['TEXT'])

def OneLineGUI():
    return sg.FlexForm('Get filename example').LayoutAndRead(
        [[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()]])

#=---------------------------------- main ------------------------------
def main():
    # button, (filename,) = OneLineGUI()
    # DebugTe`st()
    sg.MsgBox('Hello')
    ChatBot()
    Everything()
    SourceDestFolders()
    NonBlockingPeriodicUpdateForm_ContextManager()
    NonBlockingPeriodicUpdateForm()
    ChatBot()
    Everything()
    sg.ChangeLookAndFeel('GreenTan')
    Everything()
    # ChatBot()

    SourceDestFolders()
    MachineLearningGUI()
    NonBlockingPeriodicUpdateForm()
    ProgressMeter()
    DebugTest()
    sg.ChangeLookAndFeel('Purple')
    Everything_NoContextManager()
    NonBlockingPeriodicUpdateForm_ContextManager()

    sg.MsgBox('Done with all recipes')

if __name__ == '__main__':
    main()
    exit(69)
