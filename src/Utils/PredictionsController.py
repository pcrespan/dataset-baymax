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
            "ptbr": "itching",
        },
        {
            "key": "skin_rash",
            "en": "skin_rash",
            "ptbr": "skin_rash",
        },
        {
            "key": "nodal_skin_eruptions",
            "en": "nodal_skin_eruptions",
            "ptbr": "nodal_skin_eruptions",
        },
        {
            "key": "continuous_sneezing",
            "en": "continuous_sneezing",
            "ptbr": "continuous_sneezing",
        },
        {
            "key": "shivering",
            "en": "shivering",
            "ptbr": "shivering",
        },
        {
            "key": "chills",
            "en": "chills",
            "ptbr": "chills",
        },
        {
            "key": "joint_pain",
            "en": "joint_pain",
            "ptbr": "joint_pain",
        },
        {
            "key": "stomach_pain",
            "en": "stomach_pain",
            "ptbr": "stomach_pain",
        },
        {
            "key": "acidity",
            "en": "acidity",
            "ptbr": "acidity",
        },
        {
            "key": "ulcers_on_tongue",
            "en": "ulcers_on_tongue",
            "ptbr": "ulcers_on_tongue",
        },
        {
            "key": "muscle_wasting",
            "en": "muscle_wasting",
            "ptbr": "muscle_wasting",
        },
        {
            "key": "vomiting",
            "en": "vomiting",
            "ptbr": "vomiting",
        },
        {
            "key": "burning_micturition",
            "en": "burning_micturition",
            "ptbr": "burning_micturition",
        },
        {
            "key": "spotting_urination",
            "en": "spotting_urination",
            "ptbr": "spotting_urination",
        },
        {
            "key": "fatigue",
            "en": "fatigue",
            "ptbr": "fatigue",
        },
        {
            "key": "weight_gain",
            "en": "weight_gain",
            "ptbr": "weight_gain",
        },
        {
            "key": "anxiety",
            "en": "anxiety",
            "ptbr": "anxiety",
        },
        {
            "key": "cold_hands_and_feets",
            "en": "cold_hands_and_feets",
            "ptbr": "cold_hands_and_feets",
        },
        {
            "key": "mood_swings",
            "en": "mood_swings",
            "ptbr": "mood_swings",
        },
        {
            "key": "weight_loss",
            "en": "weight_loss",
            "ptbr": "weight_loss",
        },
        {
            "key": "restlessness",
            "en": "restlessness",
            "ptbr": "restlessness",
        },
        {
            "key": "lethargy",
            "en": "lethargy",
            "ptbr": "lethargy",
        },
        {
            "key": "patches_in_throat",
            "en": "patches_in_throat",
            "ptbr": "patches_in_throat",
        },
        {
            "key": "irregular_sugar_level",
            "en": "irregular_sugar_level",
            "ptbr": "irregular_sugar_level",
        },
        {
            "key": "cough",
            "en": "cough",
            "ptbr": "cough",
        },
        {
            "key": "high_fever",
            "en": "high_fever",
            "ptbr": "high_fever",
        },
        {
            "key": "sunken_eyes",
            "en": "sunken_eyes",
            "ptbr": "sunken_eyes",
        },
        {
            "key": "breathlessness",
            "en": "breathlessness",
            "ptbr": "breathlessness",
        },
        {
            "key": "sweating",
            "en": "sweating",
            "ptbr": "sweating",
        },
        {
            "key": "dehydration",
            "en": "dehydration",
            "ptbr": "dehydration",
        },
        {
            "key": "indigestion",
            "en": "indigestion",
            "ptbr": "indigestion",
        },
        {
            "key": "headache",
            "en": "headache",
            "ptbr": "headache",
        },
        {
            "key": "yellowish_skin",
            "en": "yellowish_skin",
            "ptbr": "yellowish_skin",
        },
        {
            "key": "dark_urine",
            "en": "dark_urine",
            "ptbr": "dark_urine",
        },
        {
            "key": "nausea",
            "en": "nausea",
            "ptbr": "nausea",
        },
        {
            "key": "loss_of_appetite",
            "en": "loss_of_appetite",
            "ptbr": "loss_of_appetite",
        },
        {
            "key": "pain_behind_the_eyes",
            "en": "pain_behind_the_eyes",
            "ptbr": "pain_behind_the_eyes",
        },
        {
            "key": "back_pain",
            "en": "back_pain",
            "ptbr": "back_pain",
        },
        {
            "key": "constipation",
            "en": "constipation",
            "ptbr": "constipation",
        },
        {
            "key": "abdominal_pain",
            "en": "abdominal_pain",
            "ptbr": "abdominal_pain",
        },
        {
            "key": "diarrhoea",
            "en": "diarrhoea",
            "ptbr": "diarrhoea",
        },
        {
            "key": "mild_fever",
            "en": "mild_fever",
            "ptbr": "mild_fever",
        },
        {
            "key": "yellow_urine",
            "en": "yellow_urine",
            "ptbr": "yellow_urine",
        },
        {
            "key": "yellowing_of_eyes",
            "en": "yellowing_of_eyes",
            "ptbr": "yellowing_of_eyes",
        },
        {
            "key": "acute_liver_failure",
            "en": "acute_liver_failure",
            "ptbr": "acute_liver_failure",
        },
        {
            "key": "fluid_overload",
            "en": "fluid_overload",
            "ptbr": "fluid_overload",
        },
        {
            "key": "swelling_of_stomach",
            "en": "swelling_of_stomach",
            "ptbr": "swelling_of_stomach",
        },
        {
            "key": "swelled_lymph_nodes",
            "en": "swelled_lymph_nodes",
            "ptbr": "swelled_lymph_nodes",
        },
        {
            "key": "malaise",
            "en": "malaise",
            "ptbr": "malaise",
        },
        {
            "key": "blurred_and_distorted_vision",
            "en": "blurred_and_distorted_vision",
            "ptbr": "blurred_and_distorted_vision",
        },
        {
            "key": "phlegm",
            "en": "phlegm",
            "ptbr": "phlegm",
        },
        {
            "key": "throat_irritation",
            "en": "throat_irritation",
            "ptbr": "throat_irritation",
        },
        {
            "key": "redness_of_eyes",
            "en": "redness_of_eyes",
            "ptbr": "redness_of_eyes",
        },
        {
            "key": "sinus_pressure",
            "en": "sinus_pressure",
            "ptbr": "sinus_pressure",
        },
        {
            "key": "runny_nose",
            "en": "runny_nose",
            "ptbr": "runny_nose",
        },
        {
            "key": "congestion",
            "en": "congestion",
            "ptbr": "congestion",
        },
        {
            "key": "chest_pain",
            "en": "chest_pain",
            "ptbr": "chest_pain",
        },
        {
            "key": "weakness_in_limbs",
            "en": "weakness_in_limbs",
            "ptbr": "weakness_in_limbs",
        },
        {
            "key": "fast_heart_rate",
            "en": "fast_heart_rate",
            "ptbr": "fast_heart_rate",
        },
        {
            "key": "pain_during_bowel_movements",
            "en": "pain_during_bowel_movements",
            "ptbr": "pain_during_bowel_movements",
        },
        {
            "key": "pain_in_anal_region",
            "en": "pain_in_anal_region",
            "ptbr": "pain_in_anal_region",
        },
        {
            "key": "bloody_stool",
            "en": "bloody_stool",
            "ptbr": "bloody_stool",
        },
        {
            "key": "irritation_in_anus",
            "en": "irritation_in_anus",
            "ptbr": "irritation_in_anus",
        },
        {
            "key": "neck_pain",
            "en": "neck_pain",
            "ptbr": "neck_pain",
        },
        {
            "key": "dizziness",
            "en": "dizziness",
            "ptbr": "dizziness",
        },
        {
            "key": "cramps",
            "en": "cramps",
            "ptbr": "cramps",
        },
        {
            "key": "bruising",
            "en": "bruising",
            "ptbr": "bruising",
        },
        {
            "key": "obesity",
            "en": "obesity",
            "ptbr": "obesity",
        },
        {
            "key": "swollen_legs",
            "en": "swollen_legs",
            "ptbr": "swollen_legs",
        },
        {
            "key": "swollen_blood_vessels",
            "en": "swollen_blood_vessels",
            "ptbr": "swollen_blood_vessels",
        },
        {
            "key": "puffy_face_and_eyes",
            "en": "puffy_face_and_eyes",
            "ptbr": "puffy_face_and_eyes",
        },
        {
            "key": "enlarged_thyroid",
            "en": "enlarged_thyroid",
            "ptbr": "enlarged_thyroid",
        },
        {
            "key": "brittle_nails",
            "en": "brittle_nails",
            "ptbr": "brittle_nails",
        },
        {
            "key": "swollen_extremeties",
            "en": "swollen_extremeties",
            "ptbr": "swollen_extremeties",
        },
        {
            "key": "excessive_hunger",
            "en": "excessive_hunger",
            "ptbr": "excessive_hunger",
        },
        {
            "key": "extra_marital_contacts",
            "en": "extra_marital_contacts",
            "ptbr": "extra_marital_contacts",
        },
        {
            "key": "drying_and_tingling_lips",
            "en": "drying_and_tingling_lips",
            "ptbr": "drying_and_tingling_lips",
        },
        {
            "key": "slurred_speech",
            "en": "slurred_speech",
            "ptbr": "slurred_speech",
        },
        {
            "key": "hip_joint_pain",
            "en": "hip_joint_pain",
            "ptbr": "hip_joint_pain",
        },
        {
            "key": "muscle_weakness",
            "en": "muscle_weakness",
            "ptbr": "muscle_weakness",
        },
        {
            "key": "stiff_neck",
            "en": "stiff_neck",
            "ptbr": "stiff_neck",
        },
        {
            "key": "swelling_joints",
            "en": "swelling_joints",
            "ptbr": "swelling_joints",
        },
        {
            "key": "movement_stiffness",
            "en": "movement_stiffness",
            "ptbr": "movement_stiffness",
        },
        {
            "key": "spinning_movements",
            "en": "spinning_movements",
            "ptbr": "spinning_movements",
        },
        {
            "key": "loss_of_balance",
            "en": "loss_of_balance",
            "ptbr": "loss_of_balance",
        },
        {
            "key": "unsteadiness",
            "en": "unsteadiness",
            "ptbr": "unsteadiness",
        },
        {
            "key": "weakness_of_one_body_side",
            "en": "weakness_of_one_body_side",
            "ptbr": "weakness_of_one_body_side",
        },
        {
            "key": "loss_of_smell",
            "en": "loss_of_smell",
            "ptbr": "loss_of_smell",
        },
        {
            "key": "bladder_discomfort",
            "en": "bladder_discomfort",
            "ptbr": "bladder_discomfort",
        },
        {
            "key": "foul_smell_of_urine",
            "en": "foul_smell_of_urine",
            "ptbr": "foul_smell_of_urine",
        },
        {
            "key": "continuous_feel_of_urine",
            "en": "continuous_feel_of_urine",
            "ptbr": "continuous_feel_of_urine",
        },
        {
            "key": "passage_of_gases",
            "en": "passage_of_gases",
            "ptbr": "passage_of_gases",
        },
        {
            "key": "internal_itching",
            "en": "internal_itching",
            "ptbr": "internal_itching",
        },
        {
            "key": "toxic_look_(typhos)",
            "en": "toxic_look_(typhos)",
            "ptbr": "toxic_look_(typhos)",
        },
        {
            "key": "depression",
            "en": "depression",
            "ptbr": "depression",
        },
        {
            "key": "irritability",
            "en": "irritability",
            "ptbr": "irritability",
        },
        {
            "key": "muscle_pain",
            "en": "muscle_pain",
            "ptbr": "muscle_pain",
        },
        {
            "key": "altered_sensorium",
            "en": "altered_sensorium",
            "ptbr": "altered_sensorium",
        },
        {
            "key": "red_spots_over_body",
            "en": "red_spots_over_body",
            "ptbr": "red_spots_over_body",
        },
        {
            "key": "belly_pain",
            "en": "belly_pain",
            "ptbr": "belly_pain",
        },
        {
            "key": "abnormal_menstruation",
            "en": "abnormal_menstruation",
            "ptbr": "abnormal_menstruation",
        },
        {
            "key": "dischromic_patches",
            "en": "dischromic_patches",
            "ptbr": "dischromic_patches",
        },
        {
            "key": "watering_from_eyes",
            "en": "watering_from_eyes",
            "ptbr": "watering_from_eyes",
        },
        {
            "key": "increased_appetite",
            "en": "increased_appetite",
            "ptbr": "increased_appetite",
        },
        {
            "key": "polyuria",
            "en": "polyuria",
            "ptbr": "polyuria",
        },
        {
            "key": "family_history",
            "en": "family_history",
            "ptbr": "family_history",
        },
        {
            "key": "mucoid_sputum",
            "en": "mucoid_sputum",
            "ptbr": "mucoid_sputum",
        },
        {
            "key": "rusty_sputum",
            "en": "rusty_sputum",
            "ptbr": "rusty_sputum",
        },
        {
            "key": "lack_of_concentration",
            "en": "lack_of_concentration",
            "ptbr": "lack_of_concentration",
        },
        {
            "key": "visual_disturbances",
            "en": "visual_disturbances",
            "ptbr": "visual_disturbances",
        },
        {
            "key": "receiving_blood_transfusion",
            "en": "receiving_blood_transfusion",
            "ptbr": "receiving_blood_transfusion",
        },
        {
            "key": "receiving_unsterile_injections",
            "en": "receiving_unsterile_injections",
            "ptbr": "receiving_unsterile_injections",
        },
        {
            "key": "coma",
            "en": "coma",
            "ptbr": "coma",
        },
        {
            "key": "stomach_bleeding",
            "en": "stomach_bleeding",
            "ptbr": "stomach_bleeding",
        },
        {
            "key": "distention_of_abdomen",
            "en": "distention_of_abdomen",
            "ptbr": "distention_of_abdomen",
        },
        {
            "key": "history_of_alcohol_consumption",
            "en": "history_of_alcohol_consumption",
            "ptbr": "history_of_alcohol_consumption",
        },
        {
            "key": "fluid_overload",
            "en": "fluid_overload",
            "ptbr": "fluid_overload",
        },
        {
            "key": "blood_in_sputum",
            "en": "blood_in_sputum",
            "ptbr": "blood_in_sputum",
        },
        {
            "key": "prominent_veins_on_calf",
            "en": "prominent_veins_on_calf",
            "ptbr": "prominent_veins_on_calf",
        },
        {
            "key": "palpitations",
            "en": "palpitations",
            "ptbr": "palpitations",
        },
        {
            "key": "painful_walking",
            "en": "painful_walking",
            "ptbr": "painful_walking",
        },
        {
            "key": "pus_filled_pimples",
            "en": "pus_filled_pimples",
            "ptbr": "pus_filled_pimples",
        },
        {
            "key": "blackheads",
            "en": "blackheads",
            "ptbr": "blackheads",
        },
        {
            "key": "scurring",
            "en": "scurring",
            "ptbr": "scurring",
        },
        {
            "key": "skin_peeling",
            "en": "skin_peeling",
            "ptbr": "skin_peeling",
        },
        {
            "key": "silver_like_dusting",
            "en": "silver_like_dusting",
            "ptbr": "silver_like_dusting",
        },
        {
            "key": "small_dents_in_nails",
            "en": "small_dents_in_nails",
            "ptbr": "small_dents_in_nails",
        },
        {
            "key": "inflammatory_nails",
            "en": "inflammatory_nails",
            "ptbr": "inflammatory_nails",
        },
        {
            "key": "blister",
            "en": "blister",
            "ptbr": "blister",
        },
        {
            "key": "red_sore_around_nose",
            "en": "red_sore_around_nose",
            "ptbr": "red_sore_around_nose",
        },
        {
            "key": "yellow_crust_ooze",
            "en": "yellow_crust_ooze",
            "ptbr": "yellow_crust_ooze",
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