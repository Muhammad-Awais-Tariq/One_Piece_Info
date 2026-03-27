import requests

def get_website(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }    
    response = requests.get(url,headers=headers)
    content = response.json()  
    return content

def one_piece_character_info(name):
    url = "https://api.api-onepiece.com/v2/characters/en"
    raw_characters = get_website(url)

    for character in raw_characters:
        character_name = character.get("name")
        if name.lower().title() in character_name.lower().title() :
                return character
    
def extract_info(character):
     name = character.get("name")
     complete_info = []

     for k , v in character.items():
        if k not in  ["id","name","crew","fruit"]:
            complete_info.append(f"The {k} of {name} is {v}")
        if k == "crew":
            crew = character.get("crew")
            if crew.get("roman_name"):
                crew_name = crew.get("roman_name")
            else:
                crew_name = crew.get("name")
            complete_info.append(f"The {k} of {name} is {crew_name}")
        if k == "fruit":
            fruit = character.get("fruit")
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
    character = one_piece_character_info(name)
    if character:
        return extract_info(character)
    else:
        return "No chracter found enter a valid name"

def print_info():
    info = get_character_info()

    for value in info:
        print(value)

def main():
    print("What information do you want?\n1. Characters\n2. Swords\n3. Fruits\n4. Episodes")
    while True:
        while True:
            try:
                option = int(input("Enter the required option: "))
            except ValueError:
                print("Enter a number")
                continue
            else:
                break
        if option in [1,2,3,4]:
            break
    
    if option == 1:
        print_info()
    
if __name__ == "__main__":
    main()