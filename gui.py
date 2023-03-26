from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from db.session import Session
from db.car import Car
from db.brand import Brand
from db.color import Color
from db.engineandfuel import EngineAndFuel
from db.model import Model
from db.client import Client

def MainPage(root,database):
    #OKNO  # stworzenie okna
    root.title("Salon Samochodowy")  # tytuł okna
    root.iconbitmap("D:/Nauka/Python/pythonProject/Projects/DB Project/cabrio.ico")
    root.geometry("1450x610")
    root.configure(background='#ffffe5')
    mode_frame = Frame(master=root, bg='#ffff99', bd=2, padx=40, pady=10)
    mode_frame.grid(column=3, row=0, rowspan=5, padx=30, pady=20)

    #OBRAZKI
    car_photo = ImageTk.PhotoImage(Image.open("D:/Nauka/Python/pythonProject/Projects/DB Project/porsche.png"))
    label_car = Label(root, image=car_photo).grid(row=2, column=0, rowspan=3, padx=30, pady=15, columnspan=2)
    logo = ImageTk.PhotoImage(Image.open("D:/Nauka/Python/pythonProject/Projects/DB Project/logo.png"))
    label_logo = Label(image=logo).grid(row=0, column=0, rowspan=2, pady=30)

    #NAPIS
    title = Label(text='PANEL STEROWANIA\nSALONU SAMOCHODOWEGO', padx=30, pady=70, bg='#ffff99', font=90).grid(row=0, column=1, rowspan=2)

    #PRZYCISKI
    insert_button = Button(root, text='dodaj samochód', padx=60, pady=30, bg='#fffe89',cursor="mouse",command=lambda:AddPage(root, database,mode_frame)).grid(row=0, column=2, padx=10)
    delete_button = Button(root, text='usuń samochód', padx=60, pady=30, bg='#fffe89',cursor="mouse",command=lambda:DeletePage(database,mode_frame)).grid(row=1, column=2, padx=10)
    change_button = Button(root, text='edytuj samochód', padx=57, pady=30, bg='#fffe89',cursor="mouse",command=lambda:EditPage(database,mode_frame)).grid(row=2, column=2, padx=10)
    show_button = Button(root, text='pokaż samochody', padx=54, pady=30, bg='#fffe89',cursor="mouse",command=lambda:ShowCarPage(database,mode_frame)).grid(row=3, column=2, padx=10)
    show_clients = Button(root, text='pokaż klientów', padx=62, pady=30, bg='#fffe89',cursor="mouse",command=lambda:ShowClientPage(database,mode_frame)).grid(row=4, column=2, padx=10)


    root.mainloop()  # pętla główna


def AddPage(root, database, mode_frame):
    # RAMKA ZMIAN
    for widget in mode_frame.winfo_children():  # czyszczenie
        widget.destroy()
    info_label = Label(mode_frame, text='Dodawanie nowego samochodu:',bg='#ffff99', pady=20).grid(column=0,row=0, columnspan=2)

    brands=["Volkswagen", "Audi", "Seat", "Porsche"]
    v_models=["Golf", "Passat"]
    a_models=["A4", "Q2"]
    s_models=["Leon", "Toledo"]
    p_models=["911", "Cayenne"]
    engines=["1.4G", "1.6G", "2.1G", "2.8G", "1.8D", "2.2D"]
    colors=["Black","White","Blue", "Red", "Grey","Yellow"]

    #PASEK WYBORU
    def pick_model(e):
        if brand_box.get() == "Volkswagen":
            model_box.config(value=v_models)
            model_box.current(0)
        elif brand_box.get() == "Audi":
            model_box.config(value=a_models)
            model_box.current(0)
        elif brand_box.get() == "Seat":
            model_box.config(value=s_models)
            model_box.current(0)
        elif brand_box.get() == "Porsche":
            model_box.config(value=p_models)
            model_box.current(0)

    brand_box = ttk.Combobox(mode_frame, value=brands)
    brand_box.current("0")
    brand_box.grid(column=0,row=1,padx=30,pady=20, columnspan=2)
    brand_box.bind("<<ComboboxSelected>>", pick_model)

    model_box = ttk.Combobox(mode_frame, value=["`Model`"])
    model_box.current("0")
    model_box.grid(column=0,row=2,padx=30,pady=20, columnspan=2)

    engine_box = ttk.Combobox(mode_frame, value=engines)
    engine_box.current("0")
    engine_box.grid(column=0, row=3,padx=30,pady=20, columnspan=2)

    color_box = ttk.Combobox(mode_frame, value=colors)
    color_box.current("0")
    color_box.grid(column=0, row=4,padx=30,pady=20, columnspan=2)

    price_entry = Entry(mode_frame, text='Cena:', width=30)
    price_entry.grid(column=0, row=5,columnspan=2,pady=20)
    price_entry.delete(0, END)
    price_entry.insert(0,"Cena:")

    add = Button(mode_frame, text='dodaj', padx=20, pady=10, bg='green', cursor="mouse",command=lambda:AddToDB(database)).grid(row=6, column=0,pady=10)
    cancel = Button(mode_frame, text='anuluj', padx=20, pady=10, bg='red', cursor="mouse",command=lambda:CancelAdd(mode_frame)).grid(row=6, column=1,pady=10)

    #DODAWANIE DO BAZY

    def AddToDB(database):
        if ErrorCheck(mode_frame, price_entry.get()) == 1:
            return
        valueList = []
        #id
        highest_id = database.take_highest_id(Car) + 1
        valueList.append(highest_id)

        #color
        if color_box.get() == "Black":
            valueList.append(1)
        elif color_box.get() == "White":
            valueList.append(2)
        elif color_box.get() == "Blue":
            valueList.append(3)
        elif color_box.get() == "Red":
            valueList.append(4)
        elif color_box.get() == "Grey":
            valueList.append(5)
        elif color_box.get() == "Yellow":
            valueList.append(6)

        #brand & model
        if brand_box.get() == "Volkswagen" and model_box.get() == "Golf":
            valueList.append(1)
            valueList.append(1)
        elif brand_box.get() == "Volkswagen" and model_box.get() == "Passat":
            valueList.append(1)
            valueList.append(2)
        elif brand_box.get() == "Audi" and model_box.get() == "A4":
            valueList.append(2)
            valueList.append(3)
        elif brand_box.get() == "Audi" and model_box.get() == "Q2":
            valueList.append(2)
            valueList.append(4)
        elif brand_box.get() == "Seat" and model_box.get() == "Toledo":
            valueList.append(3)
            valueList.append(5)
        elif brand_box.get() == "Seat" and model_box.get() == "Leon":
            valueList.append(3)
            valueList.append(6)
        elif brand_box.get() == "Porsche" and model_box.get() == "911":
            valueList.append(4)
            valueList.append(7)
        elif brand_box.get() == "Porsche" and model_box.get() == "Cayenne":
            valueList.append(4)
            valueList.append(8)

        #price
        if int(price_entry.get()) > 0:
            valueList.append(price_entry.get())
        else:
            for widget in mode_frame.winfo_children():  # czyszczenie
                widget.destroy()
            feedback_info = Label(mode_frame, text='Błąd!', bg='#ffff99', pady=20, padx=20).grid(column=0, row=1)

        if engine_box.get() == "1.4G":
            valueList.append(1)
        elif engine_box.get() == "1.6G":
            valueList.append(2)
        elif engine_box.get() == "2.1G":
            valueList.append(3)
        elif engine_box.get() == "2.8G":
            valueList.append(4)
        elif engine_box.get() == "1.8D":
            valueList.append(5)
        elif engine_box.get() == "2.2D":
            valueList.append(6)

        carToAdd = Car(valueList[0],valueList[1],valueList[2],valueList[3],valueList[4],valueList[5])
        database.save(carToAdd)

        #komunikat
        for widget in mode_frame.winfo_children():  #czyszczenie
            widget.destroy()
        feedback_info = Label(mode_frame, text='Pomyślnie dodano do bazy!',bg='#ffff99', pady=20, padx=20).grid(column=0,row=0)
        return


def CancelAdd(mode_frame):
    for widget in mode_frame.winfo_children():  #czyszczenie
        widget.destroy()
    feedback_info = Label(mode_frame, text='Anulowano dodawanie do bazy!',bg='#ffff99', pady=20, padx=20).grid(column=0,row=0)


def DeletePage(database, mode_frame):
    for widget in mode_frame.winfo_children():  # czyszczenie
        widget.destroy()
    info_label = Label(mode_frame, text='Wybierz ID samochodu do usunięcia:', bg='#ffff99', pady=20).grid(column=0, row=0, columnspan=2)

    results = database.join_car(Car, Brand, Model, EngineAndFuel, Color)
    i = 1
    for _car, _brand, _model, _engine, _color in results:
        joined_cars = Label(mode_frame, bg='#ffff99',
                            text='ID: ' + str(_car.id) + " AUTO: " + str(_brand.brand) + ' ' + str(
                                _model.model) + ' SILNIK: ' + str(_engine.designation) + ' ' + str(
                                _engine.fuel) + ' KOLOR: ' + str(_color.color))
        joined_cars.grid(column=0, row=i, pady=1, columnspan=2, sticky='w')
        i += 1

    id_entry = Entry(mode_frame, width=40)
    id_entry.grid(column=0, row=i, pady=20)
    id_entry.delete(0, END)
    id_entry.insert(0, "Podaj ID:")

    delete = Button(mode_frame, text='usuń', padx=20, pady=10, bg='red', cursor="mouse", command=lambda:DeleteFromDB(database,id_entry)).grid(row=i, column=1, pady=10)

    def DeleteFromDB(database, id_entry):
        ErrorCheck(mode_frame,id_entry.get())
        database.remove(Car, id_entry.get())
        for widget in mode_frame.winfo_children():  # czyszczenie
            widget.destroy()
        feedback_info = Label(mode_frame, text='Usunięto z bazy!', bg='#ffff99', pady=20, padx=20).grid(column=0, row=0)
        return


def EditPage(database, mode_frame):
    for widget in mode_frame.winfo_children():  # czyszczenie
        widget.destroy()
    info_label = Label(mode_frame, text='Wybierz ID samochodu który chcesz modyfikować:', bg='#ffff99', pady=20).grid(column=0, row=0, columnspan=2)

    results = database.join_car(Car, Brand, Model, EngineAndFuel, Color)
    i = 1
    for _car, _brand, _model, _engine, _color in results:
        joined_cars = Label(mode_frame, bg='#ffff99',
                            text='ID: ' + str(_car.id) + " AUTO: " + str(_brand.brand) + ' ' + str(
                                _model.model) + ' SILNIK: ' + str(_engine.designation) + ' ' + str(
                                _engine.fuel) + ' KOLOR: ' + str(_color.color) + " CENA: "+ str(_car.price))
        joined_cars.grid(column=0, row=i, pady=1, columnspan=2, sticky='w')
        i += 1

    id_entry = Entry(mode_frame, width=30)
    id_entry.grid(column=0, row=i, pady=20)
    id_entry.delete(0, END)
    id_entry.insert(0, "Podaj ID:")

    update = Button(mode_frame, text='modyfikuj', padx=20, pady=10, bg='yellow', cursor="mouse", command=lambda:UpdateDB(database,id_entry.get())).grid(row=i, column=1, pady=10)

    def UpdateDB(database,id_entry):
        for widget in mode_frame.winfo_children():  # czyszczenie
            widget.destroy()
        info_label = Label(mode_frame, text='Co chcesz modyfikować:', bg='#ffff99', pady=20).grid(column=0, row=0, columnspan=2)

        if ErrorCheck(mode_frame, id_entry) == 1:
            return

        car_id =  id_entry

        v=StringVar()
        op1=Radiobutton(mode_frame, text="Marka", bg='#ffff99', variable=v, value="brand")
        op1.grid(column=0, row=1, columnspan=2)
        op2=Radiobutton(mode_frame, text="Model", bg='#ffff99', variable=v, value="model")
        op2.grid(column=0, row=2, columnspan=2)
        op3=Radiobutton(mode_frame, text="Silnik", bg='#ffff99', variable=v, value="engineandfuel")
        op3.grid(column=0, row=3, columnspan=2)
        op4=Radiobutton(mode_frame, text="Kolor", bg='#ffff99', variable=v, value="color")
        op4.grid(column=0, row=4, columnspan=2)
        op5=Radiobutton(mode_frame, text="Cena", bg='#ffff99', variable=v, value="price")
        op5.grid(column=0, row=5, columnspan=2)

        ok = Button(mode_frame, text='OK', padx=20, pady=10, bg='yellow', cursor="mouse", command=lambda: Change(database, car_id, v.get())).grid(row=i, column=0, pady=10, columnspan=2)

    def Change(database, car_id, v):
        for widget in mode_frame.winfo_children():  # czyszczenie
            widget.destroy()
        info_label = Label(mode_frame, text='Zmodyfikuj dane:', bg='#ffff99', pady=20).grid(column=0, row=0, columnspan=2)
        choosen_car = database.take(Car, car_id)

        brands = ["Volkswagen", "Audi", "Seat", "Porsche"]
        v_models = ["Golf", "Passat"]
        a_models = ["A4", "Q2"]
        s_models = ["Leon", "Toledo"]
        p_models = ["911", "Cayenne"]
        engines = ["1.4G", "1.6G", "2.1G", "2.8G", "1.8D", "2.2D"]
        colors = ["Black", "White", "Blue", "Red", "Grey", "Yellow"]
        prices = [30000, 40000, 50000, 75000, 100000, 150000]

        if v == 'brand':
            engine_box = ttk.Combobox(mode_frame, value=brands)
            engine_box.current("0")
            engine_box.grid(column=0, row=1, padx=30, pady=20, columnspan=2)
            old_value=database.take_old_value(Car,car_id,v)
        elif v == 'model' and choosen_car == 1:
            engine_box = ttk.Combobox(mode_frame, value=v_models)
            engine_box.current("0")
            engine_box.grid(column=0, row=1, padx=30, pady=20, columnspan=2)
            old_value = database.take_old_value(Car, car_id, v)
        elif v == 'model' and choosen_car == 2:
            engine_box = ttk.Combobox(mode_frame, value=a_models)
            engine_box.current("0")
            engine_box.grid(column=0, row=1, padx=30, pady=20, columnspan=2)
            old_value = database.take_old_value(Car, car_id, v)
        elif v == 'model' and choosen_car == 3:
            engine_box = ttk.Combobox(mode_frame, value=s_models)
            engine_box.current("0")
            engine_box.grid(column=0, row=1, padx=30, pady=20, columnspan=2)
            old_value = database.take_old_value(Car, car_id, v)
        elif v == 'model' and choosen_car == 4:
            engine_box = ttk.Combobox(mode_frame, value=p_models)
            engine_box.current("0")
            engine_box.grid(column=0, row=1, padx=30, pady=20, columnspan=2)
            old_value = database.take_old_value(Car, car_id, v)
        elif v == 'engineandfuel':
            engine_box = ttk.Combobox(mode_frame, value=engines)
            engine_box.current("0")
            engine_box.grid(column=0, row=1, padx=30, pady=20, columnspan=2)
            old_value = database.take_old_value(Car, car_id, v)
        elif v == 'color':
            engine_box = ttk.Combobox(mode_frame, value=colors)
            engine_box.current("0")
            engine_box.grid(column=0, row=1, padx=30, pady=20, columnspan=2)
            old_value = database.take_old_value(Car, car_id, v)
        elif v == 'price':
            engine_box = ttk.Combobox(mode_frame, value=prices)
            engine_box.current("0")
            engine_box.grid(column=0, row=1, padx=30, pady=20, columnspan=2)
            old_value = database.take_old_value(Car, car_id, v)

        confirm = Button(mode_frame, text='Zatwierdź', padx=20, pady=10, bg='yellow', cursor="mouse",
                             command=lambda: finally_accept_change(database, v, car_id, old_value, engine_box)).grid(row=i, column=0, pady=10, columnspan=2)

    def finally_accept_change(database, column, car_id, old, new):
        #print(car_id)
        if column == 'brand' and new.get() == "Volkswagen":
            new_value=1
        elif column == 'brand' and new.get() == "Audi":
            new_value=2
        elif column == 'brand' and new.get() == "Seat":
            new_value=3
        elif column == 'brand' and new.get() == "Porsche":
            new_value=4
        elif column == 'model' and new.get() == "Golf":
            new_value=1
        elif column == 'model' and new.get() == "Passat":
            new_value=2
        elif column == 'model' and new.get() == "A4":
            new_value=3
        elif column == 'model' and new.get() == "Q2":
            new_value=4
        elif column == 'model' and new.get() == "Toledo":
            new_value=5
        elif column == 'model' and new.get() == "Leon":
            new_value=6
        elif column == 'model' and new.get() == "911":
            new_value=7
        elif column == 'model' and new.get() == "Cayenne":
            new_value=8
        elif column == 'engineandfuel' and new.get() == "1.4G":
            new_value=1
        elif column == 'engineandfuel' and new.get() == "1.6G":
            new_value=2
        elif column == 'engineandfuel' and new.get() == "2.1G":
            new_value=3
        elif column == 'engineandfuel' and new.get() == "2.8G":
            new_value=4
        elif column == 'engineandfuel' and new.get() == "1.8D":
            new_value=5
        elif column == 'engineandfuel' and new.get() == "2.2D":
            new_value=6
        elif column == 'color' and new.get() == "Black":
            new_value=1
        elif column == 'color' and new.get() == "White":
            new_value = 2
        elif column == 'color' and new.get() == "Blue":
            new_value=3
        elif column == 'color' and new.get() == "Red":
            new_value=4
        elif column == 'color' and new.get() == "Grey":
            new_value=5
        elif column == 'color' and new.get() == "Yellow":
            new_value=6
        elif column=="price":
            new_value=new.get()

        database.modify(column, car_id, old, new_value)

        for widget in mode_frame.winfo_children():  #czyszczenie
            widget.destroy()
        feedback_info = Label(mode_frame, text='Pomyślnie zmodyfikowano bazę!',bg='#ffff99', pady=20, padx=20).grid(column=0,row=1)
        return


def ShowCarPage(database, mode_frame):
    for widget in mode_frame.winfo_children():  # czyszczenie
        widget.destroy()
    info_label = Label(mode_frame, text='Samochody w bazie:', bg='#ffff99', pady=20).grid(column=0, row=0, columnspan=2)

    results=database.join_car(Car, Brand, Model, EngineAndFuel, Color)
    i=1
    for _car, _brand, _model, _engine, _color in results:
        joined_cars=Label(mode_frame,bg='#ffff99',text=str(_brand.brand)+' ' +str(_model.model)+' SILNIK: '+ str(_engine.designation)+ ' '+str(_engine.fuel)+' KOLOR: '+ str(_color.color)+" CENA: "+str(_car.price))
        joined_cars.grid(column=0,row=i, pady=2, columnspan=2,sticky='w')
        i+=1
    return


def ShowClientPage(database, mode_frame):
    for widget in mode_frame.winfo_children():  # czyszczenie
        widget.destroy()
    info_label = Label(mode_frame, text='Klienci w bazie:', bg='#ffff99', pady=20).grid(column=0, row=0, columnspan=2)

    results = database.join_client(Client)
    i = 1
    for _client in results:
        joined_client = Label(mode_frame, bg='#ffff99', text=str(_client.client_name)+ " "+ str(_client.surname)+' ADRES: '+str(_client.address))
        joined_client.grid(column=0, row=i, pady=2, columnspan=2, sticky='w')
        i+=1

    return

def ErrorCheck(mode_frame, entry):
    try:
        int(entry)
    except:
        print('error')
        for widget in mode_frame.winfo_children():  # czyszczenie
            widget.destroy()
        info_label = Label(mode_frame, text='Błąd!', bg='#ffff99', pady=20).grid(column=0, row=0, columnspan=2)
        return 1