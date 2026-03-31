import requests

def get_website(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }    
    response = requests.get(url,headers=headers)
    content = response.json()  
    return content

def one_piece_info(name , entity_type , is_episode = False):
    url = f"https://api.api-onepiece.com/v2/{entity_type}/en"
    raw_info = get_website(url)
    if is_episode:
        for info in raw_info:
            entity_number = info.get("id")
            if int(name) == entity_number :
                    return entity_type ,info    
    if not is_episode:    
        for info in raw_info:
            entity_name = info.get("name")
            if name.lower().title() in entity_name.lower().title() :
                    return entity_type ,info
   
    
def extract_info(entity_type , info):
    name = info.get("name")
    complete_info = []
    for k , v in info.items():
        if entity_type == "characters":     
           if k not in  ["id","name","crew","fruit"]:
               complete_info.append(f"The {k} of {name} is {v}")
           if k == "crew":
               crew = info.get("crew")
               if crew.get("roman_name"):
                   crew_name = crew.get("roman_name")
               else:
                   crew_name = crew.get("name")
               complete_info.append(f"The {k} of {name} is {crew_name}")
           if k == "fruit":
               fruit = info.get("fruit")
               if fruit.get("roman_name"):
                   fruit_name = fruit.get("roman_name")
               else:
                   fruit_name = fruit.get("name")
               fruit_type = fruit.get("type")
               if fruit.get("filename"):
                   fruit_image = fruit.get("filename")
               complete_info.append(f"The {k} of {name} is {fruit_name} which is a {fruit_type} fruit\n {fruit_image}")
           
        if entity_type == "swords":
           if k in ["description","category","isDestroy"]:
               if v:
                   if k == "description":    
                       complete_info.append(f"The {k} of {name} is\n {v}")
                   if k == "category":
                       complete_info.append(f"The {k} of {name} is {v}")
                   if k ==  "isDestroy":
                       complete_info.append(f"{name} is Destroyed")

        if entity_type == "fruits":
           if k in ["description","filename","roman_name","type"]:
               if v:
                   if k == "description":
                       complete_info.append(f"The {k} of {name} is\n {v}")
                   if k == "filename":
                       complete_info.append(f"The image of {name} can be viewed at\n {v}")
                   if k == "roman_name":
                       complete_info.append(f"The Japanese name of {name} is {v}")
                   if k == "type":
                       complete_info.append(f"The {k} of {name} is {v}")

        if entity_type == "episodes":
            if k in ["title","description","release_date","chapter"]:
                if v:
                    complete_info.append(f"The {k} of the episode is {v}")      
           
    return complete_info

def get_entity_info(entity):
    if entity == "episodes":
        number = input(f"Enter the number of the {entity[:-1]} you want info about: ")
        entity_type , info = one_piece_info(number,entity,is_episode=True)
    else:
        name = input(f"Enter the name of the {entity[:-1]} you want info about: ")
        entity_type , info = one_piece_info(name,entity)
    if entity:
        return extract_info(entity_type , info)
    else:
        return f"No {entity[:-1]} found enter a valid name"

def print_info(value):
    info = get_entity_info(value)

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
        print_info("characters")
    if option == 2:
        print_info("swords")
    if option == 3:
        print_info("fruits")
    if option == 4:
        print_info("episodes")
    
if __name__ == "__main__":
    main()