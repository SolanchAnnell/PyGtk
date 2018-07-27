import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi_composites import GtkTemplate

@GtkTemplate(ui='wnd.ui')
class MiApp(Gtk.Window):
    __gtype_name__='MiApp'
    txt1 =GtkTemplate.Child()
    txt2 =GtkTemplate.Child()
    txt3 =GtkTemplate.Child()

    def __init__(self):
        Gtk.Window.__init__(self)
        self.init_template()
        self.personas=[]

    @GtkTemplate.Callback
    def _agregar_clicked_cb(self, button):
        nombre =self.txt1.get_text()
        apellido=self.txt2.get_text()
        carrera=self.txt3.get_text()
        self.personas.append((nombre, apellido, carrera))

    @GtkTemplate.Callback
    def _destroy_cb(self, widget):
        f=open("personas.txt","a")
        for persona in self.personas:
            nombre=persona[0]
            apellido=persona[1]
            carrera=persona[2]
            
            f.write(nombre +" " + apellido +" "+ carrera+"\n")
        f.close()
        Gtk.main_quit()
w =MiApp()

w.show_all()
Gtk.main()

