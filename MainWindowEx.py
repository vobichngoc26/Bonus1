import os
import webbrowser
import pandas as pd
import plotly.express as px
from PyQt6.QtWidgets import QMessageBox, QFileDialog
from bonus1.MainWindow import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.excel_file_path = None
        self.output_html_path = "output_chart.html"

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
        self.statusbar.showMessage("Sẵn sàng. Vui lòng chọn tập tin Excel.")

    def setupSignalAndSlot(self):
        self.pushButtonOpenFile.clicked.connect(self.select_excel_file)
        self.pushButtonOpenChart.clicked.connect(self.open_chart_in_browser)
        self.pushButtonSaveChart.clicked.connect(self.save_chart_to_html)

    def select_excel_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self.MainWindow, "Chọn Tập Tin Excel", "", "Excel Files (*.xlsx *.xls)")
        if file_path:
            self.excel_file_path = file_path
            self.lineEditDataset.setText(file_path)

    def generate_chart(self):
        if not self.excel_file_path:
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Vui lòng chọn tập tin Excel hợp lệ!")
            return None
        df = pd.read_excel(self.excel_file_path)
        df["Số tín chỉ"] = pd.to_numeric(df["Tín Chỉ"], errors='coerce')
        fig = px.sunburst(df, path=["Học Kỳ", "Bắt buộc/tự chọn", "Tên học phần"],
                          values="Số tín chỉ", title="Chương trình đào tạo")
        return fig

    def save_chart_to_html(self):
        try:
            fig = self.generate_chart()
            if fig:
                self.output_html_path = "411_10k.html"  
                fig.write_html(self.output_html_path, include_plotlyjs='cdn', full_html=True)
                self.statusbar.showMessage(f"Biểu đồ đã được cập nhật tại: {self.output_html_path}")
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể lưu biểu đồ: {str(e)}")
    def open_chart_in_browser(self):
        try:
            file_path, _ = QFileDialog.getOpenFileName(
                self.MainWindow, "Chọn File HTML", "", "HTML Files (*.html)"
            )
            if file_path:
                webbrowser.open(f"file://{os.path.abspath(file_path)}")
            else:
                QMessageBox.warning(self.MainWindow, "Cảnh báo", "Bạn chưa chọn file nào!")
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể mở biểu đồ: {str(e)}")

    def show(self):
        self.MainWindow.show()