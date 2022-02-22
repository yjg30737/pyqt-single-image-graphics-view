from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView


class SingleImageGraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.__initVal()

    def __initVal(self):
        self._scene = QGraphicsScene()
        self._p = QPixmap()
        self._item = ''

    def setFilename(self, filename: str):
        self._p = QPixmap(filename)
        self._setPixmap(self._p)

    def setPixmap(self, p):
        self._setPixmap(p)

    def _setPixmap(self, p):
        self._p = p
        self._item = self._scene.addPixmap(self._p)
        self.setScene(self._scene)