from fastapi import FastAPI
from models import Plan
from pydantic import BaseModel, Json
from typing import Dict, Optional
from fastapi.middleware.cors import CORSMiddleware

class Item(BaseModel):
    point_break_even: int
    days_in_mount: int
    total_proceeds: int

    proceed_input_percent: float

    hookah_average_check: float
    hookah_proceeds_percent: float

    bar_proceeds_percent: float
    bar_people_count: float
    bar_average_check: float

    kitchen_proceeds_percent: float
    kitchen_average_check: float

    bar_foodcost: float
    bar_products_write_off_percent: float
    bar_surplus_percent: float
    bar_failure_percent: float

    kitchen_foodcost_percent: float
    kitchen_products_write_off_percent: float
    kitchen_surplus_percent: float
    kitchen_failure_percent: float

    fot_labor_zp_povar_percent: float
    fot_labor_povar_compensation_rub: Optional[int] = 0 #Компенсации_Повар(руб)
    fot_labor_povar_mat_help_rub: Optional[int] = 0 #Пособия,Мат.помощь_Повар(руб)

    fot_labor_admin_zp_rub: int
    fot_labor_admin_zp_bonus_rub: Optional[int] = 0
    fot_labor_admin_zp_compensation_rub: Optional[int] = 0
    fot_labor_admin_zp_mat_help_rub: Optional[int] = 0

    fot_zp_zvukar: Optional[int] = 0
    fot_zp_zavhoz: Optional[int] = 0
    fot_zp_officiants: Optional[int] = 0
    fot_zp_cashiers: Optional[int] = 0
    fot_zp_hostes: Optional[int] = 0
    fot_zp_barmans: Optional[int] = 0
    total_loosers_zp: Optional[int] = 0

    fot_zp_manager: int
    fot_zp_bu_calc_kadr: int
    fot_zp_admin_po_rejimy: int

    personal_apartments_rent_rub: Optional[int] = 0
    personal_food_cost_percent: float
    personal_transport_cost_rub: Optional[int] = 0
    personal_medicaments_medosmotr_rub: Optional[int] = 0
    personal_registration_in_ufms_rub: Optional[int] = 0

    rental_of_premises_rub: int
    communal_rent: int
    wanish_cost_percent: float
    parking_coupons_rub: int
    room_maintenance_rub: Optional[int] = 0
    dizenfection_rub: int
    kovri_ot_gryazi_rub: Optional[int] = 0
    to_kts_rub: int
    garbage_removal_rub: Optional[int] = 0

    premises_capital_remont_rub: Optional[int] = 0
    premises_cosmetical_remont_rub: Optional[int] = 0
    furniture_updating_rub: Optional[int] = 0
    equipment_updating_rub: Optional[int] = 0
    equipment_remont_service_rub: Optional[int] = 0
    air_conditioning_remont_service_rub: Optional[int] = 0
    ventilation_remont_service_rub: Optional[int] = 0
    lamp_remont_service_rub: Optional[int] = 0
    electric_remont_service_rub: Optional[int] = 0
    canalization_remont_service_rub: Optional[int] = 0
    posuda_inventar_updating_percent: Optional[int] = 0
    kitchen_inventar_service_rub: Optional[int] = 0
    prochie_ulucheniya_rub: Optional[int] = 0

    orgtechnic_and_cassovie: int
    packaging_rub: Optional[int] = 0
    hoztovars_percent: float
    prochie_rashodniki_percent: float

    stationery_rub: int

    # Прочие расходные материалы (значки, браслеты, телефоны POS-материалы, наклейки, дым, номерки, пейджеры)
    znachki_rub:  Optional[int] = 0
    phone_rub: Optional[int] = 0
    nomerki_rub: Optional[int] = 0
    pos_packages_rub: Optional[int] = 0
    control_brasslets_rub: Optional[int] = 0
    eticet_pistol_rub: Optional[int] = 0
    button_call: Optional[int] = 0
    padger: Optional[int] = 0
    smoke: Optional[int] = 0
    stickers: Optional[int] = 0

    # Расходы на связь
    internet_connection_rub: int
    post_office_rub: Optional[int] = 0
    phone_connection_rub: int

    transport_rub: Optional[int] = 0
    it_and_po_rub: int
    kkm_rub: int
    sas_standart_lab_issled_rub: int
    musical_design_of_music_rub: int
    sbis_ofd_rub: int
    cctv_and_control_rub: Optional[int] = 0

    # Финансовые расходы
    expenses_acquiring_percent: float
    expenses_banking_service_percent: float

    # налоги и отчисления
    income_tax_usn_envd_rub: Optional[int] = 0
    soc_fonds_percent: float
    taxes_fees_fines_rub: Optional[int] = 0

    # Реклама и маркетинг
    fot_adv_specialists_rub: int
    marketing_events_percent: float

    # P3
    p3_accountant_rub: int
    p3_royalty_rub: Optional[int] = 0
    p3_xx_rub: Optional[int] = 0


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/sayHello/")
async def sayHello(message):
    return {"message" : message}

@app.post("/setPlan/")
async def setPlan(params : Item):
    plan = Plan.Plan(params.__dict__)
    return plan.__dict__


"""
@app.get("/keyword-weights/", response_model=Dict[str, float])
async def read_keyword_weights():
    return {"foo": 2.3, "bar": 3.4}
"""