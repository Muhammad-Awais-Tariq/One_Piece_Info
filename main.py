import requests

def get_website(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }    
    response = requests.get(url,headers=headers)
    content = response.json()  
    return content

def one_piece_info(name):
    url = "https://api.api-onepiece.com/v2/characters/en"
    raw_characters = get_website(url)

    for character in raw_characters:
        chracter_name = character.get("name")
        if name.lower().title() in chracter_name.lower().title() :
                return character
    
def print_info(chracter):
     name = chracter["name"]
     complete_info = []

     for k , v in chracter.items():
        if k not in  ["id","name","crew","fruit"]:
            complete_info.append(f"The {k} of {name} is {v}")
        if k == "crew":
            crew = chracter["crew"]
            if crew.get("roman_name"):
                crew_name = crew.get("roman_name")
            else:
                crew_name = crew.get("name")
            complete_info.append(f"The {k} of {name} is {crew_name}")
        if k == "fruit":
            fruit = chracter["fruit"]
            if fruit.get("roman_name"):
                fruit_name = fruit.get("roman_name")
            else:
                fruit_name = fruit.get("name")
            fruit_type = fruit.get("type")
            if fruit.get("filename"):
                fruit_image = fruit.get("filename")
            else:
                fruit_image = "No image found"
            complete_info.append(f"The {k} of {name} is {fruit_name} which is a {fruit_type} fruit \n {fruit_image}")

     return complete_info

def get_character_info():
    name = input("Enter the name of the chracter you want info about: ")
    chracter = one_piece_info(name)
    if chracter:
        return print_info(chracter)
    else:
        return "No chracter found enter a valid name"

def main():
    info = get_character_info()
    if info:
        for value in info:
            print(value)

if __name__ == "__main__":
    main()