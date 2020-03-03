from tkinter import *
from PIL import ImageTk, Image
import time
import json
from functools import partial
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="skovde"
)
curs = mydb.cursor()
global_array = dict()

def base_ui(root, frame):
    print("New scene")
    frame.forget()
def clear_frame(frame):
    print("Clear frame")
    #frame.destroy()
def sync_data(root):
    # Sync data
    sync_frame = Frame(root, width=700, height=200, bd=1,pady=100, relief="solid")
    sync_frame.pack()
    my_img = ImageTk.PhotoImage(Image.open("logo.png"))
    my_label = Label(sync_frame, image=my_img)
    my_label.image = my_img
    my_label.pack()
#    sync_text1 = Text(sync_frame)
#    sync_text1.tag_configure("center", justify='center')
#    sync_text1.insert(INSERT,"Syncar data från databas...")
#    sync_text1.tag_add("center", "1.0", "end")
#    sync_text1.pack()

    #ipath = "logo.png"
    #img = ImageTk.PhotoImage(Image.open(ipath))
    #panel = Label(sync_frame, image = img)
    #panel.pack(side = "bottom", fill = "both", expand = "yes")

    sl_1 = Label(sync_frame,font="Times 20", text="Syncar data från databas.....",pady=20, padx=120)
    sl_1.pack()

    root.after(1000, clear_frame(sync_frame))
    root.mainloop()








def sync_new():
    print("Collecting data", end="\r")

    curs.execute("SELECT * FROM {0} WHERE backup = {1} ORDER BY id DESC".format("print", 0))
    res = curs.fetchall()
    for i, y in enumerate(res):
        global_array[i] = [y[0], y[1], y[2], y[3],y[4]]
    time.sleep(0.1)
    print("Collecting data # Up to date", end="\n")

def preview(id, frame, content, navbar):
    print("PREVIEW CLICKED - ", id, frame)
    #curs.execute("SELECT * FROM {0} WHERE id = {1}".format("print", id))
    #res = curs.fetchall()
    #for i in res:
    #    print(i)
    #    Label(frame, text = i[])
    for widget in frame.winfo_children():
        widget.destroy()  # Clears frame before inserts
    for widget in navbar.winfo_children():
        widget.destroy()
    # Rebuild navbar
    Label(navbar,font=('Helvetica', 18, 'bold'), text = "Skövdehem AB", bg = "white").pack(side=TOP, anchor="w",pady=(10, 0), padx=(10, 0))
    Label(navbar,font=('Helvetica', 8), text = "Nya inskick: {0}".format(3), bg = "white").pack(side=TOP, anchor="w", pady=(0, 20), padx=(10, 0))
    Button(navbar, text = "Skriv ut alla").pack(side=LEFT, anchor="w", pady=(0, 10), padx=(10, 0))
    Button(navbar, text = "Rensa").pack(side=LEFT, anchor="w", pady=(0, 10), padx=10)
    Button(navbar, text = "Skriv ut enskild").pack(side=RIGHT, anchor="w", pady=(0, 10), padx=10)
    # Rebuild navbar
    if content["perm_enter"] == 1:
        permtoenter = "Ja"
    else:
        permtoenter = "Nej"
    Label(frame, font=("Helvetica", 8, ""), text = "Adress", anchor="w", width=40).pack(padx=(0, 100), anchor="w")
    Label(frame, font=("Helvetica", 10, "bold"), text = content["adress"]).pack(padx=(0, 100), pady=(0, 10), anchor="w")

    Label(frame, font=("Helvetica", 8, ""), text = "Lägenhetsnummer", anchor="w").pack(padx=(0, 100), anchor="w")
    Label(frame, font=("Helvetica", 10, "bold"), text = content["lghnr"]).pack(padx=(0, 100), pady=(0, 10), anchor="w")

    Label(frame, font=("Helvetica", 8, ""), text = "Namn", anchor="w").pack(padx=(0, 100), anchor="w")
    Label(frame, font=("Helvetica", 10, "bold"), text = content["name"]).pack(padx=(0, 100), pady=(0, 10), anchor="w")

    Label(frame, font=("Helvetica", 8, ""), text = "Telefonnummer", anchor="w").pack(padx=(0, 100), anchor="w")
    Label(frame, font=("Helvetica", 10, "bold"), text = content["phonenumber"]).pack(padx=(0, 100), pady=(0, 10), anchor="w")

    Label(frame, font=("Helvetica", 8, ""), text = "Får vi gå in med huvudnyckel?", anchor="w").pack(padx=(0, 100), pady=(5,0), anchor="w")
    Label(frame, font=("Helvetica", 10, "bold"), text = permtoenter).pack(padx=(0, 100), pady=(0, 10), anchor="w")

    Label(frame, font=("Helvetica", 8, ""), text = "Beskrivning på problemet", anchor="w").pack(padx=(0, 100), pady=(5,0), anchor="w")
    Label(frame, font=("Helvetica", 10, "bold"), text = content["comments"],justify=LEFT, wraplength=400, anchor="w").pack(padx=(0, 100), pady=(0, 10), anchor="w")


def main_window(root):
    print("Starting main frame")
    #mf = Frame(root, width=700, height=200, bd=1,pady=100, relief="solid").pack()
    # Top bar
    total_number = len(global_array)
    ft = Frame(root, bg = "white")
    ft.pack(side=TOP, fill='x')
    #right_frame = Frame(ft, height=50, bg="#000").pack(side=TOP, fill="both", pady=20, padx=20)

    Label(ft,font=('Helvetica', 18, 'bold'), text = "Skövdehem AB", bg = "white").pack(side=TOP, anchor="w",pady=(10, 0), padx=(10, 0))
    Label(ft,font=('Helvetica', 8), text = "Nya inskick: {0}".format(total_number), bg = "white").pack(side=TOP, anchor="w", pady=(0, 20), padx=(10, 0))
    Button(ft, text = "Skriv ut alla").pack(side=LEFT, anchor="w", pady=(0, 10), padx=(10, 0))
    Button(ft, text = "Rensa").pack(side=LEFT, anchor="w", pady=(0, 10), padx=10)

    #Label(ft, text = "D: whost TABLE: prints | succesful").pack(side=TOP, anchor="w")
    f_status = Frame(root)
    f_status.pack(side=BOTTOM, fill="x", pady = (1,1), padx = (1, 0), anchor="w")
    # Left frame toptext
    Label(f_status, font=('Helvetica', 8), text="Status: READY | up to date").pack(anchor="w")
    #print_all_btn = Button(
    #    button_frame,
    #    text = "Skriv ut alla",
    #    anchor="w",
    #    padx=30,
    #    pady=5,
    #    fg="#f4f4f4",
    #    font=('Helvetica', 10, "bold"),
    #    bg="#2ecc71",
    #    borderwidth=0,
    #    bd=0,
    #    highlightthickness=0
    #    ).pack(side=LEFT, fill="both", anchor="w", padx=30,pady=(20, 10))
    #clear_all_items = Button(
    #    button_frame,
    #    text = "Rensa",
    #    anchor="w",
    #    padx=30,
    #    pady=5,
    #    fg="#f4f4f4",
    #    font=('Helvetica', 10, "bold"),
    #    bg="#cc2e2e",
    #    borderwidth=0,
    #    bd=0,
    #    highlightthickness=0
    #    ).pack(side=LEFT, fill="both", anchor="w", padx=30,pady=(20, 10))

    f = Frame(root, bg = "#f4f4f4")
    f.pack(side=LEFT, anchor="nw", pady=(0, 50), expand=TRUE, fill="both")
    # Left frame toptext
    Label(f, font=('Helvetica', 8), bg="#f4f4f4",text="New reports").pack(side=TOP, anchor="w", pady = (10, 5), padx = 10)


    # Left column
    f3 = Frame(f, bg = "#f4f4f4")
    f3.pack(side=LEFT,pady = (0,20), padx = 10, anchor="nw")


    # RIGHT SIDE ONLY ON CLICK
    f2 = Frame(root, width=300, bg = "#f4f0f0")
    f2.pack(side=RIGHT, pady = (0, 50), padx = (5, 5), fill="both", expand=TRUE, anchor="nw")
    for i in global_array:
        #print(global_array[i][4])
        if global_array[i][1] == 1:
            prefix = "Felanmälan  "
        elif global_array[i][1] == 2:
            prefix = "Intresseanm"
        contents = json.loads(global_array[i][4])
        #for x, y in enumerate(contents):
            #print(x)
            #print(x, y)
        partial_args = partial(preview, global_array[i][0], f2, contents, ft)
        Button(f3,
        text = "{0}    |    {3}    |    {1}    -    {2}".format(prefix, contents['adress'], contents['name'], contents["on_date"]),
        font=('Helvetica', 9, "bold"),
        anchor="w",
        fg = '#544e4e',
        bg = '#f9f9f9',
        bd =  0,
        highlightthickness=0,
        highlightcolor="#ffffff",
        highlightbackground="#ffffff",
        borderwidth=0,
        relief="solid",
        pady=5,
        padx=5,
        command=partial_args
        ).grid(row=i, column=0, pady=3, sticky="nsew")
        Grid.columnconfigure(f2, i, weight=1)

    root.mainloop()
def init_ui():
    root = Tk()
    root.title("Extrationsprogram")
    root.call('wm', 'iconphoto', root._w, ImageTk.PhotoImage(file='icon.png'))
    #sync_data(root)     # SYNC DATA Sync before mainloop instead
    sync_new()
    main_window(root)
    #text1 = Button(frame, text="lite text")
    #text1.pack(side=TOP)
