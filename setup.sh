#!/bin/bash

# Устанавливаем python3-venv и создаем виртуальное окружение
apt install python3-venv -y
python3 -m venv path/to/venv
python3 -m venv myenv

# Активируем виртуальное окружение
source myenv/bin/activate

# Устанавливаем пакет MailTm через pip
pip3 install MailTm

# Устанавливаем pipx для установки Python приложений
apt install pipx -y
pipx install MailTm

# Устанавливаем python3-xyz через apt
apt install python3-xyz -y

# Устанавливаем MailTm через pip с флагом --break-system-packages
pip install MailTm --break-system-packages
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
