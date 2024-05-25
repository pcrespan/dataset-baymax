import numpy as np

from src.Predictions.DecisionTreeModel import useDecisionTree
from src.Predictions.RandomForestModel import useRandomForest
from src.Predictions.KNeighborsModel import useKNeighbors
from src.Predictions.SVCModel import useSVC

def predict(symptonsData):
    formattedSymptons = [];
    options = getDatasetColumns();
    
    for i in range(0, len(options)):
        formattedSymptons.append(0);

    for i in range(0, len(symptonsData)):
        index = options.index(symptonsData[i]);
        formattedSymptons[index] = 1;
    
    formattedSymptons = np.array(formattedSymptons).reshape(1, -1);

    dtResult = useDecisionTree(formattedSymptons);
    rfResult = useRandomForest(formattedSymptons);
    knResult = useKNeighbors(formattedSymptons);
    svcResult = useSVC(formattedSymptons);

    return [
        {
            "method": "DecisionTree",
            "prognosis": dtResult[0],
            "accuracy": dtResult[1],
        },
        {
            "method": "RandomForest",
            "prognosis": rfResult[0],
            "accuracy": rfResult[1],
        },
        {
            "method": "K-nearest",
            "prognosis": knResult[0],
            "accuracy": knResult[1],
        },
        {
            "method": "SVC",
            "prognosis": svcResult[0],
            "accuracy": svcResult[1],
        },
    ];

def getSymptons():
    return [
        {
            "key": "itching",
            "en": "itching",
            "ptbr": "coceira",
        },
        {
            "key": "skin_rash",
            "en": "skin_rash",
            "ptbr": "erupções_cutâneas",
        },
        {
            "key": "nodal_skin_eruptions",
            "en": "nodal_skin_eruptions",
            "ptbr": "erupções_nodulares_na_pele",
        },
        {
            "key": "continuous_sneezing",
            "en": "continuous_sneezing",
            "ptbr": "espirros_contínuos",
        },
        {
            "key": "shivering",
            "en": "shivering",
            "ptbr": "tremores",
        },
        {
            "key": "chills",
            "en": "chills",
            "ptbr": "calafrios",
        },
        {
            "key": "joint_pain",
            "en": "joint_pain",
            "ptbr": "dor_nas_articulações",
        },
        {
            "key": "stomach_pain",
            "en": "stomach_pain",
            "ptbr": "dor_no_estômago",
        },
        {
            "key": "acidity",
            "en": "acidity",
            "ptbr": "acidez",
        },
        {
            "key": "ulcers_on_tongue",
            "en": "ulcers_on_tongue",
            "ptbr": "úlceras_na_língua",
        },
        {
            "key": "muscle_wasting",
            "en": "muscle_wasting",
            "ptbr": "desgaste_muscular",
        },
        {
            "key": "vomiting",
            "en": "vomiting",
            "ptbr": "vômito",
        },
        {
            "key": "burning_micturition",
            "en": "burning_micturition",
            "ptbr": "ardência_ao_urinar",
        },
        {
            "key": "spotting_urination",
            "en": "spotting_urination",
            "ptbr": "manchas_ao_urinar",
        },
        {
            "key": "fatigue",
            "en": "fatigue",
            "ptbr": "fadiga",
        },
        {
            "key": "weight_gain",
            "en": "weight_gain",
            "ptbr": "ganho_de_peso",
        },
        {
            "key": "anxiety",
            "en": "anxiety",
            "ptbr": "ansiedade",
        },
        {
            "key": "cold_hands_and_feets",
            "en": "cold_hands_and_feets",
            "ptbr": "mãos_e_pés_frios",
        },
        {
            "key": "mood_swings",
            "en": "mood_swings",
            "ptbr": "mudanças_de_humor",
        },
        {
            "key": "weight_loss",
            "en": "weight_loss",
            "ptbr": "perda_de_peso",
        },
        {
            "key": "restlessness",
            "en": "restlessness",
            "ptbr": "inquietação",
        },
        {
            "key": "lethargy",
            "en": "lethargy",
            "ptbr": "letargia",
        },
        {
            "key": "patches_in_throat",
            "en": "patches_in_throat",
            "ptbr": "placas_na_garganta",
        },
        {
            "key": "irregular_sugar_level",
            "en": "irregular_sugar_level",
            "ptbr": "nível_irregular_de_açúcar",
        },
        {
            "key": "cough",
            "en": "cough",
            "ptbr": "tosse",
        },
        {
            "key": "high_fever",
            "en": "high_fever",
            "ptbr": "febre_alta",
        },
        {
            "key": "sunken_eyes",
            "en": "sunken_eyes",
            "ptbr": "olhos_encovados",
        },
        {
            "key": "breathlessness",
            "en": "breathlessness",
            "ptbr": "falta_de_ar",
        },
        {
            "key": "sweating",
            "en": "sweating",
            "ptbr": "sudorese",
        },
        {
            "key": "dehydration",
            "en": "dehydration",
            "ptbr": "desidratação",
        },
        {
            "key": "indigestion",
            "en": "indigestion",
            "ptbr": "indigestão",
        },
        {
            "key": "headache",
            "en": "headache",
            "ptbr": "dor_de_cabeça",
        },
        {
            "key": "yellowish_skin",
            "en": "yellowish_skin",
            "ptbr": "pele_amarelada",
        },
        {
            "key": "dark_urine",
            "en": "dark_urine",
            "ptbr": "urina_escura",
        },
        {
            "key": "nausea",
            "en": "nausea",
            "ptbr": "náusea",
        },
        {
            "key": "loss_of_appetite",
            "en": "loss_of_appetite",
            "ptbr": "perda_de_apetite",
        },
        {
            "key": "pain_behind_the_eyes",
            "en": "pain_behind_the_eyes",
            "ptbr": "dor_atrás_dos_olhos",
        },
        {
            "key": "back_pain",
            "en": "back_pain",
            "ptbr": "dor_nas_costas",
        },
        {
            "key": "constipation",
            "en": "constipation",
            "ptbr": "constipação",
        },
        {
            "key": "abdominal_pain",
            "en": "abdominal_pain",
            "ptbr": "dor_abdominal",
        },
        {
            "key": "diarrhoea",
            "en": "diarrhoea",
            "ptbr": "diarreia",
        },
        {
            "key": "mild_fever",
            "en": "mild_fever",
            "ptbr": "febre_leve",
        },
        {
            "key": "yellow_urine",
            "en": "yellow_urine",
            "ptbr": "urina_amarela",
        },
        {
            "key": "yellowing_of_eyes",
            "en": "yellowing_of_eyes",
            "ptbr": "amarelamento_dos_olhos",
        },
        {
            "key": "acute_liver_failure",
            "en": "acute_liver_failure",
            "ptbr": "falência_hepática_aguda",
        },
        {
            "key": "fluid_overload",
            "en": "fluid_overload",
            "ptbr": "sobrecarga_de_fluidos",
        },
        {
            "key": "swelling_of_stomach",
            "en": "swelling_of_stomach",
            "ptbr": "inchaço_do_estômago",
        },
        {
            "key": "swelled_lymph_nodes",
            "en": "swelled_lymph_nodes",
            "ptbr": "linfonodos_inchados",
        },
        {
            "key": "malaise",
            "en": "malaise",
            "ptbr": "mal-estar",
        },
        {
            "key": "blurred_and_distorted_vision",
            "en": "blurred_and_distorted_vision",
            "ptbr": "visão_embaçada_e_distorcida",
        },
        {
            "key": "phlegm",
            "en": "phlegm",
            "ptbr": "catarro",
        },
        {
            "key": "throat_irritation",
            "en": "throat_irritation",
            "ptbr": "irritação_na_garganta",
        },
        {
            "key": "redness_of_eyes",
            "en": "redness_of_eyes",
            "ptbr": "vermelhidão_nos_olhos",
        },
        {
            "key": "sinus_pressure",
            "en": "sinus_pressure",
            "ptbr": "pressão_sinusal",
        },
        {
            "key": "runny_nose",
            "en": "runny_nose",
            "ptbr": "coriza",
        },
        {
            "key": "congestion",
            "en": "congestion",
            "ptbr": "congestão",
        },
        {
            "key": "chest_pain",
            "en": "chest_pain",
            "ptbr": "dor_no_peito",
        },
        {
            "key": "weakness_in_limbs",
            "en": "weakness_in_limbs",
            "ptbr": "fraqueza_nos_membros",
        },
        {
            "key": "fast_heart_rate",
            "en": "fast_heart_rate",
            "ptbr": "batimento_cardíaco_rápido",
        },
        {
            "key": "pain_during_bowel_movements",
            "en": "pain_during_bowel_movements",
            "ptbr": "dor_durante_a_evacuação",
        },
        {
            "key": "pain_in_anal_region",
            "en": "pain_in_anal_region",
            "ptbr": "dor_na_região_anal",
        },
        {
            "key": "bloody_stool",
            "en": "bloody_stool",
            "ptbr": "fezes_com_sangue",
        },
        {
            "key": "irritation_in_anus",
            "en": "irritation_in_anus",
            "ptbr": "irritação_no_ânus",
        },
        {
            "key": "neck_pain",
            "en": "neck_pain",
            "ptbr": "dor_no_pescoço",
        },
        {
            "key": "dizziness",
            "en": "dizziness",
            "ptbr": "tontura",
        },
        {
            "key": "cramps",
            "en": "cramps",
            "ptbr": "cãibras",
        },
        {
            "key": "bruising",
            "en": "bruising",
            "ptbr": "hematomas",
        },
        {
            "key": "obesity",
            "en": "obesity",
            "ptbr": "obesidade",
        },
        {
            "key": "swollen_legs",
            "en": "swollen_legs",
            "ptbr": "pernas_inchadas",
        },
        {
            "key": "swollen_blood_vessels",
            "en": "swollen_blood_vessels",
            "ptbr": "vasos_sanguíneos_inchados",
        },
        {
            "key": "puffy_face_and_eyes",
            "en": "puffy_face_and_eyes",
            "ptbr": "rosto_e_olhos_inchados",
        },
        {
            "key": "enlarged_thyroid",
            "en": "enlarged_thyroid",
            "ptbr": "tireoide_aumentada",
        },
        {
            "key": "brittle_nails",
            "en": "brittle_nails",
            "ptbr": "unhas_quebradiças",
        },
        {
            "key": "swollen_extremeties",
            "en": "swollen_extremeties",
            "ptbr": "extremidades_inchadas",
        },
        {
            "key": "excessive_hunger",
            "en": "excessive_hunger",
            "ptbr": "fome_excessiva",
        },
        {
            "key": "extra_marital_contacts",
            "en": "extra_marital_contacts",
            "ptbr": "contatos_extraconjugais",
        },
        {
            "key": "drying_and_tingling_lips",
            "en": "drying_and_tingling_lips",
            "ptbr": "lábios_secos_e_formigando",
        },
        {
            "key": "slurred_speech",
            "en": "slurred_speech",
            "ptbr": "fala_arrastada",
        },
        {
            "key": "hip_joint_pain",
            "en": "hip_joint_pain",
            "ptbr": "dor_na_articulação_do_quadril",
        },
        {
            "key": "muscle_weakness",
            "en": "muscle_weakness",
            "ptbr": "fraqueza_muscular",
        },
        {
            "key": "stiff_neck",
            "en": "stiff_neck",
            "ptbr": "rigidez_no_pescoço",
        },
        {
            "key": "swelling_joints",
            "en": "swelling_joints",
            "ptbr": "inchaço_nas_articulações",
        },
        {
            "key": "movement_stiffness",
            "en": "movement_stiffness",
            "ptbr": "rigidez_de_movimentos",
        },
        {
            "key": "spinning_movements",
            "en": "spinning_movements",
            "ptbr": "movimentos_giratórios",
        },
        {
            "key": "loss_of_balance",
            "en": "loss_of_balance",
            "ptbr": "perda_de_equilíbrio",
        },
        {
            "key": "unsteadiness",
            "en": "unsteadiness",
            "ptbr": "falta_de_estabilidade",
        },
        {
            "key": "weakness_of_one_body_side",
            "en": "weakness_of_one_body_side",
            "ptbr": "fraqueza_de_um_lado_do_corpo",
        },
        {
            "key": "loss_of_smell",
            "en": "loss_of_smell",
            "ptbr": "perda_de_olfato",
        },
        {
            "key": "bladder_discomfort",
            "en": "bladder_discomfort",
            "ptbr": "desconforto_na_bexiga",
        },
        {
            "key": "foul_smell_of_urine",
            "en": "foul_smell_of_urine",
            "ptbr": "odor_forte_da_urina",
        },
        {
            "key": "continuous_feel_of_urine",
            "en": "continuous_feel_of_urine",
            "ptbr": "sensação_contínua_de_urina",
        },
        {
            "key": "passage_of_gases",
            "en": "passage_of_gases",
            "ptbr": "passagem_de_gases",
        },
        {
            "key": "internal_itching",
            "en": "internal_itching",
            "ptbr": "coceira_interna",
        },
        {
            "key": "toxic_look_(typhos)",
            "en": "toxic_look_(typhos)",
            "ptbr": "aparência_tóxica_(tifo)",
        },
        {
            "key": "depression",
            "en": "depression",
            "ptbr": "depressão",
        },
        {
            "key": "irritability",
            "en": "irritability",
            "ptbr": "depressão",
        },
        {
            "key": "muscle_pain",
            "en": "muscle_pain",
            "ptbr": "dor_muscular",
        },
        {
            "key": "altered_sensorium",
            "en": "altered_sensorium",
            "ptbr": "sensorium_alterado",
        },
        {
            "key": "red_spots_over_body",
            "en": "red_spots_over_body",
            "ptbr": "manchas_vermelhas_no_corpo",
        },
        {
            "key": "belly_pain",
            "en": "belly_pain",
            "ptbr": "dor_na_barriga",
        },
        {
            "key": "abnormal_menstruation",
            "en": "abnormal_menstruation",
            "ptbr": "menstruação_anormal",
        },
        {
            "key": "dischromic_patches",
            "en": "dischromic_patches",
            "ptbr": "manchas_discromáticas",
        },
        {
            "key": "watering_from_eyes",
            "en": "watering_from_eyes",
            "ptbr": "lacrimejamento_dos_olhos",
        },
        {
            "key": "increased_appetite",
            "en": "increased_appetite",
            "ptbr": "aumento_do_apetite",
        },
        {
            "key": "polyuria",
            "en": "polyuria",
            "ptbr": "poliúria",
        },
        {
            "key": "family_history",
            "en": "family_history",
            "ptbr": "histórico_familiar",
        },
        {
            "key": "mucoid_sputum",
            "en": "mucoid_sputum",
            "ptbr": "escarro_mucóide",
        },
        {
            "key": "rusty_sputum",
            "en": "rusty_sputum",
            "ptbr": "escarro_enferrujado",
        },
        {
            "key": "lack_of_concentration",
            "en": "lack_of_concentration",
            "ptbr": "falta_de_concentração",
        },
        {
            "key": "visual_disturbances",
            "en": "visual_disturbances",
            "ptbr": "distúrbios_visuais",
        },
        {
            "key": "receiving_blood_transfusion",
            "en": "receiving_blood_transfusion",
            "ptbr": "recebendo_transfusão_de_sangue",
        },
        {
            "key": "receiving_unsterile_injections",
            "en": "receiving_unsterile_injections",
            "ptbr": "recebendo_injeções_não_esterilizadas",
        },
        {
            "key": "coma",
            "en": "coma",
            "ptbr": "coma",
        },
        {
            "key": "stomach_bleeding",
            "en": "stomach_bleeding",
            "ptbr": "sangramento_estomacal",
        },
        {
            "key": "distention_of_abdomen",
            "en": "distention_of_abdomen",
            "ptbr": "distensão_abdominal",
        },
        {
            "key": "history_of_alcohol_consumption",
            "en": "history_of_alcohol_consumption",
            "ptbr": "histórico_de_consumo_de_álcool",
        },
        {
            "key": "fluid_overload",
            "en": "fluid_overload",
            "ptbr": "sobrecarga_de_fluidos",
        },
        {
            "key": "blood_in_sputum",
            "en": "blood_in_sputum",
            "ptbr": "sangue_no_escarro",
        },
        {
            "key": "prominent_veins_on_calf",
            "en": "prominent_veins_on_calf",
            "ptbr": "veias_proeminentes_na_panturrilha",
        },
        {
            "key": "palpitations",
            "en": "palpitations",
            "ptbr": "palpitações",
        },
        {
            "key": "painful_walking",
            "en": "painful_walking",
            "ptbr": "dor_ao_caminhar",
        },
        {
            "key": "pus_filled_pimples",
            "en": "pus_filled_pimples",
            "ptbr": "espinhas_com_pus",
        },
        {
            "key": "blackheads",
            "en": "blackheads",
            "ptbr": "cravos",
        },
        {
            "key": "scurring",
            "en": "scurring",
            "ptbr": "cicatrizes",
        },
        {
            "key": "skin_peeling",
            "en": "skin_peeling",
            "ptbr": "descamação_da_pele",
        },
        {
            "key": "silver_like_dusting",
            "en": "silver_like_dusting",
            "ptbr": "Argiria",
        },
        {
            "key": "small_dents_in_nails",
            "en": "small_dents_in_nails",
            "ptbr": "pequenas_depressões_nas_unhas",
        },
        {
            "key": "inflammatory_nails",
            "en": "inflammatory_nails",
            "ptbr": "unhas_inflamadas",
        },
        {
            "key": "blister",
            "en": "blister",
            "ptbr": "bolha",
        },
        {
            "key": "red_sore_around_nose",
            "en": "red_sore_around_nose",
            "ptbr": "ferida_vermelha_ao_redor_do_nariz",
        },
        {
            "key": "yellow_crust_ooze",
            "en": "yellow_crust_ooze",
            "ptbr": "crosta_amarela_exsudativa",
        }
    ];

'''
def getPrognosis():
    return [
        {
            "key": "Fungal infection",
            "en": "Fungal infection",
            "ptbr": "Infecção fúngica",
        },
        {
            "key": "Allergy",
            "en": "Allergy",
            "ptbr": "Alergia"
        },
        {
            "key": "GERD",
            "en": "GERD",
            "ptbr": "DRGE"
        },
        {
            "key": "Chronic cholestasis",
            "en": "Chronic cholestasis",
            "ptbr": "Colestase crônica"
        },
        {
            "key": "Drug Reaction",
            "en": "Drug Reaction",
            "ptbr": "Reação a medicamentos"
        },
        {
            "key": "Peptic ulcer disease",
            "en": "Peptic ulcer disease",
            "ptbr": "Úlcera péptica"
        },
        {
            "key": "AIDS",
            "en": "AIDS",
            "ptbr": "AIDS"
        },
        {
            "key": "Diabetes",
            "en": "Diabetes",
            "ptbr": "Diabetes"
        },
        {
            "key": "Gastroenteritis",
            "en": "Gastroenteritis",
            "ptbr": "Gastroenterite"
        },
        {
            "key": "Bronchial Asthma",
            "en": "Bronchial Asthma",
            "ptbr": "Asma brônquica"
        },
        {
            "key": "Hypertension",
            "en": "Hypertension",
            "ptbr": "Hipertensão"
        },
        {
            "key": "Migraine",
            "en": "Migraine",
            "ptbr": "Enxaqueca"
        },
        {
            "key": "Cervical spondylosis",
            "en": "Cervical spondylosis",
            "ptbr": "Espondilose cervical"
        },
        {
            "key": "Paralysis (brain hemorrhage)",
            "en": "Paralysis (brain hemorrhage)",
            "ptbr": "Paralisia (hemorragia cerebral)"
        },
        {
            "key": "Jaundice",
            "en": "Jaundice",
            "ptbr": "Icterícia"
        },
        {
            "key": "Malaria",
            "en": "Malaria",
            "ptbr": "Malária"
        },
        {
            "key": "Chicken pox",
            "en": "Chicken pox",
            "ptbr": "Catapora"
        },
        {
            "key": "Dengue",
            "en": "Dengue",
            "ptbr": "Dengue"
        },
        {
            "key": "Typhoid",
            "en": "Typhoid",
            "ptbr": "Tifoide"
        },
        {
            "key": "hepatitis A",
            "en": "Hepatitis A",
            "ptbr": "Hepatite A"
        },
        {
            "key": "Hepatitis B",
            "en": "Hepatitis B",
            "ptbr": "Hepatite B"
        },
        {
            "key": "Hepatitis C",
            "en": "Hepatitis C",
            "ptbr": "Hepatite C"
        },
        {
            "key": "Hepatitis D",
            "en": "Hepatitis D",
            "ptbr": "Hepatite D"
        },
        {
            "key": "Hepatitis E",
            "en": "Hepatitis E",
            "ptbr": "Hepatite E"
        },
        {
            "key": "Alcoholic hepatitis",
            "en": "Alcoholic hepatitis",
            "ptbr": "Hepatite alcoólica"
        },
        {
            "key": "Tuberculosis",
            "en": "Tuberculosis",
            "ptbr": "Tuberculose"
        },
        {
            "key": "Common Cold",
            "en": "Common Cold",
            "ptbr": "Resfriado comum"
        },
        {
            "key": "Pneumonia",
            "en": "Pneumonia",
            "ptbr": "Pneumonia"
        },
        {
            "key": "Dimorphic hemmorhoids(piles)",
            "en": "Dimorphic hemmorhoids(piles)",
            "ptbr": "Hemorróidas dimórficas (hemorróidas)"
        },
        {
            "key": "Heart attack",
            "en": "Heart attack",
            "ptbr": "Ataque cardíaco"
        },
        {
            "key": "Varicose veins",
            "en": "Varicose veins",
            "ptbr": "Varizes"
        },
        {
            "key": "Hypothyroidism",
            "en": "Hypothyroidism",
            "ptbr": "Hipotireoidismo"
        },
        {
            "key": "Hyperthyroidism",
            "en": "Hyperthyroidism",
            "ptbr": "Hipertireoidismo"
        },
        {
            "key": "Hypoglycemia",
            "en": "Hypoglycemia",
            "ptbr": "Hipoglicemia"
        },
        {
            "key": "Osteoarthristis",
            "en": "Osteoarthristis",
            "ptbr": "Osteoartrite"
        },
        {
            "key": "Arthritis",
            "en": "Arthritis",
            "ptbr": "Artrite"
        },
        {
            "key": "(vertigo) Paroxysmal Positional Vertigo",
            "en": "(vertigo) Paroxysmal Positional Vertigo",
            "ptbr": "(vertigem) Vertigem Posicional Paroxística"
        },
        {
            "key": "Acne",
            "en": "Acne",
            "ptbr": "Acne"
        },
        {
            "key": "Urinary tract infection",
            "en": "Urinary tract infection",
            "ptbr": "Infecção do trato urinário"
        },
        {
            "key": "Psoriasis",
            "en": "Psoriasis",
            "ptbr": "Psoríase"
        },
        {
            "key": "Impetigo",
            "en": "Impetigo",
            "ptbr": "Impetigo"
        }
    ];
'''

def getDatasetColumns():
    return [
        "itching",
        "skin_rash",
        "nodal_skin_eruptions",
        "continuous_sneezing",
        "shivering",
        "chills",
        "joint_pain",
        "stomach_pain",
        "acidity",
        "ulcers_on_tongue",
        "muscle_wasting",
        "vomiting",
        "burning_micturition",
        "spotting_urination",
        "fatigue",
        "weight_gain",
        "anxiety",
        "cold_hands_and_feets",
        "mood_swings",
        "weight_loss",
        "restlessness",
        "lethargy",
        "patches_in_throat",
        "irregular_sugar_level",
        "cough",
        "high_fever",
        "sunken_eyes",
        "breathlessness",
        "sweating",
        "dehydration",
        "indigestion",
        "headache",
        "yellowish_skin",
        "dark_urine",
        "nausea",
        "loss_of_appetite",
        "pain_behind_the_eyes",
        "back_pain",
        "constipation",
        "abdominal_pain",
        "diarrhoea",
        "mild_fever",
        "yellow_urine",
        "yellowing_of_eyes",
        "acute_liver_failure",
        "fluid_overload",
        "swelling_of_stomach",
        "swelled_lymph_nodes",
        "malaise",
        "blurred_and_distorted_vision",
        "phlegm",
        "throat_irritation",
        "redness_of_eyes",
        "sinus_pressure",
        "runny_nose",
        "congestion",
        "chest_pain",
        "weakness_in_limbs",
        "fast_heart_rate",
        "pain_during_bowel_movements",
        "pain_in_anal_region",
        "bloody_stool",
        "irritation_in_anus",
        "neck_pain",
        "dizziness",
        "cramps",
        "bruising",
        "obesity",
        "swollen_legs",
        "swollen_blood_vessels",
        "puffy_face_and_eyes",
        "enlarged_thyroid",
        "brittle_nails",
        "swollen_extremeties",
        "excessive_hunger",
        "extra_marital_contacts",
        "drying_and_tingling_lips",
        "slurred_speech",
        "hip_joint_pain",
        "muscle_weakness",
        "stiff_neck",
        "swelling_joints",
        "movement_stiffness",
        "spinning_movements",
        "loss_of_balance",
        "unsteadiness",
        "weakness_of_one_body_side",
        "loss_of_smell",
        "bladder_discomfort",
        "foul_smell_of_urine",
        "continuous_feel_of_urine",
        "passage_of_gases",
        "internal_itching",
        "toxic_look_(typhos)",
        "depression",
        "irritability",
        "muscle_pain",
        "altered_sensorium",
        "red_spots_over_body",
        "belly_pain",
        "abnormal_menstruation",
        "dischromic_patches",
        "watering_from_eyes",
        "increased_appetite",
        "polyuria",
        "family_history",
        "mucoid_sputum",
        "rusty_sputum",
        "lack_of_concentration",
        "visual_disturbances",
        "receiving_blood_transfusion",
        "receiving_unsterile_injections",
        "coma",
        "stomach_bleeding",
        "distention_of_abdomen",
        "history_of_alcohol_consumption",
        "fluid_overload",
        "blood_in_sputum",
        "prominent_veins_on_calf",
        "palpitations",
        "painful_walking",
        "pus_filled_pimples",
        "blackheads",
        "scurring",
        "skin_peeling",
        "silver_like_dusting",
        "small_dents_in_nails",
        "inflammatory_nails",
        "blister",
        "red_sore_around_nose",
        "yellow_crust_ooze",
        "prognosis",
    ];