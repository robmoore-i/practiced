import random

nouns = {
    "volunteer": "მოხალისე",
    "bread": "პური",
    "tea": "ჩაი",
    "teacher": "მასწავლებელი",
    "director": "დირექტორი",
    "bear": "დათვი",
    "peach": "ატამი",
    "manager": "მენეჯერი",
    "school": "სკოლა",
    "dog": "ძაღლი",
    "cat": "კატა",
    "problem": "პრობლემა",
    "police": "პოლიცია",
    "money": "ფული",
    "wallet": "საფუპე",
    "passport": "პასპორტი",
    "telephone": "ტელეფონი",
    "water": "წყალი",
    "cinema": "კინო",
    "hospital": "საავადმყოფო",
    "bed": "ლოგინი",
    "grass": "ბალახი",
    "picture": "სურათი",
    "hand": "ხელი",
    "tooth": "კბილი",
    "heart": "გული",
    "poem": "ლექსი",
    "blade edge": "გნდე",
    "frost": "თრთვილი",
    "priest": "მღვდელი",
    "gloom": "წყვდიადი",
    "morning": "დილა",
    "weather": "ამინდი",
    "town": "ქალაქი",
    "house": "სახლი",
    "day": "დღე",
    "centre": "ცენტრი",
    "train": "მატარებელი",
    "friend": "მეგობარი",
    "neighbour": "მეზობელი",
    "man": "ადამიანი",
    "today": "დღეს",
    "yesterday": "გუშინ",
    "tomorrow": "ხვალ",
    "sun": "მზე",
    "milk": "რძე",
    "moon": "მთვარე",
    "rain": "წვიმა",
    "meat": "ხორცი",
    "cheese": "ყველი",
    "colour": "ფერი",
    "horse": "ცხენი",
    "wall": "კედელი",
    "biscuit": "ნამცხვარი",
    "door": "კარი",
    "table": "მაგიდა",
    "pen": "კალამი",
    "bull": "ხარი",
    "cherry": "ალუბარი",
    "ball": "ბურთი",
    "church": "ეკლესია",
    "apple": "ვაშლი",
    "fish": "თევზი",
    "lion": "ლომი",
    "car": "მანქანა",
    "melon": "ნესვი",
    "tap": "ონკანი",
    "giraffe": "ჟირაფი",
    "elephant": "სპილო",
    "cake": "ტორტი",
    "pencil": "ფანქარი",
    "umbrella": "ქოლგა",
    "pig": "ღორი",
    "grapes": "ყურძენი",
    "bird": "ჩიტი",
    "book": "წიგნი",
    "well": "ჭა",
    "tree": "ხე",
    "owl": "ბუ",
    "opinion": "აზრი",
    "favourite": "საყვარელი",
    "world": "მსოფლიო",
    "bag": "ჩანთა",
    "shirt": "პერანგი",
    "kitchen": "სამზარეულო",
    "sky": "ცა",
    "sleep": "ძილი",
    "cloud": "ღრუბელი",
    "sailor": "მეზღვაული",
    "ship": "გემ",
    "station": "სადგური",
    "sea": "ზღვა",
    "turtle": "კუ"
}

def random_noun():
    return random.choice(list(nouns.keys()))

def translate_prompt_noun_ge_en():
    noun = random_noun()
    return {
        "prompt": "What is the english noun \"" + nouns[noun] + "\"?",
        "answer": noun
    }

def translate_prompt_noun_en_ge():
    noun = random_noun()
    return {
        "prompt": "What is the georgian noun \"" + noun + "\"?",
        "answer": nouns[noun]
    }

def translate_prompt_noun():
    return random.choice([
        translate_prompt_noun_ge_en,
        translate_prompt_noun_en_ge
    ])()
