#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2008 林哲瑋 Zhe-Wei Lin (billy3321,雨蒼) <bill3321 -AT- gmail.com>
# Last Midified : 30 Mar 2009
# Install Microsoft Internet Explorer for one or more users.
# Released under GNU General Public License
#
# @category 'Networking'
# @maintaner '林哲瑋 Zhe-Wei Lin (billy3321,雨蒼) <bill3321 -AT- gmail.com>'
# @author '林哲瑋 Zhe-Wei Lin (billy3321,雨蒼) <bill3321 -AT- gmail.com>'
# @license 'GPL'
# @parent 'Networking/ie6'
# @hide

import os
import pygtk
pygtk.require('2.0')
import gtk
import commands
import getopt

def get_args():
	try:
	    opts, args = getopt.getopt(sys.argv[1:], '', ['message=', 'command='])
	    for o, a in opts:
	      if o == '--message':
	        message = a
	      elif o == '--command':
	        command = a
	      
	  except getopt.GetoptError:
	    pass

def sel_users():
    USERS_LIST=commands.getoutput('cat /etc/passwd | grep bash | cut -d ":" -f 1').split('\n')
    USERS_HOME_LIST=commands.getoutput('cat /etc/passwd | grep bash | cut -d ":" -f 6').split('\n')
    USERS_LIST.pop(0)
    USERS_HOME_LIST.pop(0)

    dlg_bts={}
    dlg = gtk.MessageDialog \
        (None, gtk.DIALOG_MODAL,  \
        gtk.MESSAGE_QUESTION, \
        gtk.BUTTONS_OK)
    dlg.set_markup ('<b>請選擇欲 %s 的使用者細項：</b>' % message )
    for user_name in USERS_LIST:
     user_name_box= user_name + "_box"
     dlg_bts[user_name_box]=gtk.CheckButton(user_name)
     dlg.vbox.pack_start(dlg_bts[user_name_box],True,True,2)

    dlg.vbox.show_all ()

    ret = dlg.run ()
    for user_name in USERS_LIST:
     user_name_box= user_name + "_box"
     if dlg_bts[user_name_box].get_active():
      if command :
       print "正在為" + user_name + message + "..." 
       os.system("su -c " + user_name + " " + command)
      else:
       print user_name 


def user_scope ():

    USERS_LIST=commands.getoutput('cat /etc/passwd | grep bash | cut -d ":" -f 1').split('\n')
    USERS_LIST.pop(0)

    dlg = gtk.MessageDialog \
        (None, gtk.DIALOG_MODAL,  \
        gtk.MESSAGE_QUESTION, \
        gtk.BUTTONS_OK)
    dlg.set_markup ('<b>請選擇您欲 %s 的使用者：</b>' % message)

    currectuser_btn=gtk.RadioButton (None, '只套用到我自己')
    dlg.vbox.pack_start (currectuser_btn, False, True, 2)
    alluser_btn =gtk.RadioButton (currectuser_btn ,'套用到所有使用者')
    dlg.vbox.pack_start (alluser_btn, False, True, 2)
    seluser_btn =gtk.RadioButton (currectuser_btn ,'選擇套用的使用者')
    dlg.vbox.pack_start (seluser_btn, False, True, 2)

    dlg.vbox.show_all ()

    ret = dlg.run ()
    currectuser = currectuser_btn.get_active()
    alluser = alluser_btn.get_active()
    seluser = seluser_btn.get_active()

    dlg.destroy ()
    if ret != gtk.RESPONSE_OK:
       return False
    while gtk.events_pending ():
      gtk.main_iteration ()

    if currectuser:
      user_name =  os.getenv('REAL_USER')
      if command:
       print "正在為當前使用者" + message + "..."
       os.system("su -c " + user_name + " " + command)
      else: 
       print user_name
    elif alluser:
      if command:
       print "正在為所有使用者" + message + "..."
       for user_name in USERS_LIST:
        os.system("su -c " + user_name + " " + command)
      else:
       for user_name in USERS_LIST:
        print user_name,

    elif seluser:
       sel_users()

def main():
    get_args()
    user_scope()


if __name__ == "__main__":
    main()

