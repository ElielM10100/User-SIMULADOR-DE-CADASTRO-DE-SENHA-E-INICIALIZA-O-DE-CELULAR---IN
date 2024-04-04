# Definindo a senha
senha_correta = "1234"

# Loop para permitir 3 tentativas
for tentativa in range(3):
    senha_digitada = input("Por favor, insira a senha: ")

    # Verifica se a senha está correta
    if senha_digitada == senha_correta:
        print("Bem-vindo.")
        break  # Sai do loop se a senha estiver correta
    else:
        # Calcula o número de tentativas restantes
        tentativas_restantes = 3 - (tentativa + 1)
        if tentativas_restantes > 0:
            print(f"Senha incorreta. Você tem {tentativas_restantes} tentativa(s) restante(s).")
        else:
            print("Senha incorreta. O celular foi bloqueado.")
            break  # Sai do loop se exceder o número de tentativas

# Se o loop for concluído sem quebrar, significa que todas as tentativas foram usadas
else:
    print("Número máximo de tentativas excedido. O celular foi bloqueado.")
