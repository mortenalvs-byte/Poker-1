from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QDialog

from poker.tools.helper import get_dir


def _ui_path(filename):
    return get_dir('gui', 'ui', filename)


def _load_ui(instance, filename):
    uic.loadUi(_ui_path(filename), instance)


class AnalyserForm(QMainWindow):

    def __init__(self):
        super(AnalyserForm, self).__init__()
        _load_ui(self, 'analyser_form.ui')

        self.show()


class TableSetupForm(QMainWindow):

    def __init__(self):
        super(TableSetupForm, self).__init__()
        _load_ui(self, 'table_setup_form.ui')

        self.show()


class SetupForm(QMainWindow):
    def __init__(self):
        super(SetupForm, self).__init__()
        _load_ui(self, 'setup_form.ui')

        self.show()


class StrategyEditorForm(QMainWindow):

    def __init__(self):
        super(StrategyEditorForm, self).__init__()
        _load_ui(self, 'strategy_manager_form.ui')

        self.show()


class GeneticAlgo(QDialog):

    def __init__(self):
        super(GeneticAlgo, self).__init__()
        _load_ui(self, 'genetic_algo_form.ui')
        self.show()


class MainForm(QMainWindow):

    def __init__(self):
        super(MainForm, self).__init__()
        _load_ui(self, 'main_form.ui')

        self.show()


class UiPokerbot(QMainWindow):

    def __init__(self):
        super(UiPokerbot, self).__init__()
        _load_ui(self, 'main_form.ui')

        self.show()
