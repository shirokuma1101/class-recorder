# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Window
###########################################################################

class Window ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"ClassRecorder", pos = wx.DefaultPosition, size = wx.Size( 300,350 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sizer_base = wx.BoxSizer( wx.VERTICAL )

		self.panel_recordbuttons = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizer_recordbuttons = wx.BoxSizer( wx.HORIZONTAL )

		self.button_recordstart = wx.Button( self.panel_recordbuttons, wx.ID_ANY, u"録画開始", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer_recordbuttons.Add( self.button_recordstart, 1, wx.ALL, 0 )

		self.button_recordstop = wx.Button( self.panel_recordbuttons, wx.ID_ANY, u"録画停止", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer_recordbuttons.Add( self.button_recordstop, 1, wx.ALL, 0 )


		self.panel_recordbuttons.SetSizer( sizer_recordbuttons )
		self.panel_recordbuttons.Layout()
		sizer_recordbuttons.Fit( self.panel_recordbuttons )
		sizer_base.Add( self.panel_recordbuttons, 0, wx.ALL|wx.EXPAND, 0 )

		self.panel_reqsettings = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizer_reqsettings = wx.StaticBoxSizer( wx.StaticBox( self.panel_reqsettings, wx.ID_ANY, u"必須設定" ), wx.VERTICAL )

		gridsizer_reqsettings = wx.GridSizer( 0, 2, 0, 0 )

		self.statictext_subject = wx.StaticText( sizer_reqsettings.GetStaticBox(), wx.ID_ANY, u"Subject", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.statictext_subject.Wrap( -1 )

		gridsizer_reqsettings.Add( self.statictext_subject, 0, wx.ALL|wx.EXPAND, 5 )

		choice_subjectChoices = []
		self.choice_subject = wx.Choice( sizer_reqsettings.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_subjectChoices, 0 )
		self.choice_subject.SetSelection( 0 )
		gridsizer_reqsettings.Add( self.choice_subject, 0, wx.ALL|wx.EXPAND, 0 )

		self.statictext_suffix = wx.StaticText( sizer_reqsettings.GetStaticBox(), wx.ID_ANY, u"Suffix", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.statictext_suffix.Wrap( -1 )

		gridsizer_reqsettings.Add( self.statictext_suffix, 0, wx.ALL|wx.EXPAND, 5 )

		choice_suffixChoices = []
		self.choice_suffix = wx.Choice( sizer_reqsettings.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_suffixChoices, 0 )
		self.choice_suffix.SetSelection( 0 )
		gridsizer_reqsettings.Add( self.choice_suffix, 0, wx.ALL|wx.EXPAND, 0 )


		sizer_reqsettings.Add( gridsizer_reqsettings, 1, wx.EXPAND, 5 )


		self.panel_reqsettings.SetSizer( sizer_reqsettings )
		self.panel_reqsettings.Layout()
		sizer_reqsettings.Fit( self.panel_reqsettings )
		sizer_base.Add( self.panel_reqsettings, 0, wx.EXPAND |wx.ALL, 0 )

		self.panel_optsettings = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizer_optsettings = wx.StaticBoxSizer( wx.StaticBox( self.panel_optsettings, wx.ID_ANY, u"オプション設定" ), wx.VERTICAL )


		self.panel_optsettings.SetSizer( sizer_optsettings )
		self.panel_optsettings.Layout()
		sizer_optsettings.Fit( self.panel_optsettings )
		sizer_base.Add( self.panel_optsettings, 1, wx.EXPAND |wx.ALL, 0 )


		self.SetSizer( sizer_base )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.button_recordstart.Bind( wx.EVT_BUTTON, self.click_button_recordstart )
		self.button_recordstop.Bind( wx.EVT_BUTTON, self.click_button_recordstop )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def click_button_recordstart( self, event ):
		event.Skip()

	def click_button_recordstop( self, event ):
		event.Skip()


