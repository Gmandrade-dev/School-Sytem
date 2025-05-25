import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("600x400")
app.title("CTkTabview dentro de CTkTabview")

# Tabview principal
tabview_main = ctk.CTkTabview(app)
tabview_main.pack(expand=True, fill="both", padx=20, pady=20)

# Criar abas no Tabview principal
tab1 = tabview_main.add("Aba 1")
tab2 = tabview_main.add("Aba 2")

# Tabview secundário dentro da Aba 1
tabview_inner = ctk.CTkTabview(tab1)
tabview_inner.pack(expand=True, fill="both", padx=10, pady=10)

# Abas dentro do Tabview secundário
inner_tab1 = tabview_inner.add("SubAba 1")
inner_tab2 = tabview_inner.add("SubAba 2")

# Adicionar algum conteúdo na SubAba
label = ctk.CTkLabel(inner_tab1, text="Conteúdo da SubAba 1")
label.pack(pady=20)

label2 = ctk.CTkLabel(inner_tab2, text="Conteúdo da SubAba 2")
label2.pack(pady=20)

app.mainloop()
