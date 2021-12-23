import streamlit as st
import datetime
import requests
import time

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

def notify_image(message,image):
    url = 'https://notify-api.line.me/api/notify'
    LINE_NOTIFY_TOKEN = 'bQkJGsPyTpHGDVvYmSZdpbLOzkdxlFUqv7Pgg9MGsA3'
    # messagge = 'これはテストメッセージです'
    headers ={
        'Authorization': f'Bearer {LINE_NOTIFY_TOKEN}'
    }

    data = {
        'message': message
    }

    files = {'imageFile': image}

    requests.post(
        url,
        headers =headers,
        data=data,
        files=files

    )




page = st.sidebar.selectbox('ページ選択',['リマインド','連絡','予約実行'])


if page == 'リマインド':

    st.title('リマインド画面')

    with st.form(key='booking'):
        subjectname: str = st.text_input('教科名',max_chars=20)
        subject_num: int = st.number_input('講義番号', step=1, min_value=1)
        end_date = st.date_input('締切日の選択: ',min_value=datetime.date.today())

        submit_button = st.form_submit_button(label='登録')

    if submit_button:

        st.success('予約完了しました:smile:')
        message = f'今日は{subjectname}の{subject_num}番のミニッツペーパー提出日です。'
        notify_message(message)

elif page == '連絡':
    st.title('連絡')

    with st.form(key='booking'):
        text: str = st.text_input('連絡',max_chars=200)
        input_image = st.file_uploader('写真')
        submit_button = st.form_submit_button(label='登録')

    if submit_button:

        st.success('予約完了しました:smiley:')
        message=text
        image = input_image
        notify_image(message, image)

elif page == '予約実行':
    st.title('予約実行')

    with st.form(key='booking'):
        text: str = st.text_input('報告内容',max_chars=200)
        seconds: int = st.number_input('秒数指定',step=1,min_value=10)
        submit_button = st.form_submit_button(label='登録')

    if submit_button:

        st.success('予約完了しました:sleeping:')
        message = text
        time.sleep(seconds)
        notify_message(message)
