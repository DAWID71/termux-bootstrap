import os

# Atualiza a lista de pacotes disponíveis
os.system("pkg update")

# Instala o módulo de API do Termux
os.system("pkg install termux-api")

# Testa a sintetização de voz em português
os.system('termux-tts-speak -l pt "Olá, mundo!"')

# Altera o idioma padrão para português
os.system("termux-config")
