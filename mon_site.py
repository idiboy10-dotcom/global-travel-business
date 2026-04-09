import streamlit as st
import pandas as pd
import os

# Configuration
st.set_page_config(page_title="Global Travel Business", page_icon="🌍", layout="wide")

# 🌈 Style global premium
st.markdown("""
<style>
.stApp {
    background-color: #0D1B2A;
    color: #EAEAEA;
    font-family: 'Poppins', sans-serif;
}
.card {
    background-color: #1B263B;
    border: 1px solid #FFD700;
    border-radius: 10px;
    padding: 15px;
    text-align: center;
    color: white;
    box-shadow: 0px 4px 8px rgba(0,0,0,0.3);
    transition: all 0.4s ease;
}
.card:hover {
    transform: scale(1.05);
    box-shadow: 0px 0px 20px #FFD700;
    border-color: #FFFACD;
}
.card img {
    border-radius: 10px;
    width: 100%;
    height: 200px;
    object-fit: cover;
}
hr {
    border: 1px solid #FFD700;
    margin: 20px 0;
}
</style>
""", unsafe_allow_html=True)

# 🛫 Header avec logo et nom de l'agence
col1, col2 = st.columns([1,4])

with col1:
    st.image("https://copilot.microsoft.com/th/id/BCO.1abd4eb7-c210-444e-9995-fe207381e73f.png", width=120)

with col2:
    st.title("🌍 Global Travel Business")  # ✅ affichage garanti
    st.subheader("Agence de voyages internationale")

st.markdown("<hr>", unsafe_allow_html=True)

# 📍 Destinations phares
st.markdown("## ✨ Destinations phares")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.image("https://copilot.microsoft.com/th/id/BCO.96665664-85f0-4896-b229-8cde6dd9572c.png", caption="Île de Gorée - Sénégal")
    st.write("Patrimoine historique et culturel")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.image("https://copilot.microsoft.com/th/id/BCO.65cc51bf-567d-434e-a9ad-27ef44b7553f.png", caption="Safari au Kenya")
    st.write("Aventure et nature sauvage")
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.image("https://copilot.microsoft.com/th/id/BCO.d4e22f58-5b28-4ef3-a466-b2250dc188cf.png", caption="Paris - France")
    st.write("Romance et culture européenne")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# 🎁 Offres spéciales harmonisées
st.markdown("## 🎁 Offres spéciales")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.image("https://copilot.microsoft.com/th/id/BCO.b49965a6-1fa0-4f30-b603-758dea7630b0.png", caption="Séjour à Gorée", use_column_width=True)
    st.markdown("<h3 style='color:#FFD700;'>Durée : 2 jours</h3>", unsafe_allow_html=True)
    st.markdown("<p>Prix : <b>150 000 FCFA</b> — <span style='color:#00FF00;'>-10% Promo</span></p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.image("https://copilot.microsoft.com/th/id/BCO.466b2b27-2fbd-47dc-8020-3351cb4c6a6f.png", caption="Safari au Kenya", use_column_width=True)
    st.markdown("<h3 style='color:#FFD700;'>Durée : 5 jours</h3>", unsafe_allow_html=True)
    st.markdown("<p>Prix : <b>450 000 FCFA</b> — <span style='color:#FF5733;'>-15% Promo</span></p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.image("https://copilot.microsoft.com/th/id/BCO.eed0e176-86fd-429a-9b6b-8897208ec6d3.png", caption="Séjour à Paris", use_column_width=True)
    st.markdown("<h3 style='color:#FFD700;'>Durée : 3 jours</h3>", unsafe_allow_html=True)
    st.markdown("<p>Prix : <b>600 000 FCFA</b> — <span style='color:#3498DB;'>-5% Promo</span></p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.info("✨ Profitez de ces offres limitées en réservant dès maintenant !")

st.markdown("<hr>", unsafe_allow_html=True)

# 📝 Formulaire de réservation
st.markdown("## 📝 Réservation en ligne")
with st.form("reservation_form"):
    nom = st.text_input("Nom complet")
    email = st.text_input("Adresse e-mail")
    destination = st.selectbox("Choisissez votre destination", ["Île de Gorée - Sénégal", "Safari au Kenya", "Paris - France"])
    message = st.text_area("Message ou demande spéciale")
    envoyer = st.form_submit_button("Envoyer la réservation")

    if envoyer:
        reservation = {"Nom": nom, "Email": email, "Destination": destination, "Message": message}
        fichier = "reservations.csv"

        if os.path.exists(fichier):
            df = pd.read_csv(fichier)
            df = pd.concat([df, pd.DataFrame([reservation])], ignore_index=True)
        else:
            df = pd.DataFrame([reservation])

        df.to_csv(fichier, index=False)
        st.success(f"Merci {nom} ! Votre demande pour **{destination}** a bien été enregistrée. Nous vous contacterons à **{email}** sous peu.")

st.markdown("<hr>", unsafe_allow_html=True)

# 📋 Liste des réservations (sans graphique)
st.markdown("## 📋 Liste des réservations")
fichier = "reservations.csv"
if os.path.exists(fichier):
    df = pd.read_csv(fichier)
    st.dataframe(df)
else:
    st.warning("⚠️ Aucune réservation enregistrée pour le moment.")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>📞 Contactez-nous sur WhatsApp | 🌐 Suivez-nous sur Instagram</p>", unsafe_allow_html=True)
