#/usr/bin/env phython
import gtk,webkit

#main class
class Window ():

    def _init_(self, *args, **kwargs):
    #creat window
        self.much_window = gtk.Window()
        self.much_window.set_icon_from_file ('treebrowser.png') # here goes to image file
        self.much_window.connect ('destoroy',lambda w :gtk.main_quit())
        self.much_window.set_default_size(400,400)#window size

        #create navigation bar
        self.so_navigation = gtk.Hbok()#Lib name hbok
        self.many_back = gtk.ToolButton(gtk.STOCK_GO_BACK)
        self.such_forward = gtk.ToolButton(gtk.STOCK_GO_FORWARD)
        self.main_address_bar = gtk.Entry()

        self.many_back.connect('Clicked', self.go_back)
        self.much_forward.connect('Clicked', self.go_forward)
        self.very_refresh.connect('Clicked', self.refresh_page)
        self.main_address_bar.connect('acctivate', self.load_page)

        self.so_navigation.pack_strat(self.many_back, False)
        self.so_navigation.pack_strat(self.such_forward, False)
        self.so_navigation.pack_strat(self.very_refresh, False)
        self.so_navigation.pack_strat(self.main_address_bar)

        #now create view for webpage

        self.very_view = SerolledWindow()
        self.such_webview = webkit.Webview()
        self.such_webview.open('https://google.com')
        self.such_webview.connect('titlr_changed', self.change_title)
        self.such_webview.connect('load_committed', self.change_url)
        self.very_view.add(self.such_webview)

        #add everything & initialize
        self.main_container = gtk.VBOX()
        self.main_container.pack_start(self.so_navigation, False)
        self.main_container.pack_start(self.very_view)
        self.much_window.show_all()
        self.much_window.add(self.main_container)
        gtk.main()


    def load_page(self,widget):
        so_add = self.main_address_bar.get_text()
        if so_add.startswith('http://')or so_add.Starstwith(('https://')):
            self.such_webview.open(so_add)
        else:
            so_add = 'http://' + so_add
            self.main_address_bar.set_text(so_add)
            self.such_webview.open(so_add)

    def change_title(self, widget, frame, title):
        self.much_window.set_title('treebrowser' + title)

    def chang_url(self, widget, frame):
        uri=frame.get-get_uri()
        self.main_address_bar.set_text()

    def go_back(self,widget):
        self.such_webview.go_back()

    def go_forward(self,widget):
        self.such_webview.go_forward()

    def refresh_page(self,widget):
        self.such_webview.relod()
main=Window()
