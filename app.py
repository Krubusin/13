import streamlit as st
import datetime
import requests


def notify_message(message):
    url = 'https://notify-api.line.me/api/notify'
    LINE_NOTIFY_TOKEN = 'bQkJGsPyTpHGDVvYmSZdpbLOzkdxlFUqv7Pgg9MGsA3'
    # messagge = 'これはテストメッセージです'
    headers ={
        'Authorization': f'Bearer {LINE_NOTIFY_TOKEN}'
    }

    data = {
        'message': message
    }

    requests.post(
        url,
        headers =headers,
        data=data

    )





page = st.sidebar.selectbox('ページ選択',['リマインド予約'])


if page == 'リマインド予約':



    with st.form(key='booking'):
        # booking_id: int = random.randint(0, 10)
        subjectname: str = st.text_input('教科名',max_chars=20)
        subject_num: int = st.number_input('講義番号', step=1, min_value=1)
        end_date = st.date_input('締切日の選択: ',min_value=datetime.date.today())

        submit_button = st.form_submit_button(label='登録')

    if submit_button:

        st.success('予約完了しました')
        message = f'今日は{subjectname}の{subject_num}番のミニッツペーパー提出日です。'
        notify_message(message)

