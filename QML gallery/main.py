import sys, os
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine

# Enable scaling
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
# Don't use resources, use local paths
os.environ["QT_QUICK_CONTROLS_CONF"] = "qtquickcontrols2.conf"
QIcon.setThemeSearchPaths(['./icons'])

app = QApplication(sys.argv)
QIcon.setThemeName("gallery")
engine = QQmlApplicationEngine()
engine.load(QUrl('gallery.qml'))
sys.exit(app.exec_())