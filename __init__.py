# This file is part of the Frescobaldi Extensions project,
# https://github.com/frescobaldi-extensions
#
# Copyright (c) 2018 by Urs Liska and others
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# See http://www.gnu.org/licenses/ for more information.

###################################
# Boilerplate Frescobaldi extension
###################################

# This is a minimal extension for use with Frescobaldi
# (http://frescobaldi.org, https://github.com/wbsoft/frescobaldi)

from PyQt5.QtCore import Qt
import extensions
from . import actions, config, widget

class Extension(extensions.Extension):
    """
    Boilerplate extension "My Extension".

    This is a minimal, working Frescobaldi extension providing
    stubs for all relevant functions.
    """

    # Extension configuration through class variables
    _action_collection_class = actions.Actions
    _panel_widget_class = widget.Widget
    _panel_dock_area = Qt.LeftDockWidgetArea
    _config_widget_class = config.Config
    _settings_config = {
        'show': True,
        'message': _("Initial extension message")
    }

    def __init__(self, parent, name):
        # __init__ is not necessarily needed, can be removed
        super(Extension, self).__init__(parent, name)

    def app_settings_changed(self):
        """Update extension status after global settings change."""
        # This is called automatically by the Extension base class
        pass

    def settings_changed(self, key, old, new):
        """Update extension status after extension settings change."""
        # this is triggered before app_settings_changed
        if key == 'show':
            self.action_collection().generic_action.setEnabled(new)
