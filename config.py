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

# Boilerplate extension -  configuration widget

# The PyQt5 imports are for the actual widget, not for the integration
from PyQt5.QtWidgets import (
    QCheckBox,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget
)

# This may be any QWidget descendant
class Config(QWidget):
    """Configuration widget, shown in the Preferences page."""

    def __init__(self, group):
        # group will become the widget's parent, so the
        # preference group can be accessed through self.parent()
        super(Config, self).__init__(group)

        # Add widgets

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel()
        layout.addWidget(self.label)

        self.line_edit = QLineEdit()
        layout.addWidget(self.line_edit)

        # Check box's 'toggled' signal is mapped to group.changed
        # Any modification must trigger the group's changed signal,
        # and this is one way to do it.
        self.check_box = QCheckBox(toggled=group.changed)
        layout.addWidget(self.check_box)

        layout.addStretch()

        # processing after widgets have been instantiated
        # must be added manually

        self.connect_signals()
        self.translateUI()

    # Implement mandatory methods

    def translateUI(self):
        self.label.setText(_("Action message:"))
        self.check_box.setText(_("Enable action"))

    def load_settings(self):
        self.check_box.setChecked(self.settings().get('show'))
        self.line_edit.setText(self.settings().get('message'))

    def save_settings(self):
        self.settings().set('show', self.check_box.isChecked())
        self.settings().set('message', self.line_edit.text())


    # Implement custom methods

    def connect_signals(self):
        # This is another way to trigger the group's changed signal
        self.line_edit.textChanged.connect(self.parent().changed)
