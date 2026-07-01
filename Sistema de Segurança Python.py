# Lógica principal simplificada:
se_sozinho = checar_motorista_sozinho()
horario_atual = obter_horario_atual()

if se_sozinho:
    liberar_entrada()
else:
    if horario_atual >= 21:
        executar_checagem_cameras()
        enviar_whatsapp_familiar()
        chamar_policia()