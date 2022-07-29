from flask import Flask,render_template,request
import funcoes

# Criar o site
app = Flask(__name__)

# Página inicial
@app.route('/')
@app.route('/home', methods=['POST','GET'])
# Definir a pagina inicial, chamando o arquivo html
def homepage():
    return render_template('homepage.html')

# As páginas podem ser acessadas pelo botão criado (POST) e pela digitação na barra de endereço (GET)
@app.route('/factsheets', methods=['POST','GET'])
def familia():
    #familia = input('Qual a familia?')
    return render_template('factsheets.html')

@app.route('/mapa', methods=['POST','GET'])
def mapa():
    return render_template('familia/Acaridae/mapa_Acaridae.html')

# Página com a equipe do laboratório
@app.route('/equipe', methods=['POST','GET'])
def equipe():
    return render_template('equipe.html')

# 
@app.route('/tabela', methods=['POST','GET'])
def tabela():
    return render_template('tabela1.html')

# 
@app.route('/formulario', methods=['POST','GET'])
def formulario():
    return render_template('formulario/formulario.html')

@app.route('/confirma_formulario', methods=['POST'])
def confirma_formulario():
    #Definir uma variável a partir do que foi preenchido anteriormente para ser mostrada
    tombo = funcoes.itens('tombo')
    titulo_lista = funcoes.itens('titulo_lista')
    instituicao = funcoes.itens('instituicao')
    id_taxon = funcoes.itens('id_taxon')
    nome_cientifico = funcoes.itens('nome_cientifico')
    nivel_taxon = funcoes.itens('nivel_taxon')
    autor_especie = funcoes.itens('autor_especie')
    reino = funcoes.itens('reino')
    filo = funcoes.itens('filo')
    classe = funcoes.itens('classe')
    ordem = funcoes.itens('ordem')
    familia = funcoes.itens('familia')
    genero = funcoes.itens('genero')
    sub_genero = funcoes.itens('sub_genero')
    espiteto_especifico = funcoes.itens('espiteto_especifico')
    subespecie = funcoes.itens('subespecie')
    nome_vernacular = funcoes.itens('nome_vernacular')
    observacoes = funcoes.itens('observacoes')
    status_taxon = funcoes.itens('status_taxon')
    status_ameaca = funcoes.itens('status_ameaca')
    definicao_status = funcoes.itens('definicao_status')
    criterios = funcoes.itens('criterios')
    data_coleta = funcoes.itens('data_coleta')
    localidade = funcoes.itens('localidade')
    estado = funcoes.itens('estado')
    licenca = funcoes.itens('licenca')
    titular_direitos = funcoes.itens('titular_direitos')
    informacao_retida = funcoes.itens('informacao_retida')
    latitude = funcoes.itens('latitude')
    longitude = funcoes.itens('longitude')

    #escreve os dados nas tabelas
    variaveis = funcoes.escrever_dados()

    return render_template('formulario/confirma_formulario.html',tombo=tombo,titulo_lista=titulo_lista,
    instituicao = instituicao,id_taxon = id_taxon,nome_cientifico = nome_cientifico,nivel_taxon = nivel_taxon,
    autor_especie = autor_especie,reino = reino,filo = filo,classe = classe,ordem = ordem,familia = familia,genero = genero,
    sub_genero = sub_genero,espiteto_especifico = espiteto_especifico,subespecie = subespecie,nome_vernacular = nome_vernacular,
    observacoes = observacoes,status_taxon = status_taxon,status_ameaca = status_ameaca,definicao_status = definicao_status,
    criterios = criterios,data_coleta = data_coleta,localidade = localidade,estado = estado,licenca = licenca,
    titular_direitos = titular_direitos,informacao_retida = informacao_retida,latitude = latitude,longitude = longitude)

@app.route('/factsheets',methods=['GET','POST'])
def factsheets():
    return render_template('factsheets.html')

@app.route('/login',methods=['GET','POST'])
def login():
    pass

# Para o site continuar rodando
if __name__ == '__main__':
    app.run(debug=True)