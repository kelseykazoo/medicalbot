welcome_prompt  = "Welcome doctor, what do you want to do today?\n -To list all patients, press 1\n - To run a new diagnosis, press 2\n - To quit, press q\n"
name_prompt = "What is the patient's name?\n"
appearance_prompt = "How is patient's general appearance?\n - 1: Normal appearance\n - 2: Irritable or lethargic\n"
eye_prompt = "How are the patient's eyes\n - 1: Normal/Slightly sunken\n - 2: Very sunken\n"
skin_prompt = "How is the patient's skin when you pinch it?\n - 1: Normal skin pinch\n - 2: Slow skin pinch\n "
severe_dehydration = "Severe dehydration"
some_dehydration = "Some dehydration"
no_dehydration = "No dehydration"

patients_and_diagnoses = [
    "Harry: No dehydration",
    "Ron: Some dehydration",
    "Hermione: Some dehydration",
    "Draco: Severe dehydration"
]

def list_patients():
    for patient in patients_and_diagnoses:
        print(patient)
    
    
def assess_skin(skin):
    if skin == "1":
        return some_dehydration
    elif skin == "2":
        return severe_dehydration
    
    
def asses_eyes(eyes):
    if eyes == "1":
        return no_dehydration
    elif eyes == "2":
        return severe_dehydration
        
    
      
def asses_appearance():
    appearance = input(appearance_prompt)
    if appearance == "1":
        eyes = input(eye_prompt)
        return asses_eyes(eyes)
    elif appearance == "2":
        skin = input(skin_prompt)
        return assess_skin(skin)
    
    
    
def start_new_diagnosis():
    name = input(name_prompt)
    diagnosis = asses_appearance()
    print(name, diagnosis)
    


def main():
    while(True):
        selection = input(welcome_prompt)
        if selection == "1":
            list_patients()
        elif selection == "2":
            start_new_diagnosis()
        elif selection == "q":
            return
    
    
main()
    
