from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('Landing_page.html')

@app.route('/flow1')
def flow():
    return render_template('FLOW-1.html')

# @app.route('/self')
# def self():
#     return render_template('self.html')


@app.route('/screen1')
def screen1():
    return render_template('/kiosc/index.html')

@app.route('/screen2')
def screen2():
    return render_template('/kiosc/sub1.html')

@app.route('/screen3')
def screen3():
    return render_template('/kiosc/sub2.html')

@app.route('/screen4')
def screen4():
    return render_template('/kiosc/sub3.html')

@app.route('/screen5')
def screen5():
    return render_template('/kiosc/sub4.html')

@app.route('/screen6')
def screen6():
    return render_template('/kiosc/sub5.html')


@app.route('/screen7')
def screen7():
    return render_template('/kiosc/sub6.html')

@app.route('/screen8')
def screen8():
    return render_template('/kiosc/sub7.html')

@app.route('/screen9')
def screen9():
    return render_template('/kiosc/sub8.html')


@app.route('/screen10')
def screen10():
    return render_template('/kiosc/sub9.html')

@app.route('/screen11')
def screen11():
    return render_template('/kiosc/sub10.html')

@app.route('/screen12')
def screen12():
    return render_template('/kiosc/sub11.html')


@app.route('/screen13')
def screen13():
    return render_template('/kiosc/sub12.html')

@app.route('/screen14')
def screen14():
    return render_template('/kiosc/sub13.html')

@app.route('/screen15')
def screen15():
    return render_template('/kiosc/sub14.html')

@app.route('/screen16')
def screen16():
    return render_template('/kiosc/sub15.html')


@app.route('/screen17')
def screen17():
    return render_template('/kiosc/sub16.html')


@app.route('/screen18')
def screen18():
    return render_template('/kiosc/sub17.html')

# tableorder



# 1. 첫 화면 (메뉴 선택)
@app.route('/tscreen1')
def tscreen1():
    return render_template('/table/index.html')
# 할맥1 tscreen2

# 2. 메뉴 상세 및 장바구니 담기
@app.route('/tscreen2')
def tscreen2():
    return render_template('/table/sub1.html') 

# 3. 장바구니에 담긴 후 화면
@app.route('/tscreen3')
def tscreen3():
    return render_template('/table/sub2.html')

# 4. 주류 메뉴 선택
@app.route('/tscreen4')
def tscreen4():
    return render_template('/table/sub3.html')

# 5. 주류 상세 및 장바구니 담기
@app.route('/tscreen5')
def tscreen5():
    return render_template('/table/sub4.html')

# 6. 주류 장바구니에 담긴 후 화면
@app.route('/tscreen6')
def tscreen6():
    return render_template('/table/sub5.html')

# 7. 수량 추가 후 화면
@app.route('/tscreen7')
def tscreen7():
    return render_template('/table/sub6.html')

# 8. 결제하기 확인
@app.route('/tscreen8')
def tscreen8():
    return render_template('/table/sub7.html')

# 9. 결제 방법 선택
@app.route('/tscreen9')
def tscreen9():
    return render_template('/table/sub8.html')

# 10. 주문 내역 확인 (현재 흐름에서는 사용되지 않음)
@app.route('/tscreen10')
def tscreen10():
    return render_template('/table/sub9.html')

# 11. 주문 완료 화면 (신규)
@app.route('/tscreen11')
def tscreen11():
    return render_template('/table/sub10.html')

# 12. 직원 호출 메뉴 (신규)
@app.route('/tscreen12')
def tscreen12():
    return render_template('/table/sub11.html')

# 13. 직원 호출 요청 (신규)
@app.route('/tscreen13')
def tscreen13():
    return render_template('/table/sub12.html')

@app.route('/tscreen14')
def tscreen14():
    return render_template('/table/sub13.html')

@app.route('/tscreen15')
def tscreen15():
    return render_template('/table/sub0.html')

@app.route('/tscreen16')
def tscreen16():
    return render_template('/table/sub11_1.html')





if __name__ == '__main__':
    app.run(debug=True)
