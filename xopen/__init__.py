#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Launch xdg-open with the provided file locations."""
import os
import sys
from subprocess import run
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QDesktopWidget, QWidget,
                             QGridLayout, QLabel, QLineEdit, QPushButton)


class MainWidget(QWidget):
    """Main window class."""

    def __init__(self):
        """Run the Qwidget initializer; initialize the UI."""
        super().__init__()
        self.modulepath = os.path.dirname(os.path.realpath(__file__))
        self.init_ui()
        self.keyPressEvent = self.handle_keypress  # cuz flake8 -_-

    def init_ui(self):
        """Initialize the UI."""
        # Postion the window.
        self.setFixedSize(300, 100)
        self.center()

        # Create the widgets
        self.label = QLabel('Location of the file/folder:')
        self.button = QPushButton("Go!")
        self.text_entry = QLineEdit()

        # handle button click
        self.button.clicked.connect(self.handle_button)

        # Create the grid
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.label, 0, 0)
        grid.addWidget(self.text_entry, 1, 0)
        grid.addWidget(self.button, 1, 1)

        # Title and Icon.
        self.setWindowTitle('xopen-file')
        self.setWindowIcon(QIcon.fromTheme('search',
                           QIcon(self.modulepath + '/icon.svg')))

        # Show all the Widgets
        self.setLayout(grid)
        self.show()

    def center(self):
        """Move window to the center of the screen."""
        fake_el = self.frameGeometry()
        center_px = QDesktopWidget().availableGeometry().center()
        fake_el.moveCenter(center_px)
        self.move(fake_el.topLeft())

    def handle_keypress(self, event):
        """Quit application on Escape key."""
        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.close()
            run(['xdg-open', self.text_entry.text().strip()])

    def handle_button(self):
        """Open file on click"""
        if len(self.text_entry.text().strip()) > 0:
            self.close()
            run(['xdg-open', self.text_entry.text().strip()])


def main():
    """App runner."""
    app = QApplication(["xopen-file"] + sys.argv[1:])
    window = MainWidget()
    print("started {}".format(window.windowTitle()))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
