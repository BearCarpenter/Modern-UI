# ***********************************************************************
# *                                                                     *
# * Copyright (c) 2019 Hakan Seven <hakanseven12@gmail.com>             *
# *                                                                     *
# * This program is free software; you can redistribute it and/or modify*
# * it under the terms of the GNU Lesser General Public License (LGPL)  *
# * as published by the Free Software Foundation; either version 3 of   *
# * the License, or (at your option) any later version.                 *
# * for detail see the LICENCE text file.                               *
# *                                                                     *
# * This program is distributed in the hope that it will be useful,     *
# * but WITHOUT ANY WARRANTY; without even the implied warranty of      *
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the       *
# * GNU Library General Public License for more details.                *
# *                                                                     *
# * You should have received a copy of the GNU Library General Public   *
# * License along with this program; if not, write to the Free Software *
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307*
# * USA                                                                 *
# *                                                                     *
# ***********************************************************************

import FreeCADGui
import FCBinding


DEBUG = False

if DEBUG:
    import os
    os.environ["PYDEVD_DISABLE_FILE_VALIDATION"] = "1"
    import sys
    freecadpython = sys.executable.replace('freecad', 'python')
    App.Console.PrintMessage('Using ' + freecadpython +'\n')
    try:
        import debugpy
    except ModuleNotFoundError:
        App.Console.PrintMessage('Install debugpy by: ' + freecadpython + ' -m pip install --upgrade debugpy\n')
    debugpy.configure(python=freecadpython)
    if not debugpy.is_client_connected():
        debugpy.listen(5678)

    App.Console.PrintMessage("Waiting for debugger attach\n")
    debugpy.wait_for_client()
    debugpy.breakpoint()

# When WB activated run Modern UI
mw = FreeCADGui.getMainWindow()
mw.workbenchActivated.connect(FCBinding.run)