import streamlit as st
st.title('Experimentos con inversión en mapudungun')

# página 116 del [libro de Zúñiga](https://www.cepchile.cl/cep/site/docs/20160304/20160304094227/libro_Mapudungun_Fernando-Zuniga.pdf)

## sufijos de inversión

def sufijo_inversion(persona_sujeto,persona_objeto):
    if persona_sujeto == 'tercera' and (persona_objeto == 'primera' or persona_objeto == 'segunda'):
        return 'e','mew'
    elif (persona_sujeto == 'primera' or persona_sujeto == 'segunda') and persona_objeto == 'tercera':
        return 'fi',''
    else:
        return '',''

## diccionario de modo-persona-número

indicativo_persona_inv = {}
##
indicativo_persona_inv['primera'] = {'tercera':{'singular':'ñ', 'dual':'yu', 'plural':'yiñ'}}
indicativo_persona_inv['segunda'] = {'tercera':{'singular':'mi', 'dual':'mu', 'plural':'mün'}}
##
indicativo_persona_inv['tercera'] = {'primera':{'singular':'n', 'dual':'yu', 'plural':'iñ'},
                                     'segunda':{'singular':'y', 'dual':'ymu', 'plural':'ymün'}}

## morfemas de inversión

def inversion(verbo, persona_sujeto, numero, polaridad, persona_objeto):
    ## ¿está correcto este orden? :O
    return verbo + sufijo_polaridad(polaridad) + sufijo_inversion(persona_sujeto,persona_objeto)[0] + indicativo_persona_inv[persona_sujeto][persona_objeto][numero] + sufijo_inversion(persona_sujeto,persona_objeto)[1]

## probamos todo para un verbo
verbo = 'leli'#'leli' ## mirar
persona_objeto = 'primera'
persona_sujeto = 'tercera'
numero = 'plural'
polaridad = 'positiva'

inversion(verbo, persona_sujeto, numero, polaridad, persona_objeto)

verbo = st.text_input('verbo:', 'leli')
persona_sujeto = st.selectbox('¿Cuál es la persona sujeto?', ['primera', 'segunda', 'tercera'], index=0)
persona_objeto = st.selectbox('¿Cuál es la persona del objeto?', ['primera', 'segunda', 'tercera'], index=0)
numero = st.selectbox('¿Cuántos participan en el sujeto? (número)', ['singular', 'dual', 'plural'], index=0)
polaridad = st.selectbox('polaridad', ['positiva','negativa'], index=1)

st.write(inversion(verbo, persona_sujeto, numero, polaridad, persona_objeto))