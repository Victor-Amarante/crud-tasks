# 📝 Task API - Django REST Framework

API RESTful para gerenciamento de tarefas, construída com Django REST Framework.  
Permite criar, listar, atualizar e excluir tarefas, além de filtrar por status.

## 🚀 Tecnologias Utilizadas

- **Python** (Django & Django REST Framework)
- **SQLite** (pode ser substituído por PostgreSQL/MySQL)
- **Django Filter** (para filtragem)
- **Pagination & Search** (pesquisa e paginação de tarefas)

---

## 📦 Instalação e Configuração

### 1️⃣ **Clone o repositório**
```sh
git clone https://github.com/Victor-Amarante/crud-tasks.git
cd crud-tasks
```

### 2️⃣ **Crie e ative um ambiente virtual**
```sh
python3 -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
```

### 3️⃣ **Instale as dependências**
```sh
pip install -r requirements.txt
```

### 4️⃣ **Realize as migrações**
```sh
python manage.py migrate
```

### 5️⃣ **Crie um superusuário (opcional)**
```sh
python manage.py createsuperuser
```

### 6️⃣ **Inicie o servidor**
```sh
python manage.py runserver
```
A API estará disponível em [`http://127.0.0.1:8000/api/v1/tasks/`](http://127.0.0.1:8000/api/v1/tasks/).

---

## 📌 Endpoints da API

### 📍 **Criar uma Tarefa**
- **POST** `/api/v1/tasks/`
- **Body JSON**:
  ```json
  {
    "title": "Estudar Django",
    "description": "Aprender Django REST Framework",
    "status": "pending",
    "due_date": "2024-12-31"
  }
  ```
- **Resposta**: `201 Created`

---

### 📍 **Listar Todas as Tarefas**
- **GET** `/api/v1/tasks/`
- **Resposta**:
  ```json
  [
    {
      "id": 1,
      "title": "Estudar Django",
      "description": "Aprender Django REST Framework",
      "status": "pending",
      "due_date": "2024-12-31"
    }
  ]
  ```
- **Paginação & Pesquisa**:  
  - `?search=django` → Filtra pelo título ou descrição
  - `?status=pendente` → Filtra por status

---

### 📍 **Buscar uma Tarefa por ID**
- **GET** `/api/v1/tasks/{id}/`

---

### 📍 **Atualizar uma Tarefa**
- **PUT** `/api/v1/tasks/{id}/`
- **Body JSON**:
  ```json
  {
    "title": "Estudar Django - Revisão",
    "description": "Revisar conceitos do DRF",
    "status": "working",
    "due_date": "2024-12-28"
  }
  ```
- **Resposta**: `200 OK`

---

### 📍 **Excluir uma Tarefa**
- **DELETE** `/api/v1/tasks/{id}/`
- **Resposta**:
  ```json
  {
    "message": "Tarefa excluída com sucesso"
  }
  ```
- **Resposta HTTP**: `204 No Content`

---

## 🔑 Autenticação e Permissões

A API usa **SessionAuthentication** e permite acesso somente autenticado para operações de escrita.  
Para autenticar-se, faça login em: [`http://127.0.0.1:8000/admin/`](http://127.0.0.1:8000/admin/).

---

## 🛠 Autor

👤 **Victor Amarante**  
🔗 [GitHub](https://github.com/Victor-Amarante)