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

# Boilerplate extension - Tool panel widget

# The PyQt5 imports are for the example implementation,
# they are not generally needed for a panel's widget.
from PyQt5.QtWidgets import QLabel, QVBoxLayout

# The mandatory import
from extensions.widget import ExtensionWidget

# The widget for a Tool Panel should inherit from
# extensions.widget.ExtensionWidget, either exclusively
# or with multiple inheritance, e.g.
#   class Widget(QTabWidget, ExtensionWidget)
class Widget(ExtensionWidget):
    """The Tool Panel widget."""
    def __init__(self, panel):
        super(Widget, self).__init__(panel)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.label = QLabel()
        layout.addWidget(self.label)

        layout.addStretch()

        self.translateUI()

    def translateUI(self):
        self.label.setText("A dummy label")
