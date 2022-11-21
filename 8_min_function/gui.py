import sys
from PyQt5 import uic
from PyQt5.QtCore import QFile, Qt, QCoreApplication
from PyQt5.QtWidgets import QApplication, QRadioButton, \
    QPushButton, QSpinBox, QCheckBox, QLabel, QGroupBox, \
    QDoubleSpinBox, QProgressDialog, QVBoxLayout
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtGui import QPainter, QPixmap
from ga import Ga


class Gui:
    def __init__(self):
        # loading widgets elements from ui file
        self.window = uic.loadUi("min_function.ui")

        # Getting widgets elements
        self.single_run_rb = self.window.findChild(QRadioButton, 'singleRunRadioButton')
        self.multi_run_rb = self.window.findChild(QRadioButton, 'multiRunRadioButton')
        self.repetitions_sb = self.window.findChild(QSpinBox, 'repetitionsSpinBox')
        self.population_sb = self.window.findChild(QSpinBox, 'populationSpinBox')
        self.crossover_dsb = self.window.findChild(QDoubleSpinBox, 'crossoverDoubleSpinBox')
        self.mutation_dsb = self.window.findChild(QDoubleSpinBox, 'mutationDoubleSpinBox')
        self.generation_sb = self.window.findChild(QSpinBox, 'generationSpinBox')
        self.elitism_cb = self.window.findChild(QCheckBox, 'elitismCheckBox')
        self.run_pb = self.window.findChild(QPushButton, 'runPushButton')
        self.x_result_l = self.window.findChild(QLabel, 'xResultLabel')
        self.fx_l = self.window.findChild(QLabel, 'fxLabel')
        self.correct_results_l = self.window.findChild(QLabel, 'correctResultsLabel')
        self.incorrect_results_l = self.window.findChild(QLabel, 'incorrectResultsLabel')
        self.results_single_run_gb = self.window.findChild(QGroupBox, 'resultsSingleRunGroupBox')
        self.results_multi_run_gb = self.window.findChild(QGroupBox, 'resultsMultiRunGroupBox')
        self.icon_result_l = self.window.findChild(QLabel, 'iconResultLabel')
        self.graph_vbl = self.window.findChild(QVBoxLayout, 'graphVerticalLayout')

        # Connecting
        self.run_pb.clicked.connect(self.on_run_pb_clicked)
        self.multi_run_rb.toggled.connect(self.on_multi_run_rb_toggled)

        # Graph settings
        self.chart = QChart()
        self.chart.setTitle('Chart')
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.graph_vbl.addWidget(self.chart_view)

        self.repetitions_sb.setEnabled(False)
        self.results_multi_run_gb.setEnabled(False)

    def on_multi_run_rb_toggled(self):
        if self.multi_run_rb.isChecked():
            self.repetitions_sb.setEnabled(True)
            self.repetitions_sb.setValue(100)
            self.results_single_run_gb.setEnabled(False)
            self.results_multi_run_gb.setEnabled(True)
            self.chart_view.setEnabled(False)
        else:
            self.repetitions_sb.setEnabled(False)
            self.repetitions_sb.setValue(1)
            self.results_single_run_gb.setEnabled(True)
            self.results_multi_run_gb.setEnabled(False)
            self.chart_view.setEnabled(True)

    def on_run_pb_clicked(self):
        self.chart.removeAllSeries()
        min_function = 421.0
        ga_answer = 0.0
        correct = 0
        incorrect = 0

        ga = Ga(self.population_sb.value(),
                self.crossover_dsb.value(),
                self.mutation_dsb.value(),
                self.generation_sb.value(),
                self.elitism_cb.isChecked())

        progress_dialog = QProgressDialog('Repetitions...',
                                          'Cancel',
                                          0,
                                          self.repetitions_sb.value(),
                                          self.window)
        progress_dialog.setWindowModality(Qt.WindowModal)
        ga_output = ()
        for i in range(self.repetitions_sb.value()):
            ga_output = ga.run_generation()
            ga_answer = ga_output[0]

            if ga_answer == min_function:
                correct += 1
            else:
                incorrect += 1
            progress_dialog.setValue(i)

            if progress_dialog.wasCanceled():
                break

        progress_dialog.setValue(self.repetitions_sb.value())

        if self.single_run_rb.isChecked():
            self.x_result_l.setText(str(ga_answer))
            self.fx_l.setText('{0:.2f}'.format(ga.calc_function(ga_answer)))
            if ga_answer == min_function:
                self.icon_result_l.setPixmap(QPixmap('correct-icon.png'))
            else:
                self.icon_result_l.setPixmap(QPixmap('incorrect-icon.png'))

            # Graph
            series_1 = QLineSeries()
            series_1.setName('Average Fit')
            series_2 = QLineSeries()
            series_2.setName('Best Fit')
            for i in range(len(ga_output[1])):
                series_1.append(ga_output[1][i], ga_output[2][i])
                series_2.append(ga_output[1][i], ga_output[3][i])
            self.chart.addSeries(series_1)
            self.chart.addSeries(series_2)
            self.chart.createDefaultAxes()

        else:
            self.correct_results_l.setText(str(correct))
            self.incorrect_results_l.setText(str(incorrect))


if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    gui = Gui()
