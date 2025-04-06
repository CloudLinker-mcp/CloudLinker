**📌 README - CloudLinker**  

---

### **⚠️ ANTES DE COMENZAR: Instalar Todo Esto**  
*(Sigue los pasos en orden. Copia y pega los comandos tal cual.)*  

---

### **1️⃣ Instalar Git (Control de Versiones)**  
1. **Descarga Git**:  
   - Ve a: https://github.com/git-for-windows/git/releases/download/v2.43.0.windows.1/Git-2.43.0-64-bit.exe  
   - Haz doble clic en el archivo descargado y sigue las opciones **por defecto**.  

2. **Configura tu usuario y email** (abre **Git Bash** desde el menú Inicio y pega esto):  
   ```bash
   git config --global user.name "Tu Nombre"
   git config --global user.email "tu_email@ejemplo.com"
   ```

---

### **2️⃣ Instalar Python (Backend)**  
1. **Descarga Python 3.11**:  
   - Ve a: https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe  
   - Al instalar, **marca la casilla** que dice *"Add Python to PATH"*.  

2. **Verifica que funcione** (en **Git Bash**):  
   ```bash
   python --version
   ```
   - Debe mostrar `Python 3.11.X`.  

---

### **3️⃣ Instalar PostgreSQL (Base de Datos)**  
1. **Descarga PostgreSQL**:  
   - Ve a: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads  
   - Descarga la versión **15** para Windows.  
   - Durante la instalación:  
     - Anota la **contraseña** que pongas (la necesitarás después).  
     - Deja el puerto como `5432`.  

2. **Verifica que esté corriendo**:  
   - Busca **pgAdmin 4** en el menú Inicio y ábrelo.  

---

### **4️⃣ Clonar el Repositorio**  
1. **Abre Git Bash** y pega:  
   ```bash
   cd ~/Desktop
   git clone https://github.com/CloudLinker-mcp/CloudLinker.git
   cd CloudLinker/backend
   ```

---

### **5️⃣ Configurar Entorno Virtual (Venv)**  
1. **Crea y activa el entorno virtual** (en Git Bash):  
   ```bash
   python -m venv venv
   source venv/Scripts/activate
   ```
   - Verás `(venv)` al inicio de la línea de comandos.  

2. **Instala dependencias**:  
   ```bash
   pip install -r requirements.txt
   ```

---

### **6️⃣ Variables de Entorno (Archivo `.env`)**  
1. **Crea el archivo `.env`** en `CloudLinker/backend`:  
   - Haz clic derecho > **Nuevo > Documento de texto**.  
   - Nómbralo `.env` (asegúrate de que no sea `.env.txt`).  
   - Pega esto (cambia los valores por los tuyos):  
     ```plaintext
     DATABASE_URL="postgresql://tu_usuario_postgres:tu_contraseña_postgres@localhost:5432/cloudlinker_db"
     API_KEYS="clave1,clave2"
     ```

---

### **7️⃣ Levantar el Servidor**  
1. **Ejecuta** (en Git Bash, con el `venv` activado):  
   ```bash
   uvicorn src.main:app --reload
   ```
2. **Abre tu navegador en**:  
   ```
   http://localhost:8000/health
   ```
   - Debe mostrar: `{"status": "ok"}`.  

---

### **🔧 Herramientas Opcionales (Recomendadas)**  
- **Visual Studio Code (Editor de Código)**:  
  - Descarga: https://code.visualstudio.com/download  
- **Postman (Probar APIs)**:  
  - Descarga: https://www.postman.com/downloads/  

---

### **🚨 ¿Algo no funciona?**  
- **Error de PostgreSQL**:  
  - Asegúrate de que el servicio esté corriendo (busca *"Services"* en Windows y verifica que *"postgresql"* esté en *"Running"*).  
- **Error de Python**:  
  - Reinstala Python marcando **"Add to PATH"**.  
- **Error de Git**:  
  - Cierra y vuelve a abrir Git Bash.  

---

**✅ ¡Listo! Ahora puedes contribuir al proyecto.**  
**🔗 Repositorio:** https://github.com/CloudLinker-mcp/CloudLinker  

--- 

**¿Dudas?** Pregunta a Frank o escribe en el grupo de WhatsApp. 😊  

--- 

*(Documentación actualizada el 2024-05-01)*.
