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

from extensions import ExtensionSettings

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

        self.check_box = QCheckBox()
        layout.addWidget(self.check_box)

        layout.addStretch()

        # processing after widgets have been instantiated

        self.connect_signals()
        self.translateUI()


    # Implement mandatory methods

    def translateUI(self):
        self.label.setText(_("Action message:"))
        self.check_box.setText(_("Enable action"))

    def load_settings(self):
        # Use extensions.ExtensionSettings() instead of QSettings()
        s = ExtensionSettings()
        s.beginGroup('boilerplate')
        self.check_box.setChecked(s.value('show', False, bool))
        self.line_edit.setText(
            s.value('message', _("Initial action message"), str))

    def save_settings(self):
        s = ExtensionSettings()
        s.beginGroup('boilerplate')
        s.setValue('show', self.check_box.isChecked())
        s.setValue('message', self.line_edit.text())


    # Implement custom methods

    def connect_signals(self):
        # Ensure Preferences are considered modified
        for s in [self.check_box.toggled,
                  self.line_edit.textChanged]:
            s.connect(self.parent().changed)
