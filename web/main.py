from flask import Flask, render_template, request
from keras.models import load_model
from sklearn.preprocessing import StandardScaler
import pandas as pd

app = Flask(__name__)
scaler = StandardScaler()
df = pd.read_csv('c:/bank_account_fraud/csv/model_results.csv')

@app.route('/', methods=['GET'])
def main():
    return render_template('/input.html')

@app.route('/result', methods=['POST'])
def main_result():
    # 변수 입력값 불러오기
    income = float(request.form['income'])
    name_email_similarity = float(request.form['name_email_similarity'])
    current_address_months_count = int(request.form['current_address_months_count'])
    customer_age = int(request.form['customer_age'])
    days_since_request = float(request.form['days_since_request'])
    intended_balcon_amount = float(request.form['intended_balcon_amount'])
    zip_count_4w = int(request.form['zip_count_4w'])
    velocity_24h = float(request.form['velocity_24h'])
    date_of_birth_distinct_emails_4w = int(request.form['date_of_birth_distinct_emails_4w'])
    credit_risk_score = int(request.form['credit_risk_score'])
    bank_months_count = int(request.form['bank_months_count'])
    proposed_credit_limit = int(request.form['proposed_credit_limit'])
    device_distinct_emails_8w = int(request.form['device_distinct_emails_8w'])
    month = int(request.form['month'])
    email_is_free = int(request.form['email_is_free'])
    if email_is_free == 1:
        email = '무료 이메일'
    else:
        email = '유로 이메일'
    phone_home_valid = int(request.form['phone_home_valid'])
    if phone_home_valid == 1:
        phone_home = '집전화 있음'
    else:
        phone_home = '집전화 없음'
    phone_mobile_valid = int(request.form['phone_mobile_valid'])
    if phone_mobile_valid == 1:
        phone_mobile = '휴대전화 있음'
    else:
        phone_mobile = '휴대전화 없음'
    has_other_cards = int(request.form['has_other_cards'])
    if has_other_cards == 1:
        other_cards = '다른 카드가 있음'
    else:
        other_cards = '다른 카드가 없음'
    foreign_request = int(request.form['foreign_request'])
    if foreign_request == 1:
        foreign_request_r = '해외 승인요청'
    else:
        foreign_request_r = '국내 승인요청'
    keep_alive_session = int(request.form['keep_alive_session'])
    if keep_alive_session == 1:
        keep_alive_session_r = '세션 로그아웃 안 함'
    else:
        keep_alive_session_r = '세션 로그아웃 함'
    payment_type = int(request.form['payment_type'])
    if payment_type == 0:
        payment = 'AA'
        payment_type_AA = 1
        payment_type_AB = 0
        payment_type_AC = 0
        payment_type_AD = 0
        payment_type_AE = 0
    elif payment_type == 1:
        payment = 'AB'
        payment_type_AA = 0
        payment_type_AB = 1
        payment_type_AC = 0
        payment_type_AD = 0
        payment_type_AE = 0
    elif payment_type == 2:
        payment = 'AC'
        payment_type_AA = 0
        payment_type_AB = 0
        payment_type_AC = 1
        payment_type_AD = 0
        payment_type_AE = 0
    elif payment_type == 3:
        payment = 'AD'
        payment_type_AA = 0
        payment_type_AB = 0
        payment_type_AC = 0
        payment_type_AD = 1
        payment_type_AE = 0
    else:
        payment = 'AE'
        payment_type_AA = 0
        payment_type_AB = 0
        payment_type_AC = 0
        payment_type_AD = 0
        payment_type_AE = 1
    housing_status = int(request.form['housing_status'])
    if housing_status == 0:
        housing = 'BA'
        housing_status_BA = 1
        housing_status_BB = 0
        housing_status_BC = 0
        housing_status_BD = 0
        housing_status_BE = 0
        housing_status_BF = 0
        housing_status_BG = 0
    elif housing_status == 1:
        housing = 'BB'
        housing_status_BA = 0
        housing_status_BB = 1
        housing_status_BC = 0
        housing_status_BD = 0
        housing_status_BE = 0
        housing_status_BF = 0
        housing_status_BG = 0
    elif housing_status == 2:
        housing = 'BC'
        housing_status_BA = 0
        housing_status_BB = 0
        housing_status_BC = 1
        housing_status_BD = 0
        housing_status_BE = 0
        housing_status_BF = 0
        housing_status_BG = 0
    elif housing_status == 3:
        housing = 'BD'
        housing_status_BA = 0
        housing_status_BB = 0
        housing_status_BC = 0
        housing_status_BD = 1
        housing_status_BE = 0
        housing_status_BF = 0
        housing_status_BG = 0
    elif housing_status == 4:
        housing = 'BE'
        housing_status_BA = 0
        housing_status_BB = 0
        housing_status_BC = 0
        housing_status_BD = 0
        housing_status_BE = 1
        housing_status_BF = 0
        housing_status_BG = 0
    elif housing_status == 5:
        housing = 'BF'
        housing_status_BA = 0
        housing_status_BB = 0
        housing_status_BC = 0
        housing_status_BD = 0
        housing_status_BE = 0
        housing_status_BF = 1
        housing_status_BG = 0
    else:
        housing = 'BG'
        housing_status_BA = 0
        housing_status_BB = 0
        housing_status_BC = 0
        housing_status_BD = 0
        housing_status_BE = 0
        housing_status_BF = 0
        housing_status_BG = 1
    employment_status = int(request.form['employment_status'])
    if employment_status == 0:
        employment = 'CA'
        employment_status_CA = 1
        employment_status_CB = 0
        employment_status_CC = 0
        employment_status_CD = 0
        employment_status_CE = 0
        employment_status_CF = 0
        employment_status_CG = 0
    elif employment_status == 1:
        employment = 'CB'
        employment_status_CA = 0
        employment_status_CB = 1
        employment_status_CC = 0
        employment_status_CD = 0
        employment_status_CE = 0
        employment_status_CF = 0
        employment_status_CG = 0
    elif employment_status == 2:
        employment = 'CC'
        employment_status_CA = 0
        employment_status_CB = 0
        employment_status_CC = 1
        employment_status_CD = 0
        employment_status_CE = 0
        employment_status_CF = 0
        employment_status_CG = 0
    elif employment_status == 3:
        employment = 'CD'
        employment_status_CA = 0
        employment_status_CB = 0
        employment_status_CC = 0
        employment_status_CD = 1
        employment_status_CE = 0
        employment_status_CF = 0
        employment_status_CG = 0
    elif employment_status == 4:
        employment = 'CE'
        employment_status_CA = 0
        employment_status_CB = 0
        employment_status_CC = 0
        employment_status_CD = 0
        employment_status_CE = 1
        employment_status_CF = 0
        employment_status_CG = 0
    elif employment_status == 5:
        employment = 'CF'
        employment_status_CA = 0
        employment_status_CB = 0
        employment_status_CC = 0
        employment_status_CD = 0
        employment_status_CE = 0
        employment_status_CF = 1
        employment_status_CG = 0
    else:
        employment = 'CG'
        employment_status_CA = 0
        employment_status_CB = 0
        employment_status_CC = 0
        employment_status_CD = 0
        employment_status_CE = 0
        employment_status_CF = 0
        employment_status_CG = 1
    source = int(request.form['source'])
    if source == 0:
        source_r = '브라우저'
        source_INTERNET = 1
        source_TELEAPP = 0
    else:
        source_r = '모바일'
        source_INTERNET = 0
        source_TELEAPP = 1
    device_os = int(request.form['device_os'])
    if device_os == 0:
        device = 'Linux'
        device_os_linux = 1
        device_os_macintosh = 0
        device_os_other = 0
        device_os_windows = 0
        device_os_x11 = 0
    elif device_os == 1:
        device = 'Macintosh'
        device_os_linux = 0
        device_os_macintosh = 1
        device_os_other = 0
        device_os_windows = 0
        device_os_x11 = 0
    elif device_os == 2:
        device = '기타'
        device_os_linux = 0
        device_os_macintosh = 0
        device_os_other = 1
        device_os_windows = 0
        device_os_x11 = 0
    elif device_os == 3:
        device = 'Windows'
        device_os_linux = 0
        device_os_macintosh = 0
        device_os_other = 0
        device_os_windows = 1
        device_os_x11 = 0
    else:
        device = 'X11'
        device_os_linux = 0
        device_os_macintosh = 0
        device_os_other = 0
        device_os_windows = 0
        device_os_x11 = 1

    test_set = [[income, name_email_similarity, current_address_months_count, customer_age, days_since_request,
                 intended_balcon_amount, zip_count_4w, velocity_24h, date_of_birth_distinct_emails_4w,
                 credit_risk_score, email_is_free, phone_home_valid, phone_mobile_valid, bank_months_count,
                 has_other_cards, proposed_credit_limit, foreign_request, keep_alive_session, device_distinct_emails_8w,
                 month, payment_type_AA, payment_type_AB, payment_type_AC, payment_type_AD, payment_type_AE,
                 employment_status_CA, employment_status_CB, employment_status_CC, employment_status_CD,
                 employment_status_CE, employment_status_CF, employment_status_CG, housing_status_BA, housing_status_BB,
                 housing_status_BC, housing_status_BD, housing_status_BE, housing_status_BF, housing_status_BG,
                 source_INTERNET, source_TELEAPP, device_os_linux, device_os_macintosh, device_os_other,
                 device_os_windows, device_os_x11
                 ]]
    test_set_scaled = scaler.transform(test_set)

    # LOGIT
    logit_model = load_model('c:/bank_account_fraud/model/logit.model')
    logit_model.load_weights('c:/bank_account_fraud/model/logit.weight')
    logit_rate = logit_model.predict(test_set_scaled)
    if logit_rate >= 0.5:
        logit_result = '사기 계좌'
    else:
        logit_result = '정상 계좌'
    logit_score = df[df.Model == 'Logit'].iloc[0, 1]

    # DECISION TREE
    tree_model = load_model('c:/bank_account_fraud/model/tree.model')
    tree_model.load_weights('c:/bank_account_fraud/model/tree.weight')
    tree_rate = tree_model.predict(test_set_scaled)
    if tree_rate >= 0.5:
        tree_result = '사기 계좌'
    else:
        tree_result = '정상 계좌'
    tree_score = df[df.Model == 'Tree'].iloc[0, 1]

    # RANDOM FOREST
    rf_model = load_model('c:/bank_account_fraud/model/rf.model')
    rf_model.load_weights('c:/bank_account_fraud/model/rf.weight')
    rf_rate = rf_model.predict(test_set_scaled)
    if rf_rate >= 0.5:
        rf_result = '사기 계좌'
    else:
        rf_result = '정상 계좌'
    rf_score = df[df.Model == 'RF'].iloc[0, 1]

    # SVM
    svm_model = load_model('c:/bank_account_fraud/model/svm.model')
    svm_model.load_weights('c:/bank_account_fraud/model/svm.weight')
    svm_rate = svm_model.predict(test_set_scaled)
    if svm_rate >= 0.5:
        svm_result = '사기 계좌'
    else:
        svm_result = '정상 계좌'
    svm_score = df[df.Model == 'SVM'].iloc[0, 1]

    # KNN
    knn_model = load_model('c:/bank_account_fraud/model/knn.model')
    knn_model.load_weights('c:/bank_account_fraud/model/knn.weight')
    knn_rate = knn_model.predict(test_set_scaled)
    if knn_rate >= 0.5:
        knn_result = '사기 계좌'
    else:
        knn_result = '정상 계좌'
    knn_score = df[df.Model == 'KNN'].iloc[0, 1]

    # ANN
    ann_model = load_model('c:/bank_account_fraud/model/ann.model')
    ann_model.load_weights('c:/bank_account_fraud/model/ann.weight')
    ann_rate = ann_model.predict(test_set_scaled)
    if ann_rate >= 0.5:
        ann_result = '사기 계좌'
    else:
        ann_result = '정상 계좌'
    ann_score = df[df.Model == 'ANN'].iloc[0, 1]

    # DNN
    dnn_model = load_model('c:/bank_account_fraud/model/dnn.model')
    dnn_model.load_weights('c:/bank_account_fraud/model/dnn.weight')
    dnn_rate = dnn_model.predict(test_set_scaled)
    if dnn_rate >= 0.5:
        dnn_result = '사기계좌'
    else:
        dnn_result = '정상계좌'
    dnn_score = df[df.Model == 'DNN'].iloc[0, 1]

    return render_template('/main_result.html', logit_rate='{:.2f}%'.format(logit_rate[0][0]*100),
                           tree_rate='{:.2f}%'.format(tree_rate[0][0]*100), rf_rate='{:.2f}%'.format(rf_rate[0][0]*100),
                           svm_rate='{:.2f}%'.format(svm_rate[0][0] * 100), knn_rate='{:.2f}%'.format(knn_rate[0][0]*100),
                           ann_rate='{:.2f}%'.format(ann_rate[0][0]*100), dnn_rate='{:.2f}%'.format(dnn_rate[0][0] * 100),
                           logit_result=logit_result, tree_result=tree_result, rf_result=rf_result, svm_result=svm_result,
                           knn_result=knn_result, ann_result=ann_result, dnn_result=dnn_result, logit_score=logit_score,
                           tree_score=tree_score, rf_score=rf_score, svm_score=svm_score, knn_score=knn_score,
                           ann_score=ann_score, dnn_score=dnn_score, income=income, name_email_similarity=name_email_similarity,
                           current_address_months_count=current_address_months_count, customer_age=customer_age,
                           days_since_request=days_since_request, intended_balcon_amount=intended_balcon_amount,
                           zip_count_4w=zip_count_4w, velocity_24h=velocity_24h, date_of_birth_distinct_emails_4w=date_of_birth_distinct_emails_4w,
                           credit_risk_score=credit_risk_score, email=email, phone_home=phone_home,
                           phone_mobile=phone_mobile, bank_months_count=bank_months_count, other_cards=other_cards,
                           proposed_credit_limit=proposed_credit_limit, foreign_request_r=foreign_request_r,
                           keep_alive_session_r=keep_alive_session_r, device_distinct_emails_8w=device_distinct_emails_8w,
                           month=month, payment=payment, employment=employment, housing=housing, source_r=source_r, device=device
                           )

if __name__ == '__main__':
    #웹브라우저에서 실행할 때 http://localhost로 하면 느림
    #http://127.0.0.1로 할 것
    app.run(port=8000, threaded=False)
