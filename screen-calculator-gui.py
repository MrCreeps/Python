import math
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton

class TriangleWidget(QWidget):
    def __init__(self):
        super().__init__()
        # Create widgets
        self.diagonal_label = QLabel("Diagonal Length:")
        self.diagonal_input = QLineEdit()
        self.width_ratio_label = QLabel("Width Ratio:")
        self.width_ratio_input = QLineEdit()
        self.length_ratio_label = QLabel("Length Ratio:")
        self.length_ratio_input = QLineEdit()
        self.horizontal_res_label = QLabel("Horizontal Resolution:")
        self.horizontal_res_input = QLineEdit()
        self.calculate_button = QPushButton("Calculate")
        self.vertical_res_label = QLabel()
        self.length_label = QLabel()
        self.width_label = QLabel()
        self.area_label = QLabel()
        self.tpx_label = QLabel()
        self.ppi_label = QLabel()

        # Create layout
        layout = QVBoxLayout()
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.diagonal_label)
        input_layout.addWidget(self.diagonal_input)
        input_layout.addWidget(self.width_ratio_label)
        input_layout.addWidget(self.width_ratio_input)
        input_layout.addWidget(self.length_ratio_label)
        input_layout.addWidget(self.length_ratio_input)
        input_layout.addWidget(self.horizontal_res_label)
        input_layout.addWidget(self.horizontal_res_input)
        layout.addLayout(input_layout)
        layout.addWidget(self.calculate_button)
        layout.addWidget(QLabel("Vertical Resolution:"))
        layout.addWidget(self.vertical_res_label)
        layout.addWidget(QLabel("Length:"))
        layout.addWidget(self.length_label)
        layout.addWidget(QLabel("Width:"))
        layout.addWidget(self.width_label)
        layout.addWidget(QLabel("Area:"))
        layout.addWidget(self.area_label)
        layout.addWidget(QLabel("Total Pixel Resolution:"))
        layout.addWidget(self.tpx_label)
        layout.addWidget(QLabel("Pixel Density (Pixels per Inch):"))
        layout.addWidget(self.ppi_label)
        self.setLayout(layout)

        # Connect signal to slot
        self.calculate_button.clicked.connect(self.calculate)

    def find_length_and_width(self, hypotenuse, length_width_ratio):
        # Calculate the length of the triangle
        length = hypotenuse / math.sqrt(1 + (1 / (length_width_ratio ** 2)))

        # Calculate the width of the triangle
        width = length / length_width_ratio

        return (length, width)

    def calculate(self):
        # Get input values
        try:
            hypotenuse = float(self.diagonal_input.text())
            width_ratio = float(self.width_ratio_input.text())
            length_ratio = float(self.length_ratio_input.text())
            hres = float(self.horizontal_res_input.text())

            # Calculate length and width
            length_width_ratio = width_ratio/length_ratio
            length, width = self.find_length_and_width(hypotenuse, length_width_ratio)

            # Calculate other values
            area = length * width
            vres = hres / length_width_ratio
            tpx = hres * vres
            ppi = (tpx / area)**0.5

            # Set label text
            self.vertical_res_label.setText(str(vres))
            self.length_label.setText(str(length))
            self.width_label.setText(str(width))
            self.area_label.setText(str(area))
            self.tpx_label.setText(str(tpx))
            self.ppi_label.setText(str(ppi))
        except:
            return

if __name__ == '__main__':
    print("Reference Values:\nUHD (4k) = 3840\nQHD (1440p ) = 2560\nFHD (1080p) = 1920\nHD (720p) = 1280")

    app = QApplication([])
    widget = TriangleWidget()
    widget.show()
    widget.setWindowTitle("Screen Info Calculator")
    app.exec_()
