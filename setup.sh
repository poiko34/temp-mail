#!/bin/bash

# Устанавливаем mailtm
sudo pip3 install mailtm --break-system-packages

cp mail.py /
# Исправляем символы возврата каретки (\r) в mail.py (если они есть)
dos2unix /mail.py

# Или, если dos2unix не доступен, используем sed
# sed -i 's/\r//g' /home/mrhacker/Desktop/temp-mail/mail.py

# Делаем mail.py исполнимым и доступным как команду
chmod +x /mail.py

# Создаем символическую ссылку для запуска команды mail
ln -s /mail.py /usr/local/bin/mail

# Деактивируем виртуальное окружение
deactivate
clear
echo Installation complete
