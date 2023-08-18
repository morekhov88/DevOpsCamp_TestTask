# <hosts.txt> - inventory файл  
# Ключ -K нужен для ввода пароля и выполнения команд под sudo 

# Команда для запуска
ansible-playbook -i <hosts.txt> playbook.yml -K
