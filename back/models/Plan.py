# author : Alexxander Lugovskoy
# vk.com/delta85

from datetime import datetime, timedelta
from pydantic import BaseModel

import mysql_connect
from logger import logger
"""
params = {
            'department_id' : str('10b20b9b-915f-6dc5-0156-024b6e41000d'),
            'point_break_even': float(2550000),
            'days_in_mount': float(22),
            'total_proceeds' : float(2550000),

            'proceed_input_percent' : float(21.95),

            'hookah_average_check' : float(333),
            'hookah_proceeds_percent' : float(5.3),

            'bar_proceeds_percent' : float(65.72),
            'bar_people_count' : float(11339),
            'bar_average_check': float(500),

            'kitchen_proceeds_percent' : float(7.03),
            'kitchen_average_check' : float(329),

            'bar_foodcost' : float(-51.5),
            'bar_products_write_off_percent' : float(-0.04),
            'bar_surplus_percent' : float(1.5),
            'bar_failure_percent' : float(-0.5),

            'kitchen_foodcost_percent' : float(-45),
            'kitchen_products_write_off_percent' : float(-1.5),
            'kitchen_surplus_percent' : float(1.0),
            'kitchen_failure_percent' : float(-1.0),

            'fot_labor_zp_povar_percent' : float(-25.0),
            'fot_labor_povar_compensation_rub' : int(0),
            'fot_labor_povar_mat_help_rub' : int(0),

            'fot_labor_admin_zp_rub' : int(-40000),
            'fot_labor_admin_zp_bonus_rub' : int(0),
            'fot_labor_admin_zp_compensation_rub' : int(0),
            'fot_labor_admin_zp_mat_help_rub' : int(0),

            'fot_zp_zvukar' : int(0),
            'fot_zp_zavhoz' : int(0),
            'fot_zp_officiants' : int(0),
            'fot_zp_cashiers' : int(0),
            'fot_zp_hostes' : int(0),
            'fot_zp_barmans' : int(0),
            'total_loosers_zp' : int(-300000),

            'fot_zp_manager' : int(-40000),
            'fot_zp_bu_calc_kadr' : int(-103000),
            'fot_zp_admin_po_rejimy' : int(-132000),

            'personal_apartments_rent_rub' : int(0),
            'personal_food_cost_percent' : float(-0.68),
            'personal_transport_cost_rub' : int(0),
            'personal_medicaments_medosmotr_rub' : int(0),
            'personal_registration_in_ufms_rub' : int(0),

            'rental_of_premises_rub' : int(-500000),
            'communal_rent' : int(0),
            'wanish_cost_percent' : float(-0.16),
            'parking_coupons_rub' : int(0),
            'room_maintenance_rub' : int(0),
            'dizenfection_rub' : int(-3003),
            'kovri_ot_gryazi_rub' : int(0),
            'to_kts_rub' : int(-7000),
            'garbage_removal_rub' : int(0),

            'premises_capital_remont_rub' : int(0),
            'premises_cosmetical_remont_rub' : int(-15000),
            'furniture_updating_rub' : int(-10000),
            'equipment_updating_rub' : int(0),
            'equipment_remont_service_rub' : int(0),
            'air_conditioning_remont_service_rub' : int(0),
            'ventilation_remont_service_rub' : int(0),
            'lamp_remont_service_rub' : int(0),
            'electric_remont_service_rub' : int(0),
            'canalization_remont_service_rub' : int(0),
            'posuda_inventar_updating_percent' : float(-0.35),
            'kitchen_inventar_service_rub' : int(-7000),
            'prochie_ulucheniya_rub' : int(0)

            'orgtechnic_and_cassovie' : int(-2500),
            'packaging_rub' : int(0),
            'hoztovars_percent' : float(-0.4),
            'prochie_rashodniki_percent' : float(-0.14),

            'stationery_rub' : int(-2500),

            #Прочие расходные материалы (значки, браслеты, телефоны POS-материалы, наклейки, дым, номерки, пейджеры)
            'znachki_rub' : int(0),
            'phone_rub' : int(0),
            'nomerki_rub' : int(0),
            'pos_packages_rub' : int(0),
            'control_brasslets_rub' : int(0),
            'eticet_pistol_rub' : int(0),
            'button_call' : int(0),
            'padger' : int(0),
            'smoke' : int(0),
            'stickers' : int(0),

            #Расходы на связь
            'internet_connection_rub' : int(-1500),
            'post_office_rub' : int(0),
            'phone_connection_rub' : int(-1000),
    
            'transport_rub' : int(0),
            'it_and_po_rub' :int(-10500),
            'kkm_rub' : int(-1400),
            'sas_standart_lab_issled_rub' : int(0),
            'musical_design_of_music_rub' : int(-12560),
            'sbis_ofd_rub' : int(-1620),
            'cctv_and_control_rub' : int(0),

            #Финансовые расходы
            'expenses_acquiring_percent' : float(-1.05),
            'expenses_banking_service_percent' : float(-0.09),

            #налоги и отчисления
            'income_tax_usn_envd_rub' : int(0),
            'soc_fonds_percent' : float(-0.93),
            'taxes_fees_fines_rub' : int(0),

            #Реклама и маркетинг
            'fot_adv_specialists_rub' : int(-128000),
            'marketing_events_percent' : float(-5.0),

            #P3
            'p3_accountant_rub' : int(-30000),
            'p3_royalty_rub' : int(0),
            'p3_xx_rub' : int(0)

        }
"""
class Plan():

    def __init__(self, params):
        # ИСХОДНЫЕ ДАННЫЕ (ОБЩИЕ)
        self.department_id = str(params.get('department_id')) #guid ТТ из iiko
        self.point_break_even = float(params.get('point_break_even')) #точка безубыточности
        self.days_in_mount = float(params.get('days_in_mount')) #кол-во учитываемых дней в месяце
        self.total_proceeds = float(params.get('total_proceeds')) #общая выручка в месяц

        #ВЫЧИСЛЯЕМЫЕ ВСПОМОГАТЕЛЬНЫЕ ДАННЫЕ
        self.one_percent = self.total_proceeds / 100 # 1 % от общей выручки


        # <<-- подсчет выручки НАЧАЛО -->>


        self.proceed_input_percent = float(params.get('proceed_input_percent')) # выручка (вход %)
        self.proceed_input_rub = round(int(self.one_percent*self.proceed_input_percent), 2) # выручка (вход руб.)

        #ИСХОДНЫЕ ДАННЫЕ ПО КАЛЬЯНАМ
        self.hookah_average_check = float(params.get('hookah_average_check')) #кальян, средний чек
        self.hookah_proceeds_percent = float(params.get('hookah_proceeds_percent')) #выручка за кальяны в % от общей суммы выручки

        #ВЫЧИСЛЯЕМЫЕ ДАННЫЕ ПО КАЛЬЯНАМ
        self.hookah_proceeds_rub = round(int(self.one_percent*self.hookah_proceeds_percent), 2) # выручка за кальяны
        self.hookah_checks_count = round(int(self.hookah_proceeds_rub/self.hookah_average_check), 2) # приблизительное необходимое количество чеков по кальянам в месяц
        self.hookah_checks_count_in_day = round(int(self.hookah_checks_count / self.days_in_mount), 2) # приблизительное необходимое количество чеков по кальянам в день

        #ИСХОДНЫЕ ДАННЫЕ ПО БАРУ
        self.bar_proceeds_percent = float(params.get('bar_proceeds_percent')) #выручка за бар в % от общей суммы выручки
        self.bar_people_count = float(params.get('bar_people_count')) #количество клиентов бара за месяц
        self.bar_average_check = float(params.get('bar_average_check')) #бар, средний чек

        #ВЫЧИСЛЯЕМЫЕ ДАННЫЕ ПО БАРУ
        self.bar_proceeds_rub = round(int(self.one_percent*self.bar_proceeds_percent), 2) #выручка по бару в месяц
        self.bar_checks_count = round(int(self.bar_proceeds_rub/self.bar_average_check), 2) #приблизительное необходимое количество чеков по бару в месяц
        self.bar_checks_count_in_day = round(int(self.bar_checks_count/self.days_in_mount),2) #приблизительное необходимое количество чеков по бару в день

        #ИСХОДНЫЕ ДАННЫЕ ПО КУХНЕ
        self.kitchen_proceeds_percent = float(params.get('kitchen_proceeds_percent')) #выручка за кухню в % от общей суммы выручки
        self.kitchen_average_check = float(params.get('kitchen_average_check')) #кухня, средний чек

        #ВЫЧИСЛЯЕМЫЕ ДАННЫЕ ПО КУХНЕ
        self.kitchen_proceeds_rub = round(int(self.one_percent*self.kitchen_proceeds_percent), 2) #выручка по кухне в месяц
        self.kitchen_checks_count = round(int(self.kitchen_proceeds_rub/self.kitchen_average_check), 2)#приблизительное необходимое количество чеков по кухне в месяц
        self.kitchen_checks_count_id_day = round(int(self.kitchen_checks_count/self.days_in_mount), 2) #приблизительное необходимое количество чеков по кухне в день

        # <<-- подсчет выручки КОНЕЦ -->>

        #CЕБЕСТОИМОСТЬ ПРОДАЖ БАРА
        self.bar_foodcost_percent = float(params.get('bar_foodcost')) #фудкост бара в %
        self.bar_one_percent = round(int(self.bar_proceeds_rub / 100), 2) # 1% от выручки по бару в месяц
        self.bar_foodcost_rub = round(int(self.bar_one_percent * self.bar_foodcost_percent), 2) # фудкост в рублях
        self.bar_products_write_off_percent = float(params.get('bar_products_write_off_percent')) #списания товаров в %
        self.bar_products_write_off_rub = round(int(self.bar_one_percent * self.bar_products_write_off_percent), 2) #списания товаров в рублях
        self.bar_surplus_percent = float(params.get('bar_surplus_percent')) #излишки по инвентаризации товара в %
        self.bar_surplus_rub = round(int(self.bar_one_percent * self.bar_surplus_percent), 2) #излишки по инвентаризации товара в руб
        self.bar_failure_percent = float(params.get('bar_failure_percent')) #недосдачи по инвентаризации товара в %
        self.bar_failure_rub = round(int(self.bar_one_percent * self.bar_failure_percent), 2) #недосдачи по инвентаризации товара в руб
        self.bar_cost_price_rub = round(int(self.bar_foodcost_rub + self.bar_products_write_off_rub + self.bar_surplus_rub + self.bar_failure_rub), 2) #CЕБЕСТОИМОСТЬ ПРОДАЖ БАРА в руб
        self.bar_cost_price_percent = round(float(self.bar_cost_price_rub/self.bar_one_percent), 2) #CЕБЕСТОИМОСТЬ ПРОДАЖ БАРА в %

        # CЕБЕСТОИМОСТЬ ПРОДАЖ КУХНЯ
        self.kitchen_foodcost_percent = float(params.get('kitchen_foodcost_percent')) #фудкост кухни в %
        self.kitchen_one_percent = round(int(self.kitchen_proceeds_rub / 100), 2) #1% от выручки по кухне в месяц
        self.kitchen_foodcost_rub = round(int(self.kitchen_one_percent*self.kitchen_foodcost_percent), 2) # фудкост кухни в рублях
        self.kitchen_products_write_off_percent = float(params.get('kitchen_products_write_off_percent')) #списания товаров в %
        self.kitchen_products_write_off_rub = round(int(self.kitchen_one_percent * self.kitchen_products_write_off_percent), 2) #списания товаров в рублях
        self.kitchen_surplus_percent = float(params.get('kitchen_surplus_percent'))  # излишки по инвентаризации товара в %
        self.kitchen_surplus_rub = round(int(self.kitchen_one_percent * self.kitchen_surplus_percent) , 2) # излишки по инвентаризации товара в руб
        self.kitchen_failure_percent = float(params.get('kitchen_failure_percent')) # недосдачи по инвентаризации товара в %
        self.kitchen_failure_rub = round(int(self.kitchen_one_percent * self.kitchen_failure_percent), 2)  # недосдачи по инвентаризации товара в руб
        self.kitchen_cost_price_rub = round(int(self.kitchen_foodcost_rub + self.kitchen_products_write_off_rub + self.kitchen_surplus_rub + self.kitchen_failure_rub), 2) #CЕБЕСТОИМОСТЬ ПРОДАЖ КУХНЯ в руб

        self.kitchen_cost_price_percent = round(float(self.kitchen_cost_price_rub/self.kitchen_one_percent), 2) #CЕБЕСТОИМОСТЬ ПРОДАЖ КУХНЯ в %

        #повар
        self.fot_labor_zp_povar_percent = round(float(params.get('fot_labor_zp_povar_percent')), 2) #Начисления повар %
        self.fot_labor_zp_povar_rub = round(int(self.kitchen_one_percent * self.fot_labor_zp_povar_percent), 2) #Начисления повар (руб)
        self.fot_labor_povar_compensation_rub = int(params.get('fot_labor_povar_compensation_rub')) #Компенсации_Повар(руб)
        self.fot_labor_povar_mat_help_rub = int(params.get('fot_labor_povar_mat_help_rub')) #Пособия,Мат.помощь_Повар руб
        self.fot_labor_povar_zp_full_rub = round(int(self.fot_labor_zp_povar_rub+self.fot_labor_povar_compensation_rub+self.fot_labor_povar_mat_help_rub), 2) #Заработная плата (ФОТ+бонусы)_Повар руб
        self.fot_labor_povar_zp_full_percent = round(float(self.fot_labor_povar_zp_full_rub/self.kitchen_one_percent), 2) #Заработная плата (ФОТ+бонусы)_Повар %

        #администратор
        self.fot_labor_admin_zp_rub = round(int(params.get('fot_labor_admin_zp_rub')), 2)
        self.fot_labor_admin_zp_bonus_rub = round(int(params.get('fot_labor_admin_zp_bonus_rub')), 2)
        self.fot_labor_admin_zp_compensation_rub = round(int(params.get('fot_labor_admin_zp_compensation_rub')), 2)
        self.fot_labor_admin_zp_mat_help_rub = round(int(params.get('fot_labor_admin_zp_mat_help_rub')), 2)
        self.fpr_labor_admin_zp_full = round(self.fot_labor_admin_zp_rub+ self.fot_labor_admin_zp_bonus_rub+self.fot_labor_admin_zp_compensation_rub+self.fot_labor_admin_zp_mat_help_rub, 2)

        #зп остальных неудачников
        self.fot_zp_zvukar = params.get('fot_zp_zvukar')
        self.fot_zp_zavhoz = params.get('fot_zp_zavhoz')
        self.fot_zp_officiants = params.get('fot_zp_officiants')
        self.fot_zp_cashiers = params.get('fot_zp_cashiers')
        self.fot_zp_hostes = params.get('fot_zp_hostes')
        self.fot_zp_barmans = params.get('fot_zp_barmans')
        self.total_loosers_zp = round(params.get('total_loosers_zp') + self.fot_zp_zvukar+self.fot_zp_zavhoz+self.fot_zp_officiants+self.fot_zp_cashiers+self.fot_zp_hostes+self.fot_zp_barmans, 2)

        #ФОТ административного персонала
        self.fot_zp_manager = params.get('fot_zp_manager')
        self.fot_zp_bu_calc_kadr = params.get('fot_zp_bu_calc_kadr')
        self.fot_zp_admin_po_rejimy = params.get('fot_zp_admin_po_rejimy')
        self.total_administration_zp = round(self.fot_zp_manager + self.fot_zp_bu_calc_kadr + self.fot_zp_admin_po_rejimy, 2)

        self.personal_apartments_rent_rub = params.get('personal_apartments_rent_rub') #Аренда квартир для персонала
        self.personal_food_cost_percent = params.get('personal_food_cost_percent')  #Питание сотрудников в процентах
        self.personal_food_cost_rub = self.one_percent * self.personal_food_cost_percent #Питание сотрудников в рублях
        self.personal_transport_cost_rub = params.get('personal_transport_cost_rub') #Проезд сотрудников
        self.personal_medicaments_medosmotr_rub = params.get('personal_medicaments_medosmotr_rub') #Медосмотр персонала/затраты на медикаменты
        self.personal_registration_in_ufms_rub = params.get('personal_registration_in_ufms_rub') #Регистрация сотрудников в УФМС

        self.rental_of_premises_rub = params.get('rental_of_premises_rub') #аренда помещения в рублях
        self.rental_of_premises_percent = round(self.rental_of_premises_rub / self.one_percent, 2) #аренда помещения в %
        self.communal_rent = params.get('communal_rent') #коммунальные услуги в руб
        self.wanish_cost_percent = params.get('wanish_cost_percent') #стоимость моющих средств в %
        self.wanish_cost_rub = round(int(self.one_percent * self.wanish_cost_percent), 2) #стоимость моющих средств в руб
        self.parking_coupons_rub = params.get('parking_coupons_rub') #парковочные купоны
        self.room_maintenance_rub = params.get('room_maintenance_rub') #обслуживание помещения
        self.dizenfection_rub = params.get('dizenfection_rub') #дизенфекция
        self.kovri_ot_gryazi_rub = params.get('kovri_ot_gryazi_rub') #коврики от грязи
        self.to_kts_rub = params.get('to_kts_rub') #Охрана, безопаснось и тех. обслуж пожарной (ТО КТС)
        self.garbage_removal_rub = params.get('garbage_removal_rub') #вывоз мусора

        #РЕМОНТ И ОБСЛУЖИВАНИЕ
        self.premises_capital_remont_rub = params.get('premises_capital_remont_rub') #затраты на копитальный ремонт
        self.premises_cosmetical_remont_rub = params.get('premises_cosmetical_remont_rub') #затраты на косметический ремонт
        self.furniture_updating_rub = params.get('furniture_updating_rub') #затраты на обновление мебели
        self.equipment_remont_service_rub = params.get('equipment_remont_service_rub') #затраты на ремонт и обслуживание оборудования
        self.air_conditioning_remont_service_rub = params.get('air_conditioning_remont_service_rub') #затраты на ремонт и обслуживание кондиционеров
        self.ventilation_remont_service_rub = params.get('ventilation_remont_service_rub') #затраты на ремонт и обслуживание вентиляции
        self.lamp_remont_service_rub = params.get('lamp_remont_service_rub') #затраты на ремонт/обслуживание/замену светильников
        self.electric_remont_service_rub = params.get('electric_remont_service_rub') #затраты на обслуживание и ремонт электрики
        self.canalization_remont_service_rub = params.get('canalization_remont_service_rub') #затраты на ремонт и обслуживание канализации
        self.posuda_inventar_updating_percent = params.get('posuda_inventar_updating_percent') #затраты на обновление посуды и инвентаря
        self.posuda_inventar_updating_rub = round(int(self.one_percent * self.posuda_inventar_updating_percent), 2)
        self.kitchen_inventar_service_rub = params.get('kitchen_inventar_service_rub') #содержание и ремонт куханного инвентаря
        self.prochie_ulucheniya_rub = params.get('prochie_ulucheniya_rub') #прочие текущие улучшения
        self.updating_and_remont_rub =  round(self.premises_capital_remont_rub + self.premises_cosmetical_remont_rub + self.furniture_updating_rub +self.equipment_remont_service_rub + self.air_conditioning_remont_service_rub + self.ventilation_remont_service_rub + self.lamp_remont_service_rub + self.electric_remont_service_rub + self.canalization_remont_service_rub + self.posuda_inventar_updating_rub + self.kitchen_inventar_service_rub +self.prochie_ulucheniya_rub, 2) #Текущии улучшения (обновление/ремонт и обслуживание)
        self.updating_and_remont_percent = round(self.updating_and_remont_rub / self.one_percent, 2)

        self.orgtechnic_and_cassovie = params.get('orgtechnic_and_cassovie') #Расходные материалы для оргтехники/кассовых аппаратов
        self.packaging_rub = params.get('packaging_rub')
        self.hoztovars_percent = params.get('hoztovars_percent')
        self.prochie_rashodniki_percent = params.get('prochie_rashodniki_percent')
        self.hoztovars_rub = round(int(self.hoztovars_percent * self.one_percent), 2)
        self.prochie_rashodniki_rub = round(int(self.prochie_rashodniki_percent * self.one_percent), 2)

        self.stationery_rub = params.get('stationery_rub') #кантовары

        # Расходы на связь
        self.internet_connection_rub = params.get('internet_connection_rub')
        self.post_office_rub = params.get('post_office_rub')
        self.phone_connection_rub = params.get('phone_connection_rub')
        self.full_cost_connection =  round(self.internet_connection_rub + self.post_office_rub + self.phone_connection_rub, 2) #сумма расходов на всю связь

        self.transport_rub = params.get('transport_rub') #расходы на транспорт
        self.it_and_po_rub = params.get('it_and_po_rub') #расходы на ИТ и ПО
        self.kkm_rub = params.get('kkm_rub') #ККМ
        self.sas_standart_lab_issled_rub = params.get('sas_standart_lab_issled_rub') #СЭС, стандартизация, лабораторные исследования
        self.musical_design_of_music_rub = params.get('musical_design_of_music_rub') #Музыкальное оформление бизнеса (РАО, ВОИС)
        self.sbis_ofd_rub = params.get('sbis_ofd_rub') #Прочие админ расход (СБИС 850 внесение изменений , ОФД оператор фискальных данных)
        self.cctv_and_control_rub = params.get('cctv_and_control_rub') #Расходы на видеомониторинг и контроль

        #ФИНАНСОВЫЕ РАСХОДЫ (ВХОДНЫЕ ДАННЫЕ)
        self.expenses_acquiring_percent = params.get('expenses_acquiring_percent') #Финансовые расходы (эквайринг)
        self.expenses_banking_service_percent = params.get('expenses_banking_service_percent') #Услуги банка
        # ФИНАНСОВЫЕ РАСХОДЫ (ВЫЧИСЛЯЕМЫЕ ДАННЫЕ)
        self.expenses_acquiring_percent_rub = round(int(self.one_percent * self.expenses_acquiring_percent), 2)
        self.expenses_banking_service_rub = round(int(self.one_percent * self.expenses_banking_service_percent), 2)
        self.financial_expenses_rub = round(self.expenses_acquiring_percent_rub + self.expenses_banking_service_rub, 2)
        self.financial_expenses_percent = round(self.expenses_acquiring_percent + self.expenses_banking_service_percent, 2)

        #НАЛОГИ И ОТЧИСЛЕНИЯ (ВХОДНЫЕ ДАННЫЕ)
        self.income_tax_usn_envd_rub = params.get('income_tax_usn_envd_rub') #Налог на прибыль/УСН/ЕНВД
        self.soc_fonds_percent = params.get('soc_fonds_percent') #Отчисления в соц фонды (ПФР и ФСС, НДФЛ)
        self.taxes_fees_fines_rub = params.get('taxes_fees_fines_rub') #Налоги, сборы, штрафы (кроме налога на прибыль, УСН, ЕНВД)

        # НАЛОГИ И ОТЧИСЛЕНИЯ (ВЫЧИСЛЯЕМЫЕ ДАННЫЕ)
        self.soc_fonds_rub = round(self.one_percent * self.soc_fonds_percent, 2)
        self.total_taxes_rub = round(self.income_tax_usn_envd_rub + self.soc_fonds_rub + self.taxes_fees_fines_rub, 2)
        self.total_taxes_percent = round(self.total_taxes_rub / self.one_percent, 2)

        #РЕКЛАМА И МАРКЕТИНГ(ВХОДНЫЕ ДАННЫЕ)
        self.fot_adv_specialists_rub = params.get('fot_adv_specialists_rub')
        self.marketing_events_percent = params.get('marketing_events_percent')
        #РЕКЛАМА И МАРКЕТИНГ(ВЫЧИСЛЯЕМЫЕ ДАННЫЕ)
        self.marketing_events_rub = round(self.one_percent * self.marketing_events_percent, 2)
        self.rm_p2_rub = round(int(self.fot_adv_specialists_rub + self.marketing_events_rub), 2)
        self.rm_p2_percent = round(self.rm_p2_rub / self.one_percent, 2)

        #P3
        self.p3_accountant_rub = params.get('p3_accountant_rub')
        self.p3_royalty_rub = params.get('p3_royalty_rub')
        self.p3_xx_rub = params.get('p3_xx_rub')
        self.p3_sum_rub = round(self.p3_accountant_rub + self.p3_royalty_rub + self.p3_xx_rub, 2)

        #ФОТ / Laborcoct
        self.total_fot_and_laborcoct_rub = round(self.fot_labor_povar_zp_full_rub + self.fpr_labor_admin_zp_full + self.total_loosers_zp + self.total_administration_zp, 2)
        #Сумма расходов ОП1:
        self.op1_total_rub = round(self.bar_cost_price_rub + self.kitchen_cost_price_rub + self.total_fot_and_laborcoct_rub + self.personal_apartments_rent_rub + self.personal_food_cost_rub + self.personal_transport_cost_rub + self.personal_medicaments_medosmotr_rub + self.personal_registration_in_ufms_rub + self.rental_of_premises_rub + self.communal_rent + self.wanish_cost_rub + self.dizenfection_rub + self.parking_coupons_rub + self.room_maintenance_rub + self.kovri_ot_gryazi_rub + self.to_kts_rub + self.garbage_removal_rub + self.updating_and_remont_rub +self.orgtechnic_and_cassovie +self.hoztovars_rub +self.prochie_rashodniki_rub + self.stationery_rub + self.full_cost_connection + self.transport_rub + self.it_and_po_rub + self.kkm_rub + self.sas_standart_lab_issled_rub + self.musical_design_of_music_rub +self.sbis_ofd_rub +self.cctv_and_control_rub +self.financial_expenses_rub + self.total_taxes_rub, 2)
        self.op1_total_percent = round(self.op1_total_rub / self.one_percent, 2)

        #СУММА РАСХОДОВ(ОБЩАЯ)
        self.total_expenses_rub = round(self.op1_total_rub + self.rm_p2_rub +self.p3_sum_rub, 2)
        self.total_expenses_percent = round(self.total_expenses_rub / self.one_percent, 2)

        #КОНЕЧНЫЙ ПРОФИТ
        self.total_profit_rub = round(int(self.total_proceeds + self.total_expenses_rub), 2) #Прибыль без учета возврата инвестиций/ распределения
        self.total_profit_percent = round(self.total_profit_rub / self.total_proceeds, 2) #Рентабельность продаж, %




#a = Plan(params)

"""
print("себестоимость продаж бара(руб): ", a.bar_cost_price_rub) #ok
print("себестоимость продаж КУХНЯ (руб): ", a.kitchen_cost_price_rub) #ok
print("ФОТ / Labor coct руб: ", a.total_fot_and_laborcoct_rub) #ok
print("Питание сотрудников (списание продуктов) руб: ", a.personal_food_cost_rub) #ok
print("Аренда помещения руб: ", a.rental_of_premises_rub) #ok
print("Моющие средства: ", a.wanish_cost_rub) #ok
print("Дизенфекция руб: ", a.dizenfection_rub) #ok
print("Охрана руб:", a.to_kts_rub)
print("Текущие улучшения (обновление/ремонт и обслуживание) руб : ", a.updating_and_remont_rub)
print("Расходные материалы для оргтехники/кассовых аппаратов: ", a.orgtechnic_and_cassovie)
print("Хозтовары: ", a.hoztovars_rub)
print("Прочие расходные материалы: ", a.prochie_rashodniki_rub)
print("Канцтовары: ", a.stationery_rub)
print("Расходы на связь: ", a.full_cost_connection)
print("ИТ услуги и ПО", a.it_and_po_rub)
print("Сумма расходов ОП1 руб: ", a.op1_total_rub)
print("Сумма расходов ОП1 %: ", a.op1_total_percent)
print("Реклама и маркетинг Р2 руб:", a.rm_p2_rub)
print("Сумма расходов Р3 руб:", a.p3_sum_rub)
print("Сумма расходов(Общая) руб: ", a.total_expenses_rub)
print("Сумма расходов (общая) %: ", a.total_expenses_percent)
print("Прибыль без учета возврата инвестиций/ распределения руб: ", a.total_profit_rub)
print("Рентабельность продаж, %: ", a.total_profit_percent)
print(a.__dict__)
"""
