#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
bl_info = {
    "name": "Notify",
    "author": "Dziban",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "Global",
    "description": "Displays a system notification when render is complete on Linux and Windows based systems",
    "warning": "",
    "wiki_url": "",
    "category": "System",
    }
import bpy, os, locale, subprocess
from bpy.app.handlers import persistent
loc = locale.getlocale() # get current locale
locx = loc[:3]
locale.getdefaultlocale()
@persistent
def is_render_complete(scene):
#LINUX
        if os.name=='posix' and locx=="es_":#Español
            bashCommand = 'notify-send -u "critical" -i "blender" "Blender | Render Finalizado!"'
        elif os.name=='posix' and locx=="ca_":#Catalán
            bashCommand = 'notify-send -u "critical" -i "blender" "Blender | S´ha finalitzat la prestació!"'
        elif os.name=='posix' and locx=="fr_":#Frances
            bashCommand = 'notify-send -u "critical" -i "blender" "Blender | Rendu terminé!"'
        elif os.name=='posix' and locx=="it_":#Italiano
            bashCommand = 'notify-send -u "critical" -i "blender" "Blender | Rendering finito!"'
        elif os.name=='posix' and locx=="pt_":#Protugues
            bashCommand = 'notify-send -u "critical" -i "blender" "Blender | Renderizado concluído!"'
        elif os.name=='posix' and locx=="de_":#Alemán
            bashCommand = 'notify-send -u "critical" -i "blender" "Blender | Fertig machen!"'
        else:
            bashCommand = 'notify-send -u "critical" -i "blender" "Blender | Render Finished!"'
        output = subprocess.check_output(['bash','-c', bashCommand])
#WINDOWS
        if os.name=='nt' and locx=="es_":#Español
            command = 'msg * /server:%computername% "blender" "Blender | Render Finalizado!"'
        elif os.name=='nt' and locx=="ca_":#Catalán
            command = 'msg * /server:%computername% "blender" "Blender | S´ha finalitzat la prestació!"'
        elif os.name=='nt' and locx=="fr_":#Frances
            command = 'msg * /server:%computername% "blender" "Blender | Rendu terminé!"'
        elif os.name=='nt' and locx=="it_":#Italiano
            command = 'msg * /server:%computername% "blender" "Blender | Rendering finito!"'
        elif os.name=='nt' and locx=="pt_":#Protugues
            command = 'msg * /server:%computername% "blender" "Blender | Renderizado concluído!"'
        elif os.name=='nt' and locx=="de_":#Alemán
            command = 'msg * /server:%computername% "blender" "Blender | Fertig machen!"'
        else:
            command = 'msg * /server:%computername% "blender" "Blender | Render Finished!"'

classes = ()
register, unregister = bpy.utils.register_classes_factory(classes)

def register():
     bpy.app.handlers.render_complete.append(is_render_complete)
def unregister():
     bpy.app.handlers.render_complete.remove(is_render_complete)

if __name__ == '__main__':
    register()
