import subprocess
import json

def categorize_request(prompt, context=
                       """
                        categorize the input into one of the following question_types:
                        1. General Inquiry
                        2. Technical Support
                        3. Sales Inquiry
                       """
                       ):
    full_prompt = f"{context}\n\nUser: {prompt}\nAssistant:"
    result = subprocess.run(
        ["ollama", "run", "jobautomation/openeurollm-dutch", "--format", "json"],
        input=full_prompt.encode(),
        capture_output=True,
    )
    return json.loads(result.stdout.decode())


def tech_support_info_gathering(requester_name= None, project_name= None, email= None):
    context=""" 
            We moeten de naam van de aanvrager, de naam van het project, en het emailadres van de 
            aanvrager achterhalen om de aanvrager verder te helpen.
            Vraag hiernaar bij de klant
                we currently know
                '{
                    "requester_name": "niet bekend",
                    "project_name": "niet bekend",
                    "email": "niet bekend"
                }'
            retourneer een dialoog met natuurlijke tekst waarin je deze informatie vraagt.
            """
    full_prompt = f"{context}\nAssistant:"
    result = subprocess.run(
        ["ollama", "run", "jobautomation/openeurollm-dutch", "--format", "json"],
        input=full_prompt.encode(),
        capture_output=True,
    )
    return json.loads(result.stdout.decode())


def general_inquiry_info_gathering():
    context=""" 
           De aanvrager schijnt een algemene vraag te hebben. We willen doorvragen om kijken naar welke afdeling we de vraag moeten doorsturen.
            Vraag bij de klant of hij iets will kopen of dat hij hulp nodig heeft.
            """
    full_prompt = f"{context}\nAssistant:"
    result = subprocess.run(
        ["ollama", "run", "jobautomation/openeurollm-dutch", "--format", "json"],
        input=full_prompt.encode(),
        capture_output=True,
    )
    return json.loads(result.stdout.decode())