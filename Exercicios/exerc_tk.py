import customtkinter as ctk

janela = ctk.CTk()

janela.title('App Walace')

janela.geometry("300x300")

ctk.set_appearance_mode('system')

texto_01 = ctk.CTkLabel(janela, text='Nome')
texto_01.pack()

botao_01 = ctk.CTkButton(janela, text='Botão 1')
botao_01.pack()

janela.mainloop()
