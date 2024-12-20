from flask import Flask, request, jsonify, Response
from dotenv import load_dotenv
import os
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

load_dotenv()

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login_handler():
    if request.method == 'POST':
        data = request.json
        login = data.get('login')
        password = data.get('password')

        if login == "admin" and password == "correct_password":
            data_token = jsonify({"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJFeHAiOiIyMDIzLTEyLTE4VDEyOjI5OjE5LjEwNjg0MTQzOVoiLCJVc2VyTG9naW4iOiJhZG1pbiJ9.0Dvg7vFTrdSX2F4751ae6Id9weC5ATvF1sQPuvejiFE"})
            return data_token
        else:
            return Response(status=401)
    else:
        return Response(status=405)


@app.route('/check', methods=['POST'])
def check_handler():
    if request.method == 'POST':
        token_str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJFeHAiOiIyMDIzLTEyLTE4VDEyOjI5OjE5LjEwNjg0MTQzOVoiLCJVc2VyTG9naW4iOiJhZG1pbiJ9.0Dvg7vFTrdSX2F4751ae6Id9weC5ATvF1sQPuvejiFE'
        token_header = request.headers.get('Authorization')
        correct_token = token_header.split(' ')
        if correct_token[1] == token_str:
            return Response(status=204)
        else:
            return Response(status=401)
    else:
        return Response(status=405)

@app.route('/grants', methods=['GET'])
def grants_handler():
    if request.method == 'GET':
        return jsonify({"grants":[{"id":1,"title":"Стипендиальный конкурс","source_url":"https://fondpotanin.ru/competitions/fellowships/","filter_values":{"cutting_off_criteria":[],"project_direction":[],"amount":0,"legal_form":[],"age":0}},{"id":2,"title":"Спорт для всех","source_url":"https://fondpotanin.ru/competitions/sport-dlya-vsekh/","filter_values":{"project_direction":[],"amount":0,"legal_form":[],"age":0,"cutting_off_criteria":[]}},{"id":3,"title":"Музей 4.0","source_url":"https://fondpotanin.ru/competitions/muzey-4-0/","filter_values":{"project_direction":[],"amount":0,"legal_form":[],"age":0,"cutting_off_criteria":[]}},{"id":4,"title":"Грантовый конкурс для преподавателей магистратуры","source_url":"https://fondpotanin.ru/competitions/professors-grants/","filter_values":{"project_direction":[],"amount":0,"legal_form":[],"age":0,"cutting_off_criteria":[]}},{"id":5,"title":"Индустриальный эксперимент","source_url":"https://fondpotanin.ru/competitions/industrial/","filter_values":{"age":0,"cutting_off_criteria":[],"project_direction":[],"amount":0,"legal_form":[]}},{"id":6,"title":"Креативный музей","source_url":"https://fondpotanin.ru/competitions/kreativnyy-muzey/","filter_values":{"project_direction":[],"amount":0,"legal_form":[],"age":0,"cutting_off_criteria":[]}},{"id":7,"title":"Профессиональное развитие","source_url":"https://fondpotanin.ru/competitions/konkurs-professionalnogo-razvitiya/","filter_values":{"legal_form":[],"age":0,"cutting_off_criteria":[],"project_direction":[],"amount":0}},{"id":8,"title":"Практики личной филантропии и альтруизма","source_url":"https://fondpotanin.ru/competitions/individual-giving-and-volunteering/","filter_values":{"age":0,"cutting_off_criteria":[],"project_direction":[],"amount":0,"legal_form":[]}},{"id":9,"title":"#фондпотанина25","source_url":"https://fondpotanin.ru/competitions/fondpotanina25/","filter_values":{"project_direction":[],"amount":0,"legal_form":[],"age":0,"cutting_off_criteria":[]}},{"id":10,"title":"Школа Фонда","source_url":"https://fondpotanin.ru/competitions/shkola-fonda/","filter_values":{"age":0,"cutting_off_criteria":[],"project_direction":[],"amount":0,"legal_form":[]}},{"id":11,"title":"Программа стажировки студентов МГИМО (совместно с МИД РФ)","source_url":"https://fondpotanin.ru/competitions/programma-stazhirovki-studentov-mgimo-sovmestno-s-mid-rf/","filter_values":{"legal_form":[],"age":0,"cutting_off_criteria":[],"project_direction":[],"amount":0}},{"id":12,"title":"Центры знаний по социальной поддержке","source_url":"https://fondpotanin.ru/competitions/socialsupport/","filter_values":{"project_direction":[],"amount":0,"legal_form":[],"age":0,"cutting_off_criteria":[]}},{"id":13,"title":"Российско-европейская программа обмена Philanthropic Leadership Platform: Russia-Europe","source_url":"https://fondpotanin.ru/competitions/rossiysko-evropeyskaya-programma-obmena-philanthropic-leadership-platform-russia-europe/","filter_values":{"project_direction":[],"amount":0,"legal_form":[],"age":0,"cutting_off_criteria":[]}},{"id":14,"title":"Социальные финансы","source_url":"https://fondpotanin.ru/competitions/oxfordsocialfinance/","filter_values":{"project_direction":[],"amount":0,"legal_form":[],"age":0,"cutting_off_criteria":[]}},{"id":15,"title":"Олимпийские стипендии","source_url":"https://fondpotanin.ru/competitions/olimpiyskie-stipendii/","filter_values":{"project_direction":[],"amount":0,"legal_form":[],"age":0,"cutting_off_criteria":[]}},{"id":16,"title":"Школа филантропии","source_url":"https://fondpotanin.ru/competitions/shkola-filantropii/","filter_values":{"project_direction":[],"amount":0,"legal_form":[],"age":0,"cutting_off_criteria":[]}},{"id":17,"title":"Инициатива «Музей. Сила места»","source_url":"https://fondpotanin.ru/competitions/muzey-sila-mesta/","filter_values":{"cutting_off_criteria":[],"project_direction":[],"amount":0,"legal_form":[],"age":0}},{"id":18,"title":"Точка опоры","source_url":"https://fondpotanin.ru/competitions/tochka-opory/","filter_values":{"project_direction":[],"amount":0,"legal_form":[],"age":0,"cutting_off_criteria":[]}},{"id":19,"title":"Конкурс на поддержку центров социальных инноваций в сфере культуры","source_url":"https://fondpotanin.ru/competitions/konkurs-na-podderzhku-tsentrov-sotsialnykh-innovatsiy-v-sfere-kultury/","filter_values":{"project_direction":[],"amount":0,"legal_form":[],"age":0,"cutting_off_criteria":[]}},{"id":20,"title":"Конкурс по приглашению для грантополучателей антикризисных конкурсов","source_url":"https://fondpotanin.ru/competitions/konkurs-po-priglasheniyu-dlya-grantopoluchateley-antikrizisnykh-konkursov/","filter_values":{"project_direction":[],"amount":0,"legal_form":[],"age":0,"cutting_off_criteria":[]}}],"filters_mapping":{"age":{"title":"Возраст участников","mapping":{}},"project_direction":{"title":"Направление проекта","mapping":{"0":{"title":"Не указано"},"1":{"title":"Выявление и поддержка молодых талантов"},"2":{"title":"Защита прав и свобод"},"3":{"title":"Охрана здоровья"}}},"legal_form":{"title":"Отсекающие критерии","mapping":{"0":{"title":"Не указано"},"1":{"title":"Юр. лицо"},"2":{"title":"Физ. лицо"}}},"cutting_off_criteria":{"title":"Отсекающие критерии","mapping":{"2":{"title":"Для студентов"},"3":{"title":"Для асприантов"},"0":{"title":"Не указано"},"1":{"title":"Для школьников"}}},"amount":{"title":"Сумма","mapping":{}}},"filters_order":["project_direction","amount","legal_form","age","cutting_off_criteria"],"meta":{"current_page":1,"total_pages":13}})
    else:
        return Response(status=405)


if __name__ == '__main__':
    app.debug = True