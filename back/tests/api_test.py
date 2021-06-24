import requests
import json
from pprint import pprint

params = {
    'department_id': str('10b20b9b-915f-6dc5-0156-024b6e41000d'),
    'point_break_even': float(2550000),
    'days_in_mount': float(22),
    'total_proceeds': float(2550000),

    'proceed_input_percent': float(21.95),

    'hookah_average_check': float(333),
    'hookah_proceeds_percent': float(5.3),

    'bar_proceeds_percent': float(65.72),
    'bar_people_count': float(11339),
    'bar_average_check': float(500),

    'kitchen_proceeds_percent': float(7.03),
    'kitchen_average_check': float(329),

    'bar_foodcost': float(-51.5),
    'bar_products_write_off_percent': float(-0.04),
    'bar_surplus_percent': float(1.5),
    'bar_failure_percent': float(-0.5),

    'kitchen_foodcost_percent': float(-45),
    'kitchen_products_write_off_percent': float(-1.5),
    'kitchen_surplus_percent': float(1.0),
    'kitchen_failure_percent': float(-1.0),

    'fot_labor_zp_povar_percent': float(-25.0),
    'fot_labor_povar_compensation_rub': int(0),
    'fot_labor_povar_mat_help_rub': int(0),

    'fot_labor_admin_zp_rub': int(-40000),
    'fot_labor_admin_zp_bonus_rub': int(0),
    'fot_labor_admin_zp_compensation_rub': int(0),
    'fot_labor_admin_zp_mat_help_rub': int(0),

    'fot_zp_zvukar': int(0),
    'fot_zp_zavhoz': int(0),
    'fot_zp_officiants': int(0),
    'fot_zp_cashiers': int(0),
    'fot_zp_hostes': int(0),
    'fot_zp_barmans': int(0),
    'total_loosers_zp': int(-300000),

    'fot_zp_manager': int(-40000),
    'fot_zp_bu_calc_kadr': int(-103000),
    'fot_zp_admin_po_rejimy': int(-132000),

    'personal_apartments_rent_rub': int(0),
    'personal_food_cost_percent': float(-0.68),
    'personal_transport_cost_rub': int(0),
    'personal_medicaments_medosmotr_rub': int(0),
    'personal_registration_in_ufms_rub': int(0),

    'rental_of_premises_rub': int(-500000),
    'communal_rent': int(0),
    'wanish_cost_percent': float(-0.16),
    'parking_coupons_rub': int(0),
    'room_maintenance_rub': int(0),
    'dizenfection_rub': int(-3003),
    'kovri_ot_gryazi_rub': int(0),
    'to_kts_rub': int(-7000),
    'garbage_removal_rub': int(0),

    'premises_capital_remont_rub': int(0),
    'premises_cosmetical_remont_rub': int(-15000),
    'furniture_updating_rub': int(-10000),
    'equipment_updating_rub': int(0),
    'equipment_remont_service_rub': int(0),
    'air_conditioning_remont_service_rub': int(0),
    'ventilation_remont_service_rub': int(0),
    'lamp_remont_service_rub': int(0),
    'electric_remont_service_rub': int(0),
    'canalization_remont_service_rub': int(0),
    'posuda_inventar_updating_percent': float(-0.35),
    'kitchen_inventar_service_rub': int(-7000),
    'prochie_ulucheniya_rub': int(0),

    'orgtechnic_and_cassovie': int(-2500),
    'packaging_rub': int(0),
    'hoztovars_percent': float(-0.4),
    'prochie_rashodniki_percent': float(-0.14),

    'stationery_rub': int(-2500),

    # Прочие расходные материалы (значки, браслеты, телефоны POS-материалы, наклейки, дым, номерки, пейджеры)
    'znachki_rub': int(0),
    'phone_rub': int(0),
    'nomerki_rub': int(0),
    'pos_packages_rub': int(0),
    'control_brasslets_rub': int(0),
    'eticet_pistol_rub': int(0),
    'button_call': int(0),
    'padger': int(0),
    'smoke': int(0),
    'stickers': int(0),

    # Расходы на связь
    'internet_connection_rub': int(-1500),
    'post_office_rub': int(0),
    'phone_connection_rub': int(-1000),

    'transport_rub': int(0),
    'it_and_po_rub': int(-10500),
    'kkm_rub': int(-1400),
    'sas_standart_lab_issled_rub': int(0),
    'musical_design_of_music_rub': int(-12560),
    'sbis_ofd_rub': int(-1620),
    'cctv_and_control_rub': int(0),

    # Финансовые расходы
    'expenses_acquiring_percent': float(-1.05),
    'expenses_banking_service_percent': float(-0.09),

    # налоги и отчисления
    'income_tax_usn_envd_rub': int(0),
    'soc_fonds_percent': float(-0.93),
    'taxes_fees_fines_rub': int(0),

    # Реклама и маркетинг
    'fot_adv_specialists_rub': int(-128000),
    'marketing_events_percent': float(-5.0),

    # P3
    'p3_accountant_rub': int(-30000),
    'p3_royalty_rub': int(0),
    'p3_xx_rub': int(0)

}

r = requests.post('http://127.0.0.1:8000/setPlan/', json = params)
print(json.dumps(params))
print(r.json())