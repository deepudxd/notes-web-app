
def add_new_note():
    file=open("notes.json","w")
    id=int(input("Enter Id of the Note:"))
    title=input("Enter the title of the note:")
    content=input("Enter the content of the note:")

    file.write(f'''{{
            "id":{id},
            "title":"{title}",
            "content":"{content}"
    }}''')

    print("edited file")

add_new_note()