import sublime, sublime_plugin

class UnixEndsAndTabs( sublime_plugin.EventListener ):
    def on_pre_save( self, view ):
        view.set_line_endings( "unix" )
        view.run_command( "expand_tabs" )