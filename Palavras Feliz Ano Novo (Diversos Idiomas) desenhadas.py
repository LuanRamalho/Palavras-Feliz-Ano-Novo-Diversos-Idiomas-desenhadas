import tkinter as tk
from tkinter import font

def create_app():
    # Cria a janela principal
    root = tk.Tk()
    root.title("Ano Novo em Diferentes Idiomas")
    root.geometry("600x400")
    root.configure(bg="#2F4F4F")

    # Configura fonte personalizada
    title_font = font.Font(family="Helvetica", size=24, weight="bold")
    text_font = font.Font(family="Helvetica", size=16)

    # Título
    title_label = tk.Label(root, text="Feliz Ano Novo!", font=title_font, bg="#FFD700", fg="#2F4F4F", padx=10, pady=10)
    title_label.pack(pady=20)

    # Dicionário de idiomas
    translations = {
        "Português": "Feliz Ano Novo",
        "Inglês": "Happy New Year",
        "Francês": "Bonne Année Nouveau",
        "Espanhol": "Feliz Año Nuevo",
        "Italiano": "Buon Anno Nuovo",
        "Alemão": "Frohes Neues Jahr"
    }

    # Adiciona os textos à interface
    frame = tk.Frame(root, bg="#2F4F4F")
    frame.pack()

    colors = ["#FF4500", "#1E90FF", "#32CD32", "#FFD700", "#9400D3", "#FF69B4"]

    for i, (language, text) in enumerate(translations.items()):
        label = tk.Label(
            frame,
            text=f"{language}: {text}",
            font=text_font,
            bg="#2F4F4F",
            fg=colors[i % len(colors)],
            padx=10,
            pady=5
        )
        label.grid(row=i, column=0, sticky="w", padx=50, pady=5)

    # Botão de saída
    exit_button = tk.Button(root, text="Sair", command=root.quit, bg="#FF6347", fg="white", font=text_font)
    exit_button.pack(pady=20)

    return root

if __name__ == "__main__":
    app = create_app()
    app.mainloop()
