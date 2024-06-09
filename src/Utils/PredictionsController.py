import numpy as np

from src.Predictions.DecisionTreeModel import useDecisionTree
from src.Predictions.RandomForestModel import useRandomForest
from src.Predictions.KNeighborsModel import useKNeighbors
from src.Predictions.SVCModel import useSVC

def predict(symptomsData):
    formattedSymptoms = [];
    options = getDatasetColumns();
    
    for i in range(0, len(options)):
        formattedSymptoms.append(0);

    for i in range(0, len(symptomsData)):
        index = options.index(symptomsData[i]);
        formattedSymptoms[index] = 1;
    
    formattedSymptoms = np.array(formattedSymptoms).reshape(1, -1);

    dtResult = useDecisionTree(formattedSymptoms);
    rfResult = useRandomForest(formattedSymptoms);
    knResult = useKNeighbors(formattedSymptoms);
    svcResult = useSVC(formattedSymptoms);

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

def getSymptoms():
    return [
        {
            "key": "itching",
            "en": "Itching",
            "ptbr": "Coceira",
        },
        {
            "key": "skin_rash",
            "en": "Skin rash",
            "ptbr": "Erupções cutâneas",
        },
        {
            "key": "nodal_skin_eruptions",
            "en": "Nodal skin eruptions",
            "ptbr": "Erupções nodulares na pele",
        },
        {
            "key": "continuous_sneezing",
            "en": "Continuous sneezing",
            "ptbr": "Espirros contínuos",
        },
        {
            "key": "shivering",
            "en": "Shivering",
            "ptbr": "Tremores",
        },
        {
            "key": "chills",
            "en": "Chills",
            "ptbr": "Calafrios",
        },
        {
            "key": "joint_pain",
            "en": "Joint pain",
            "ptbr": "Dor nas articulações",
        },
        {
            "key": "stomach_pain",
            "en": "Stomach pain",
            "ptbr": "Dor no estômago",
        },
        {
            "key": "acidity",
            "en": "Acidity",
            "ptbr": "Acidez",
        },
        {
            "key": "ulcers_on_tongue",
            "en": "Ulcers on tongue",
            "ptbr": "Úlceras na língua",
        },
        {
            "key": "muscle_wasting",
            "en": "Muscle wasting",
            "ptbr": "Desgaste muscular",
        },
        {
            "key": "vomiting",
            "en": "Vomiting",
            "ptbr": "Vômito",
        },
        {
            "key": "burning_micturition",
            "en": "Burning micturition",
            "ptbr": "Ardência ao urinar",
        },
        {
            "key": "spotting_urination",
            "en": "Spotting urination",
            "ptbr": "Manchas ao urinar",
        },
        {
            "key": "fatigue",
            "en": "Fatigue",
            "ptbr": "Fadiga",
        },
        {
            "key": "weight_gain",
            "en": "Weight gain",
            "ptbr": "Ganho de peso",
        },
        {
            "key": "anxiety",
            "en": "Anxiety",
            "ptbr": "Ansiedade",
        },
        {
            "key": "cold_hands_and_feets",
            "en": "Cold hands and feets",
            "ptbr": "Mãos e pés frios",
        },
        {
            "key": "mood_swings",
            "en": "Mood swings",
            "ptbr": "Mudanças de humor",
        },
        {
            "key": "weight_loss",
            "en": "Weight loss",
            "ptbr": "Perda de peso",
        },
        {
            "key": "restlessness",
            "en": "Restlessness",
            "ptbr": "Inquietação",
        },
        {
            "key": "lethargy",
            "en": "Lethargy",
            "ptbr": "Letargia",
        },
        {
            "key": "patches_in_throat",
            "en": "Patches in throat",
            "ptbr": "Placas na garganta",
        },
        {
            "key": "irregular_sugar_level",
            "en": "Irregular sugar level",
            "ptbr": "Nível irregular de açúcar",
        },
        {
            "key": "cough",
            "en": "Cough",
            "ptbr": "Tosse",
        },
        {
            "key": "high_fever",
            "en": "High fever",
            "ptbr": "Febre alta",
        },
        {
            "key": "sunken_eyes",
            "en": "Sunken eyes",
            "ptbr": "Olhos encovados",
        },
        {
            "key": "breathlessness",
            "en": "Breathlessness",
            "ptbr": "Falta de ar",
        },
        {
            "key": "sweating",
            "en": "Sweating",
            "ptbr": "Sudorese",
        },
        {
            "key": "dehydration",
            "en": "Dehydration",
            "ptbr": "Desidratação",
        },
        {
            "key": "indigestion",
            "en": "Indigestion",
            "ptbr": "Indigestão",
        },
        {
            "key": "headache",
            "en": "Headache",
            "ptbr": "Dor de cabeça",
        },
        {
            "key": "yellowish_skin",
            "en": "Yellowish skin",
            "ptbr": "Pele amarelada",
        },
        {
            "key": "dark_urine",
            "en": "Dark urine",
            "ptbr": "Urina escura",
        },
        {
            "key": "nausea",
            "en": "Nausea",
            "ptbr": "Náusea",
        },
        {
            "key": "loss_of_appetite",
            "en": "Loss of appetite",
            "ptbr": "Perda de apetite",
        },
        {
            "key": "pain_behind_the_eyes",
            "en": "Pain behind the eyes",
            "ptbr": "Dor atrás dos olhos",
        },
        {
            "key": "back_pain",
            "en": "Back pain",
            "ptbr": "Dor nas costas",
        },
        {
            "key": "constipation",
            "en": "Constipation",
            "ptbr": "Constipação",
        },
        {
            "key": "abdominal_pain",
            "en": "Abdominal pain",
            "ptbr": "Dor abdominal",
        },
        {
            "key": "diarrhoea",
            "en": "Diarrhoea",
            "ptbr": "Diarreia",
        },
        {
            "key": "mild_fever",
            "en": "Mild fever",
            "ptbr": "Febre leve",
        },
        {
            "key": "yellow_urine",
            "en": "Yellow urine",
            "ptbr": "Urina amarela",
        },
        {
            "key": "yellowing_of_eyes",
            "en": "Yellowing of eyes",
            "ptbr": "Amarelamento dos olhos",
        },
        {
            "key": "acute_liver_failure",
            "en": "Acute liver failure",
            "ptbr": "Falência hepática aguda",
        },
        {
            "key": "fluid_overload",
            "en": "Fluid overload",
            "ptbr": "Sobrecarga de fluidos",
        },
        {
            "key": "swelling_of_stomach",
            "en": "Swelling of stomach",
            "ptbr": "Inchaço do estômago",
        },
        {
            "key": "swelled_lymph_nodes",
            "en": "Swelled lymph nodes",
            "ptbr": "Linfonodos inchados",
        },
        {
            "key": "malaise",
            "en": "Malaise",
            "ptbr": "Mal-estar",
        },
        {
            "key": "blurred_and_distorted_vision",
            "en": "Blurred and distorted vision",
            "ptbr": "Visão embaçada e distorcida",
        },
        {
            "key": "phlegm",
            "en": "Phlegm",
            "ptbr": "Catarro",
        },
        {
            "key": "throat_irritation",
            "en": "Throat irritation",
            "ptbr": "Irritação na garganta",
        },
        {
            "key": "redness_of_eyes",
            "en": "Redness of eyes",
            "ptbr": "Vermelhidão nos olhos",
        },
        {
            "key": "sinus_pressure",
            "en": "Sinus pressure",
            "ptbr": "Pressão sinusal",
        },
        {
            "key": "runny_nose",
            "en": "Runny nose",
            "ptbr": "Coriza",
        },
        {
            "key": "congestion",
            "en": "Congestion",
            "ptbr": "Congestão",
        },
        {
            "key": "chest_pain",
            "en": "Chest pain",
            "ptbr": "Dor no peito",
        },
        {
            "key": "weakness_in_limbs",
            "en": "Weakness in limbs",
            "ptbr": "Fraqueza nos membros",
        },
        {
            "key": "fast_heart_rate",
            "en": "Fast heart rate",
            "ptbr": "Batimento cardíaco rápido",
        },
        {
            "key": "pain_during_bowel_movements",
            "en": "Pain during bowel movements",
            "ptbr": "Dor durante a evacuação",
        },
        {
            "key": "pain_in_anal_region",
            "en": "Pain in anal region",
            "ptbr": "Dor na região anal",
        },
        {
            "key": "bloody_stool",
            "en": "Bloody stool",
            "ptbr": "Fezes com sangue",
        },
        {
            "key": "irritation_in_anus",
            "en": "Irritation in anus",
            "ptbr": "Irritação no ânus",
        },
        {
            "key": "neck_pain",
            "en": "Neck pain",
            "ptbr": "Dor no pescoço",
        },
        {
            "key": "dizziness",
            "en": "Dizziness",
            "ptbr": "Tontura",
        },
        {
            "key": "cramps",
            "en": "Cramps",
            "ptbr": "Cãimbras",
        },
        {
            "key": "bruising",
            "en": "Bruising",
            "ptbr": "Hematomas",
        },
        {
            "key": "obesity",
            "en": "Obesity",
            "ptbr": "Obesidade",
        },
        {
            "key": "swollen_legs",
            "en": "Swollen legs",
            "ptbr": "Pernas inchadas",
        },
        {
            "key": "swollen_blood_vessels",
            "en": "Swollen blood vessels",
            "ptbr": "Vasos sanguíneos inchados",
        },
        {
            "key": "puffy_face_and_eyes",
            "en": "Puffy face and eyes",
            "ptbr": "Rosto e olhos inchados",
        },
        {
            "key": "enlarged_thyroid",
            "en": "Enlarged thyroid",
            "ptbr": "Tireoide aumentada",
        },
        {
            "key": "brittle_nails",
            "en": "Brittle nails",
            "ptbr": "Unhas quebradiças",
        },
        {
            "key": "swollen_extremeties",
            "en": "Swollen extremeties",
            "ptbr": "Extremidades inchadas",
        },
        {
            "key": "excessive_hunger",
            "en": "Excessive hunger",
            "ptbr": "Fome excessiva",
        },
        {
            "key": "extra_marital_contacts",
            "en": "Extra marital contacts",
            "ptbr": "Contatos extraconjugais",
        },
        {
            "key": "drying_and_tingling_lips",
            "en": "Drying and tingling lips",
            "ptbr": "Lábios secos e formigando",
        },
        {
            "key": "slurred_speech",
            "en": "Slurred speech",
            "ptbr": "Fala arrastada",
        },
        {
            "key": "hip_joint_pain",
            "en": "Hip joint pain",
            "ptbr": "Dor na articulação do quadril",
        },
        {
            "key": "muscle_weakness",
            "en": "Muscle weakness",
            "ptbr": "Fraqueza muscular",
        },
        {
            "key": "stiff_neck",
            "en": "Stiff neck",
            "ptbr": "Rigidez no pescoço",
        },
        {
            "key": "swelling_joints",
            "en": "Swelling joints",
            "ptbr": "Inchaço nas articulações",
        },
        {
            "key": "movement_stiffness",
            "en": "Movement stiffness",
            "ptbr": "Rigidez de movimentos",
        },
        {
            "key": "spinning_movements",
            "en": "Spinning movements",
            "ptbr": "Movimentos giratórios",
        },
        {
            "key": "loss_of_balance",
            "en": "Loss of balance",
            "ptbr": "Perda de equilíbrio",
        },
        {
            "key": "unsteadiness",
            "en": "Unsteadiness",
            "ptbr": "Falta de estabilidade",
        },
        {
            "key": "weakness_of_one_body_side",
            "en": "Weakness of one body side",
            "ptbr": "Fraqueza de um lado do corpo",
        },
        {
            "key": "loss_of_smell",
            "en": "Loss of smell",
            "ptbr": "Perda de olfato",
        },
        {
            "key": "bladder_discomfort",
            "en": "Bladder discomfort",
            "ptbr": "Desconforto na bexiga",
        },
        {
            "key": "foul_smell_of_urine",
            "en": "Foul smell of urine",
            "ptbr": "Odor forte da urina",
        },
        {
            "key": "continuous_feel_of_urine",
            "en": "Continuous feel of urine",
            "ptbr": "Sensação contínua de urina",
        },
        {
            "key": "passage_of_gases",
            "en": "Passage of gases",
            "ptbr": "Passagem de gases",
        },
        {
            "key": "internal_itching",
            "en": "Internal itching",
            "ptbr": "Coceira interna",
        },
        {
            "key": "toxic_look_(typhos)",
            "en": "Toxic look (typhos)",
            "ptbr": "Aparência tóxica (tifo)",
        },
        {
            "key": "depression",
            "en": "Depression",
            "ptbr": "Depressão",
        },
        {
            "key": "irritability",
            "en": "Irritability",
            "ptbr": "Irritação",
        },
        {
            "key": "muscle_pain",
            "en": "Muscle pain",
            "ptbr": "Dor muscular",
        },
        {
            "key": "altered_sensorium",
            "en": "Altered sensorium",
            "ptbr": "Sensorium alterado",
        },
        {
            "key": "red_spots_over_body",
            "en": "Red spots over body",
            "ptbr": "Manchas vermelhas no corpo",
        },
        {
            "key": "belly_pain",
            "en": "Belly pain",
            "ptbr": "Dor na barriga",
        },
        {
            "key": "abnormal_menstruation",
            "en": "Abnormal menstruation",
            "ptbr": "Menstruação anormal",
        },
        {
            "key": "dischromic_patches",
            "en": "Dischromic patches",
            "ptbr": "Manchas discromáticas",
        },
        {
            "key": "watering_from_eyes",
            "en": "Watering from eyes",
            "ptbr": "Lacrimejamento dos olhos",
        },
        {
            "key": "increased_appetite",
            "en": "Increased appetite",
            "ptbr": "Aumento do apetite",
        },
        {
            "key": "polyuria",
            "en": "Polyuria",
            "ptbr": "Poliúria",
        },
        {
            "key": "family_history",
            "en": "Family history",
            "ptbr": "Histórico familiar",
        },
        {
            "key": "mucoid_sputum",
            "en": "Mucoid sputum",
            "ptbr": "Escarro mucóide",
        },
        {
            "key": "rusty_sputum",
            "en": "Rusty sputum",
            "ptbr": "Escarro enferrujado",
        },
        {
            "key": "lack_of_concentration",
            "en": "Lack of concentration",
            "ptbr": "Falta de concentração",
        },
        {
            "key": "visual_disturbances",
            "en": "Visual disturbances",
            "ptbr": "Distúrbios visuais",
        },
        {
            "key": "receiving_blood_transfusion",
            "en": "Receiving blood transfusion",
            "ptbr": "Recebendo transfusão de sangue",
        },
        {
            "key": "receiving_unsterile_injections",
            "en": "Receiving unsterile injections",
            "ptbr": "Recebendo injeções não esterilizadas",
        },
        {
            "key": "coma",
            "en": "Coma",
            "ptbr": "Coma",
        },
        {
            "key": "stomach_bleeding",
            "en": "Stomach bleeding",
            "ptbr": "Sangramento estomacal",
        },
        {
            "key": "distention_of_abdomen",
            "en": "Distention of abdomen",
            "ptbr": "Distensão abdominal",
        },
        {
            "key": "history_of_alcohol_consumption",
            "en": "History of alcohol consumption",
            "ptbr": "Histórico de consumo de álcool",
        },
        {
            "key": "fluid_overload",
            "en": "Fluid overload",
            "ptbr": "Sobrecarga de fluidos",
        },
        {
            "key": "blood_in_sputum",
            "en": "Blood in sputum",
            "ptbr": "Sangue no escarro",
        },
        {
            "key": "prominent_veins_on_calf",
            "en": "Prominent veins on calf",
            "ptbr": "Veias proeminentes na panturrilha",
        },
        {
            "key": "palpitations",
            "en": "Palpitations",
            "ptbr": "Palpitações",
        },
        {
            "key": "painful_walking",
            "en": "Painful walking",
            "ptbr": "Dor ao caminhar",
        },
        {
            "key": "pus_filled_pimples",
            "en": "Pus filled pimples",
            "ptbr": "Espinhas com pus",
        },
        {
            "key": "blackheads",
            "en": "Blackheads",
            "ptbr": "Cravos",
        },
        {
            "key": "scurring",
            "en": "Scurring",
            "ptbr": "Cicatrizes",
        },
        {
            "key": "skin_peeling",
            "en": "Skin peeling",
            "ptbr": "Descamação da pele",
        },
        {
            "key": "silver_like_dusting",
            "en": "Silver like dusting",
            "ptbr": "Argiria",
        },
        {
            "key": "small_dents_in_nails",
            "en": "Small dents in nails",
            "ptbr": "Pequenas depressões nas unhas",
        },
        {
            "key": "inflammatory_nails",
            "en": "Inflammatory nails",
            "ptbr": "Unhas inflamadas",
        },
        {
            "key": "blister",
            "en": "Blister",
            "ptbr": "Bolha",
        },
        {
            "key": "red_sore_around_nose",
            "en": "Red sore around nose",
            "ptbr": "Ferida vermelha ao redor do nariz",
        },
        {
            "key": "yellow_crust_ooze",
            "en": "Yellow crust ooze",
            "ptbr": "Crosta amarela exsudativa",
        }
    ];

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