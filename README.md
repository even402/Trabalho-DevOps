**Documentação do Projeto - Execução do Pipeline CI/CD com Docker e Jenkins**

---

### ✨ Objetivo

Executar um pipeline automatizado com o Jenkins para construir e rodar um container Docker com uma aplicação backend Python, e enviar notificações por e-mail.

---

## 📁 Estrutura do Projeto

```
HelpDeskApp/
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
└── Jenkinsfile
```

---

## 🚀 Etapas do Setup (Windows e Linux)

### 1. **Instalar o Docker**

* **Windows**: Instale o [Docker Desktop](https://www.docker.com/products/docker-desktop/).
* **Linux (Debian/Ubuntu)**:

  ```bash
  sudo apt update
  sudo apt install -y docker.io
  sudo systemctl enable docker
  sudo systemctl start docker
  ```

### 2. **Instalar o Jenkins**

#### Via Docker (Recomendado para ambos):

```bash
# Executar Jenkins com acesso ao Docker host
docker run -d \
  --name jenkins \
  -p 8081:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -u root \
  jenkins/jenkins:lts
```

### 3. **Obter Senha Inicial do Jenkins**

```bash
# Pegue a senha inicial
sudo docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Acesse: `http://localhost:8081`
Cole a senha para acessar a interface web.

---

## ⚖️ Configuração do Projeto no Jenkins

### 1. **Criar Novo Job**

* Tipo: *Pipeline*
* Nome: `HelpDeskApp`

### 2. **Configuração do SCM**

* **Pipeline script from SCM**
* SCM: Git
* URL: `https://github.com/Even402/HelpDeskApp.git`
* Branch: `*/main`
* Script Path: `Jenkinsfile`

---

## 📃 Jenkinsfile de Exemplo

```groovy
pipeline {
    agent any

    stages {
        stage('Build Backend Docker') {
            steps {
                dir('backend') {
                    sh 'docker build -t agendamento-app .'
                }
            }
        }
        stage('Executar Container Backend') {
            steps {
                sh 'docker run --rm agendamento-app'
            }
        }
    }
}
```

---

## 🔧 Dockerfile do Backend

```Dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

---

## 📧 Configuração de Envio de E-mail (Mailtrap ou SMTP)

Configure no código `app.py` ou no Jenkins plugin *Email Extension*. Exemplo com Mailtrap:

```python
import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Seu agendamento foi processado com sucesso!")
msg['Subject'] = "Confirmação"
msg['From'] = "from@example.com"
msg['To'] = "to@example.com"

s = smtplib.SMTP("smtp.mailtrap.io", 2525)
s.login("usuario", "senha")
s.send_message(msg)
s.quit()
```

---


### 1. **Print do Jenkins executando pipeline**

* Menu > Build History > última execução > Console Output

### 2. **Print do repositório GitHub com estrutura**

* Mostrar `Jenkinsfile`, pasta `backend/`, etc.

### 3. **Print do e-mail ou log de envio no console**

---

## 📄 Observações Finais

* Verifique se a porta usada pelo container está livre (use `docker ps`).
* O Jenkins precisa ter permissão para acessar o Docker host (volume `/var/run/docker.sock`).

---

📅 Projeto testado com sucesso em: **20/06/2025**
Responsável: *Rosana Even dos Anjos Araujo*
Faculdade: *ESBAM* | Disciplina: *DevOps com Docker e Jenkins*
