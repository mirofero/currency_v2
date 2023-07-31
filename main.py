from tkinter import *
import requests


# funkce
def count():
    currency_from = drop_down_from.get()
    currency_to = drop_down_to.get()
    amount = int(user_input.get())
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"

    payload = {}
    headers = {
      "apikey": "yf8D2LSALNdt6C9WB0v5gER4Qzs67CQO"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    response.raise_for_status()
    result = response.json()
    print(result["result"])
    result_label.config(text=result["result"])


# Barvy
main_color = "#7ab9ff"

# Okno
window = Tk()
window.minsize(400, 120)
window.resizable(False, False)
window.title("Převod měn")
window.config(bg=main_color)
window.iconbitmap("icon.ico")

# Uživatelský vstup
user_input = Entry(width=20, font=("Helvetica", 12), justify=CENTER)
#user_input.insert(0, "0")
user_input.grid(row=0, column=0, padx=10, pady=(10, 0))
user_input.focus()

# Roletka = z jaké měny
drop_down_from = StringVar(window)
drop_down_from.set("CZK")  # výchozí hodnota
drop_down_from_options = OptionMenu(window, drop_down_from, "CZK", "EUR", "USD")
drop_down_from_options.grid(row=0, column=1, padx=10, pady=(10, 0))

# Roletka = na jakou měnu
drop_down_to = StringVar(window)
drop_down_to.set("EUR")  # výchozí hodnota
drop_down_to_options = OptionMenu(window, drop_down_to, "CZK", "EUR", "USD")
drop_down_to_options.grid(row=1, column=1, padx=10, pady=(10, 0))

# Tlačitko
button = Button(text="Přepočet", font=("Helvetica", 12), justify=CENTER, command=count)
button.grid(row=0, column=2, padx=10, pady=(10, 0))

# Label pro zobrazení výsledku
result_label = Label(text=0, width=20, font=("Helvetica", 12), justify=CENTER)
result_label.grid(row=1, column=0, padx=10, pady=(10, 0))

# Hlavní cyklus
window.mainloop()
