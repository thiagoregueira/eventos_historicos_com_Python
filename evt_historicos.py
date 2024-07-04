from http import HTTPStatus

import requests
import streamlit as st
from translate import Translator


def get_historical_events(month, day):
    url = f'http://history.muffinlabs.com/date/{month}/{day}'
    response = requests.get(url)
    if response.status_code == HTTPStatus.OK:
        data = response.json()
        events = data['data']['Events']
        return events
    else:
        st.error('Erro ao buscar dados. Por favor, tente novamente.')
        return None


def translate_text(text, dest_language='pt'):
    translator = Translator(to_lang=dest_language)
    translation = translator.translate(text)
    return translation


def main():
    st.title('Eventos Históricos')
    st.markdown('Entre com o dia e o mês e veja os eventos históricos.')
    day = st.number_input(
        'Digite o dia (por exemplo, 1 para 1º):',
        min_value=1,
        max_value=31,
        step=1,
    )
    month = st.number_input(
        'Digite o mês (por exemplo, 7 para julho):',
        min_value=1,
        max_value=12,
        step=1,
    )
    if st.button('Buscar Eventos'):
        events = get_historical_events(month, day)
        if events:
            st.subheader(f'Eventos históricos em {day}/{month}:')
            for event in events:
                translated_text = translate_text(event['text'])
                st.write(f"ANO: {event['year']}")
                st.write(f'Descrição: {translated_text}')
                st.write(f"Link: {event['links'][0]['link']}")
                st.write('---')


if __name__ == '__main__':
    main()
