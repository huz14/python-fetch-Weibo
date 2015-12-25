#/usr/bin/python
#encoding = utf-8

import Tkinter
import Fetcher

'''
class for the main window
'''
class App(object):
    '''
    construction function:
    initialize all the tools in a window as following:
    '''
    def __init__(self, wnd):
        #user name label
        self.userNameLabel = Tkinter.Label(wnd, text = "user name:");
        self.userNameLabel.grid(row = 0, column = 0);
        #user name entry
        self.userNameEntry = Tkinter.Entry(wnd);
        self.userNameEntry.grid(row = 0, column = 1);
        #pwd label
        self.pwdLabel = Tkinter.Label(wnd, text = "pass word:");
        self.pwdLabel.grid(row = 1, column = 0);
        #pwd Entry
        self.pwdEntry = Tkinter.Entry(wnd, show = "*");
        self.pwdEntry.grid(row = 1, column = 1);
        #ok button
        self.okButton = Tkinter.Button(wnd, text = "OK", command = self.okClick);
        self.okButton.grid(row = 2, padx = 10);
        #clear button
        self.clearButton = Tkinter.Button(wnd, text = "Clear", command = self.clearClick);
        self.clearButton.grid(row = 2, column = 1, padx = 10);
        self.resultMessage = Tkinter.Message(wnd, text = " ");
        #self.resultMessage.config(bg = 'lightgreen', font = ('times', 24, 'italic'));
        self.resultMessage.grid(row = 3);
    '''
    Ok Button listener:
    what will happen after ok button is clicked
    '''
    def okClick(self):
        self.outPutMessage = "user name: " + self.userNameEntry.get() + '\n';
        self.outPutMessage += "pass word: " + self.pwdEntry.get() + '\n';
        self.resultMessage.config(text = self.outPutMessage);
        print self.userNameEntry.get();
        print self.pwdEntry.get();

    def clearClick(self):
        self.userNameEntry.delete(0, Tkinter.END);
        self.pwdEntry.delete(0, Tkinter.END);
        self.resultMessage.config(text = "");


