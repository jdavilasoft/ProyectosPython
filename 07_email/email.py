email = input("Ingresa tu e-mail: ")

usuario, dominio = email.split("@")

usuario_separado = usuario.split(".")

if dominio == "gmail.com":
    frase_final = "estoy viendo que tu email esta registrado en Google. Es genial!"
else:
    dominio_separado = dominio.split(".")
    frase_final = "observo que estas usando un dominio personalizado de: " + dominio_separado[0]

print("Hola", usuario_separado[0], frase_final)