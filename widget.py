# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtCore import QTimer, QTime, Qt, QUrl
from PySide6.QtGui import QPainter, QColor
from PySide6.QtMultimedia import QSoundEffect
from ui_form import Ui_Widget
from random import randint


# Custom widget to draw a dot
class DotLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.dot_color = QColor("green")
        self.setVisible(False)

    def paintEvent(self, event):
        if self.isVisible():
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            radius = min(self.width(), self.height()) // 2 - 5
            center = self.rect().center()
            painter.setBrush(self.dot_color)
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(center, radius, radius)


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.user_name = ""

        label_dot_ui = self.ui.labelDot
        self.label_dot = DotLabel(self)
        self.label_dot.setGeometry(label_dot_ui.geometry())
        label_dot_ui.deleteLater()

        self.start_time = QTime()
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.show_dot)

        self.ui.btnStart.clicked.connect(self.start_test)
        self.ui.btnRetry.clicked.connect(self.retry)
        self.ui.lineEditName.returnPressed.connect(self.handle_name_entry)

        # Ses efekti objesi
        self.sound_effect = QSoundEffect()
        self.sound_effect.setSource(QUrl.fromLocalFile("ding.wav"))
        self.sound_effect.setVolume(0.5)

        # Genel arka plan rengi
        self.setStyleSheet("background-color: #ffe4ec;")

        # Buton stili
        button_style = """
        QPushButton {
            background-color: white;
            color: #d6336c;
            border: 2px solid #d6336c;
            border-radius: 8px;
            padding: 6px;
            font-weight: bold;
        }
        QPushButton:hover {
            background-color: #ffd9e8;
        }
        """

        # Metin kutusu stili
        input_style = """
        QLineEdit {
            background-color: #fff0f6;
            border: 2px solid #d6336c;
            border-radius: 8px;
            padding: 5px;
            color: #a9004a;
            font-weight: bold;
        }
        QLineEdit:focus {
            border-color: #ff4d94;
            background-color: #ffd9e8;
        }
        """

        self.ui.btnStart.setStyleSheet(button_style)
        self.ui.btnRetry.setStyleSheet(button_style)
        self.ui.lineEditName.setStyleSheet(input_style)

        # Label için renkli yazı stili (örneğin uyarı metni)
        self.ui.labelNameInfo.setStyleSheet("color: #d6336c; font-weight: bold;")

        # Başlangıçta sadece isim giriş alanı görünsün
        self.ui.btnStart.setVisible(False)
        self.ui.btnRetry.setVisible(False)
        self.ui.labelInfo.setVisible(False)
        self.ui.labelResult.setVisible(False)
        self.label_dot.setVisible(False)
        self.ui.labelLog.setVisible(False)

    def handle_name_entry(self):
        self.user_name = self.ui.lineEditName.text().strip()
        if self.user_name:
            self.ui.lineEditName.setVisible(False)
            self.ui.labelNameInfo.setVisible(False)

            self.ui.btnStart.setVisible(True)
            self.ui.btnStart.setEnabled(True)
            self.ui.labelInfo.setVisible(True)
            self.ui.labelResult.setVisible(True)
            self.ui.labelInfo.setText(f"Hoş geldin, {self.user_name}! Hazırsan 'Başla'ya tıkla.")
        else:
            self.ui.labelNameInfo.setText("Lütfen adınızı girin!")

    def start_test(self):
        self.ui.labelInfo.setText("Hazırlan...")
        self.ui.btnStart.setEnabled(False)
        self.ui.btnRetry.setEnabled(False)
        self.timer.start(2000 + self.random_delay())

    def random_delay(self):
        return randint(0, 1000)

    def show_dot(self):
        self.label_dot.setVisible(True)
        self.start_time = QTime.currentTime()
        self.sound_effect.play()  # Nokta görünürken ses çal

    def get_emoji(self, ms):
        if ms < 250:
            return "⚡️🥇"
        elif ms < 350:
            return "🚀🥈"
        elif ms < 500:
            return "🏃‍♂️🥉"
        else:
            return "🐢"

    def mousePressEvent(self, event):
        if self.label_dot.isVisible():
            reaction_time = self.start_time.msecsTo(QTime.currentTime())
            self.ui.labelResult.setText(f"Süre: {reaction_time} ms")
            self.ui.labelInfo.setText("Tebrikler!")
            self.label_dot.setVisible(False)

            self.sound_effect.play()  # Tebrik ederken ses çal

            self.ui.btnRetry.setVisible(True)
            self.ui.btnRetry.setEnabled(True)
            self.ui.btnStart.setVisible(False)
            self.ui.btnStart.setEnabled(False)

            # Skor güncelleme
            new_entry = f"{self.user_name} - {reaction_time} ms"
            emoji = self.get_emoji(reaction_time)
            entry_with_emoji = f"{emoji} {new_entry}"

            existing_log = self.ui.labelLog.text()
            lines = existing_log.strip().split("\n") if existing_log else []
            lines.append(entry_with_emoji)

            def get_ms(line):
                try:
                    return int(line.split("-")[-1].replace("ms", "").strip())
                except:
                    return 9999

            lines.sort(key=get_ms)

            updated_log = "\n".join(lines)
            self.ui.labelLog.setVisible(True)
            self.ui.labelLog.setText(updated_log)

            with open("sonuclar.txt", "a", encoding="utf-8") as f:
                f.write(entry_with_emoji + "\n")

        else:
            self.ui.labelResult.setText("Çok erken tıkladınız!")
            self.ui.labelInfo.setText("Nokta görünmeden tıkladınız!")

        self.reset_buttons()

    def reset_buttons(self):
        self.ui.btnStart.setEnabled(True)

    def retry(self):
        self.ui.lineEditName.setText("")
        self.ui.lineEditName.setVisible(True)
        self.ui.labelNameInfo.setVisible(True)
        self.ui.labelNameInfo.setText("Lütfen adınızı girin")

        self.ui.labelInfo.setVisible(False)
        self.ui.labelResult.setVisible(False)
        self.label_dot.setVisible(False)

        self.ui.btnStart.setVisible(False)
        self.ui.btnRetry.setVisible(False)

        self.user_name = ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    sys.exit(app.exec())
