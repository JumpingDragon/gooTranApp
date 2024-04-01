import sys
import googletrans

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("ui/goo_ui.ui")[0]
# 디자인한 외부 ui파일 불러와서 저장

class GoogleTrans(QMainWindow, form_class):
    def __init__(self):
        super().__init__()  # 부모 클래스 생성자 호출
        self.setupUi(self)  # 불러온 ui파일을 연결

        self.setWindowTitle("구글 한 줄 번역기")       # 윈도우 타이들
        self.setWindowIcon(QIcon("icon/gooImage.png"))      # 윈도우 아이콘
        self.statusBar().showMessage("Google Translate App v1.0 Made by JumpingDragon")   # 윈도우 상태 표시줄

        self.trans_btn.clicked.connect(self.trans_action)   # Signal (이 가야 slot에서 실행)
        self.init_btn.clicked.connect(self.init_action)
        self.inpt_init.clicked.connect(self.inputInit_action)

    def trans_action(self):   # 번역 실행 함수 -> slot 함수
        korText = self.kor_input.text()     # kor_input에 입력된 한글 텍스트 가져오기

        trans = googletrans.Translator()    # 구글트랜스 모듈의 객체 선언
        # print(googletrans.LANGUAGES) -> 번역 언어의 dest 약자 찾기

        engText = trans.translate(korText, dest="en")     # 영어 번역결과
        japText = trans.translate(korText, dest="ja")     # 일본어 번역결과
        chnText = trans.translate(korText, dest="zh-cn")     # 중국어 번역결과

        self.eng_input.append(engText.text)  # .text 써줘야 함
        # 번역된 영어 텍스트를 eng_input (ui에서 우리가 만든 영어 부분)에 출력
        self.jap_input.append(japText.text)  # .text 써줘야 함
        self.chn_input.append(chnText.text)  # .text 써줘야 함

    def init_action(self):      # gui에서 초기화 버튼
        self.kor_input.clear()   # 입력 내용 지우기
        self.eng_input.clear()
        self.jap_input.clear()
        self.chn_input.clear()

    def inputInit_action(self):
        self.kor_input.clear()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gootran = GoogleTrans()
    gootran.show()
    sys.exit(app.exec_())
