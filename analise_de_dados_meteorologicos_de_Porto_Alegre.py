#Projeto Final de Lógica de Programação - Fase 2
#Análise de Dados Meteorológicos de Porto Alegre (1961-2016)

import calendar
from collections import defaultdict
from datetime import datetime

nome_dos_meses = (
    "", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
)

# FUNÇÃO 1: CARREGAR E TRATAR OS DADOS DO ARQUIVO
def carregar_dados(nome_arquivo):
    dados_carregados = []
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            # Pula a linha do cabeçalho
            next(arquivo)
            
            for linha_bruta in arquivo:
                # O separador é a vírgula (,)
                partes = linha_bruta.strip().split(',')
                if len(partes) == 8:
                    try:
                        # O formato da data é Dia/Mês/Ano (%d/%m/%Y)
                        data_objeto = datetime.strptime(partes[0], '%d/%m/%Y').date()
                        
                        precipitacao = float(partes[1]) if partes[1] else 0.0
                        temperatura_maxima = float(partes[2]) if partes[2] else 0.0
                        temperatura_minima = float(partes[3]) if partes[3] else 0.0
                        umidade_relativa = float(partes[6]) if partes[6] else 0.0
                        velocidade_vento = float(partes[7]) if partes[7] else 0.0
                        
                        dados_carregados.append({
                            'data': data_objeto,
                            'precipitacao': precipitacao,
                            'temperatura_maxima': temperatura_maxima,
                            'temperatura_minima': temperatura_minima,
                            'umidade_relativa': umidade_relativa,
                            'velocidade_vento': velocidade_vento,
                        })
                    except (ValueError, IndexError):
                        continue
    except FileNotFoundError:
        print(f" ERRO CRÍTICO: Arquivo '{nome_arquivo}' não encontrado.")
        print("   Por favor, verifique se ele está na mesma pasta que o seu programa (.py).")

    return dados_carregados

# FUNÇÃO 2: VISUALIZAR DADOS POR INTERVALO
def visualizar_dados_periodo(dados, data_inicio_str, data_fim_str, opcao_visualizacao):
    """Exibe os dados filtrados por um intervalo de datas e opção do usuário."""
    try:
        data_inicio_corrigida = data_inicio_str.replace('-', '/')
        data_fim_corrigida = data_fim_str.replace('-', '/')

        inicio_mes, inicio_ano = map(int, data_inicio_corrigida.split('/'))
        fim_mes, fim_ano = map(int, data_fim_corrigida.split('/'))
        
        data_inicio = datetime(inicio_ano, inicio_mes, 1).date()
        ultimo_dia_mes_final = calendar.monthrange(fim_ano, fim_mes)[1]
        data_fim = datetime(fim_ano, fim_mes, ultimo_dia_mes_final).date()

    except ValueError:
        print("\n ERRO: Formato de data inválido. Use MM/AAAA (ex: 07/2010 ou 07-2010).")
        return

    print("\n" + "="*70)
    print(f" Exibindo Dados de {data_inicio_str} a {data_fim_str}")
    print("="*70)

    dados_encontrados = False
    for registro in dados:
        if data_inicio <= registro['data'] <= data_fim:
            dados_encontrados = True
            data_formatada = registro['data'].strftime('%d/%m/%Y')
            
            if opcao_visualizacao == '1':
                print(f"{data_formatada} | Precip: {registro['precipitacao']:.1f}mm | Max: {registro['temperatura_maxima']:.1f}°C | Min: {registro['temperatura_minima']:.1f}°C | Umid: {registro['umidade_relativa']:.1f}% | Vento: {registro['velocidade_vento']:.2f}m/s")
            elif opcao_visualizacao == '2':
                print(f"{data_formatada} - Precipitação: {registro['precipitacao']:.1f} mm")
            elif opcao_visualizacao == '3':
                print(f"{data_formatada} - Temp. Máxima: {registro['temperatura_maxima']:.1f}°C / Temp. Mínima: {registro['temperatura_minima']:.1f}°C")
            elif opcao_visualizacao == '4':
                print(f"{data_formatada} - Umidade Relativa: {registro['umidade_relativa']:.1f}% / Vel. Vento: {registro['velocidade_vento']:.2f} m/s")
    
    if not dados_encontrados:
        print("Nenhum dado encontrado para o período e filtro selecionados.")

# FUNÇÃO 3: MÊS MAIS CHUVOSO
def encontrar_mes_mais_chuvoso(dados):
    """Calcula o mês/ano com a maior precipitação acumulada em todo o período."""
    if not dados:
        print("Não há dados para analisar.")
        return

    chuva_por_mes = defaultdict(float)
    for registro in dados:
        chave_ano_mes = registro['data'].strftime('%Y-%m')
        chuva_por_mes[chave_ano_mes] += registro['precipitacao']
    
    if not chuva_por_mes:
        print("Não foi possível calcular a precipitação por mês.")
        return
        
    mais_chuvoso_aaaa_mm = max(chuva_por_mes, key=chuva_por_mes.get)
    
    ano, mes = mais_chuvoso_aaaa_mm.split('-')
    mais_chuvoso_mm_aaaa = f"{mes}/{ano}"
    
    print("\n" + "="*50)
    print("Mês mais chuvoso (1961-2016)")
    print("="*50)
    print(f"O mês com maior volume de chuva foi {mais_chuvoso_mm_aaaa}.")
    print(f"Total de Precipitação: {chuva_por_mes[mais_chuvoso_aaaa_mm]:.2f} mm")
    print("="*50)

# FUNÇÃO 4: MÉDIA DE TEMPERATURA MÍNIMA (2006-2016)
def calcular_media_temp_minima(dados, mes_analise):
    """Calcula a média de temperatura mínima para um dado mês entre os anos de 2006 e 2016."""
    somas_por_ano = defaultdict(float)
    contagem_por_ano = defaultdict(int)

    for registro in dados:
        if 2006 <= registro['data'].year <= 2016 and registro['data'].month == mes_analise:
            ano = registro['data'].year
            somas_por_ano[ano] += registro['temperatura_minima']
            contagem_por_ano[ano] += 1
            
    medias_anuais = {}
    for ano in range(2006, 2017):
        if contagem_por_ano[ano] > 0:
            media = somas_por_ano[ano] / contagem_por_ano[ano]
            medias_anuais[ano] = media
            
    return medias_anuais

# FUNÇÃO 5: GRÁFICO TEXTUAL
def gerar_grafico_textual(medias, mes_analise):
    """Gera um gráfico de barras textual com as médias de temperatura."""
    nome_mes = nome_dos_meses[mes_analise]
    
    print("\n" + "="*60)
    print(f" Gráfico de Temp. Mínima Média para {nome_mes} (2006-2016)")
    print("="*60)

    if not medias:
        print("Sem dados para exibir no gráfico.")
        return

    valor_maximo = max(medias.values()) if medias else 1
    # Evita divisão por zero se o valor máximo for 0
    escala = 40 / valor_maximo if valor_maximo > 0 else 0

    for ano, valor in sorted(medias.items()):
        barras = '█' * int(valor * escala)
        print(f"{ano} | {barras} ({valor:.2f}°C)")
        print()

# FUNÇÃO 6: MÉDIA GERAL DO PERÍODO
def calcular_media_geral(medias, mes_analise):
    """Calcula a média geral das temperaturas mínimas a partir do dicionário de médias anuais."""
    if medias:
        nome_mes = nome_dos_meses[mes_analise]
        media_total = sum(medias.values()) / len(medias)
        print("\n" + "="*60)
        print(f" Média Geral da Temp. Mínima para {nome_mes} (2006-2016): {media_total:.2f}°C")
        print("="*60)

# FUNÇÃO PRINCIPAL (MENU)
def executar_programa_principal():
    """Função principal que executa o menu e chama as outras funções."""
    arquivo_csv = 'Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv'
    dados_meteorologicos = carregar_dados(arquivo_csv)

    if not dados_meteorologicos:
        print("\nPrograma encerrado por falha no carregamento dos dados.")
        return

    print(f"\nCarga de dados concluída! {len(dados_meteorologicos)} registros válidos foram carregados.")

    while True:
        print("\n" + "===== MENU DE ANÁLISE METEOROLÓGICA =====".center(50))
        print("1 - Visualizar dados por período")
        print("2 - Exibir mês mais chuvoso de toda a série histórica")
        print("3 - Analisar temperatura mínima de um mês (2006–2016)")
        print("0 - Sair")
        print("="*51)
        
        opcao_menu = input("Digite a sua escolha: ")

        if opcao_menu == '1':
            data_inicio_str = input("   > Digite o mês/ano inicial (formato MM/AAAA): ")
            data_fim_str = input("   > Digite o mês/ano final (formato MM/AAAA): ")
            print("     Opções de visualização:")
            print("     1 - Todos os dados")
            print("     2 - Apenas Precipitação")
            print("     3 - Apenas Temperaturas")
            print("     4 - Apenas Umidade e Vento")
            tipo_dado = input("   > Escolha o tipo de dado: ")
            
            if tipo_dado not in ['1', '2', '3', '4']:
                print("\n ERRO: Opção de tipo de dado inválida. Tente novamente.")
                continue
            visualizar_dados_periodo(dados_meteorologicos, data_inicio_str, data_fim_str, tipo_dado)

        elif opcao_menu == '2':
            encontrar_mes_mais_chuvoso(dados_meteorologicos)

        elif opcao_menu == '3':
            try:
                mes_digitado_str = input("   > Digite o número do mês para análise (1-12): ")
                mes_selecionado = int(mes_digitado_str)
                if not 1 <= mes_selecionado <= 12:
                    print("\n ERRO: Mês deve ser um número entre 1 e 12.")
                    continue
            except ValueError:
                print("\n ERRO: Entrada inválida. Por favor, digite um número.")
                continue
            
            medias_por_ano = calcular_media_temp_minima(dados_meteorologicos, mes_selecionado)
            if not medias_por_ano:
                print(f"\nNão foram encontrados dados de temperatura mínima para o mês {mes_selecionado} no período de 2006 a 2016.")
            else:
                gerar_grafico_textual(medias_por_ano, mes_selecionado)
                calcular_media_geral(medias_por_ano, mes_selecionado)

        elif opcao_menu == '0':
            print("\n Obrigado por utilizar o sistema de análise de dados meteorológicos de Porto Alegre (1961-2016)")
            break
        else:
            print("\n ERRO: Opção inválida. Por favor, escolha uma das opções do menu.")

if __name__ == "__main__":
    executar_programa_principal()