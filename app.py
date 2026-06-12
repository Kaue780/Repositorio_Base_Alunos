import streamlit as st

st.sidebar.title("Calculadora de IMC")
st.sidebar.image("imagem.png")



#--------------------- BODY
st.title("Calculadora de IMC")

peso = st.text_input("DIgite seu peso: ")
altura = st.text_input("Digite sua altura: ")

if st.button("Calcular"):
    peso = float(peso)
    altura = float(altura)

    imc = peso / (altura ** 2)

    if imc < 18.5:
        class_imc = "Abaixo_peso"
        st.warning(f"Seu imc é {imc:.2f}. Você está abaixo do peso!")

    elif imc < 24.9:
        class_imc = "Peso_saudavel"
        st.success(f"Seu imc é {imc:.2f}. Você está abaixo do peso ideal: Parabens")

    elif imc < 29.9:
        class_imc = "Sobrepeso"
        st.warning(f"Seu IMC é {imc:.2f}. Você está com sobrepeso!")

    elif imc < 34.9:
        class_imc = "Obesidade_1"
        st.warning(f"Seu IMC é {imc:.2f}. Você está com obesidade GRAU 1!")

    elif imc < 39.9:
        class_imc = "Obesidade_2"
        st.error(f"Seu IMC é {imc:.2f}. Você está com obesidade GRAU 2!")

    else:
        class_imc = "Obesidade_3"
        st.error(f"Seu IMC é {imc:.2f}. Você está com obesidade GRAU 3!")

    
    st.markdown("---")

    with open(f"{class_imc}.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()

    st.markdown(conteudo)