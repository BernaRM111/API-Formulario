# from fastapi import FastAPI, HTTPException, status, Form
# from pydantic import BaseModel, EmailStr
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from dotenv import load_dotenv
# import os
# from fastapi.middleware.cors import CORSMiddleware 

# load_dotenv()

# SMTP_SERVER = os.getenv("SMTP_SERVER")
# SMTP_PORT = int(os.getenv("SMTP_PORT"))
# SMTP_EMAIL = os.getenv("SMTP_EMAIL")
# SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class ContactForm(BaseModel):
#     nombre: str
#     apellidos: str
#     email: EmailStr
#     mensaje: str

# def enviar_correo_verificacion(nombre: str, email: str, mensaje: str):
#     try:
#         msg = MIMEMultipart()
#         msg["From"] = SMTP_EMAIL
#         msg["To"] = email
#         msg["Subject"] = "Verificación de Contacto"

#         # Contenido del correo
#         body = f"""
#         <h1>Hola, {nombre}!</h1>
#         <p>Gracias por contactarnos. Hemos recibido tu mensaje:</p>
#         <blockquote>{mensaje}</blockquote>
#         <p>Nos pondremos en contacto contigo pronto.</p>
#         """

#         msg.attach(MIMEText(body, "html"))

#         with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
#             server.starttls()
#             server.login(SMTP_EMAIL, SMTP_PASSWORD)
#             server.sendmail(SMTP_EMAIL, email, msg.as_string())

#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=f"Error al enviar el correo: {str(e)}"
#         )

# @app.post("/contacto")
# async def enviar_formulario_contacto(form: ContactForm):
#     enviar_correo_verificacion(form.nombre, form.email, form.mensaje)
    
#     return {
#         "mensaje": "Formulario enviado exitosamente. Se ha enviado un correo de verificación." 
#     }

from fastapi import FastAPI, HTTPException, status, Form
from pydantic import BaseModel, EmailStr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware 

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ContactForm(BaseModel):
    nombre: str
    apellidos: str
    email: EmailStr
    mensaje: str

def enviar_correo_verificacion(nombre: str, apellidos: str,email: str, mensaje: str):
    try:
        msg = MIMEMultipart()
        msg["From"] = SMTP_EMAIL
        msg["To"] = email
        msg["Subject"] = "Verificación de Contacto"

        # URL del logo de la empresa (cambiar por el enlace de tu logo)
        logo_url = "https://forreal360.com/wp-content/uploads/2022/02/for_real_img_12.png"

        # Contenido del correo con diseño mejorado y logo
        body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; color: #333;">
            <div style="width: 90%; max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #e0e0e0; border-radius: 8px; background-color: #f9f9f9;">
                
                <!-- Logo -->
                <div style="text-align: center; margin-bottom: 20px;">
                    <img src="{logo_url}" alt="Logo" style="width: 120px; height: auto;">
                </div>

                <h1 style="color: #2c3e50; text-align: center;">¡Hola, {nombre} {apellidos}!</h1>
                <p style="font-size: 16px; line-height: 1.6;">
                    Gracias por contactarnos. Hemos recibido tu mensaje y es un placer ayudarte. Aquí tienes una copia de tu mensaje:
                </p>
                <blockquote style="background-color: #eaf2f8; padding: 15px; border-left: 4px solid #3498db; margin: 10px 0; font-size: 14px;">
                    {mensaje}
                </blockquote>
                <p style="font-size: 16px; line-height: 1.6;">
                    Nos pondremos en contacto contigo lo antes posible. ¡Gracias por confiar en nosotros!
                </p>
                <div style="text-align: center; margin-top: 20px;">
                    <p style="font-size: 14px; color: #888;">&copy; 2024 Real View. Todos los derechos reservados.</p>
                </div>
            </div>
        </body>
        </html>
        """

        msg.attach(MIMEText(body, "html"))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_EMAIL, SMTP_PASSWORD)
            server.sendmail(SMTP_EMAIL, email, msg.as_string())

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al enviar el correo: {str(e)}"
        )

@app.post("/contacto")
async def enviar_formulario_contacto(form: ContactForm):
    enviar_correo_verificacion(form.nombre, form.apellidos, form.email, form.mensaje)
    
    return {
        "mensaje": "Formulario enviado exitosamente. Se ha enviado un correo de verificación." 
    }
