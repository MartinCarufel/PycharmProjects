import tkinter as tk
import tkinter.ttk as ttk

CHOIX = ["oui", "non", "peut-être"]
JOURS_SEMAINE = ['Lundi', 'Mardi', 'Mercredi',
                    'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']


class DemoWidget(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.champs = {
            'message': tk.StringVar(),
            'jour': tk.StringVar(),
            'choix': tk.IntVar(),
            'conditions': tk.BooleanVar(),
        }
        self._create_gui()
        self.pack()

    def _create_gui(self):
        label = tk.Label(self, text="Un message")
        label.grid(column=0, row=0)

        text = tk.Entry(self, textvariable=self.champs['message'])
        text.grid(column=1, row=0, columnspan=2)

        label = tk.Label(self, text="Un choix")
        label.grid(column=0, row=1)

        combo = ttk.Combobox(self, values=JOURS_SEMAINE,
                                textvariable=self.champs['jour'])
        combo.grid(column=1, row=1, columnspan=2)

        for i, rb_label in enumerate(CHOIX):
            rb = ttk.Radiobutton(self, text=rb_label, value=i,
                                    variable=self.champs['choix'])
            rb.grid(column=i, row=2)

        checkButton = ttk.Checkbutton(self, text="Accepter les conditions",
                                      variable=self.champs['conditions'])
        checkButton.grid(column=0, row=3, columnspan=3)

        button = tk.Button(self, text="Valider", command=self.valider)
        button.grid(column=0, row=4)

        button = tk.Button(self, text="Fermer", command=app.quit)
        button.grid(column=2, row=4)

    def valider(self):
        """affiche les valeurs saisies sur la console
            mais on pourrait faire quelque chose de plus intéressant"""
        for v, k in self.champs.items():
            print(f"{v} : {k.get()}")


app = tk.Tk()
app.title("Demo Widgets")
DemoWidget(app)
app.mainloop()