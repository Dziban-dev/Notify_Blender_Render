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
    "blender": (2, 79, ),
    "location": "Global",
    "description": "Sends a system notification when render is complete.",
    "warning": "",
    "wiki_url": "",
    "category": "System",
    }
import bpy, os, subprocess
from bpy.app.handlers import persistent
@persistent
def is_render_complete(scene):
        if os.name=='posix':
            bashCommand = 'notify-send -u "critical" -i "blender" "Blender | Render Finished!"'
        output = subprocess.check_output(['bash','-c', bashCommand])
        if os.name=='nt':
            command = 'msg * /server:%computername% "blender" "Blender | Render Finished!"'
def register():
     bpy.app.handlers.render_complete.append(is_render_complete)
def unregister():
     bpy.app.handlers.render_complete.remove(is_render_complete)
if __name__ == '__main__':
    register()