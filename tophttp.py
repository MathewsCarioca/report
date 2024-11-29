import pandas as pd

# Carregar o arquivo CSV
csv_file = "test-dataset.csv"  # Substitua pelo caminho do seu arquivo
data = pd.read_csv(csv_file)

# Filtrar somente tráfego HTTP
http_data = data[data['ClientRequestScheme'] == 'http']

# Exibir informações básicas do DataFrame filtrado
print(f"Total de linhas com tráfego HTTP: {len(http_data)}")
print(f"Colunas disponíveis: {http_data.columns.tolist()}")

# Função para obter os valores mais frequentes de uma coluna
def get_top_values(column_name, n=5):
    return http_data[column_name].value_counts().head(n)

# Colunas para análise
columns_to_analyze = [
    "ClientIP", "ClientRequestHost", "ClientRequestMethod", "ClientRequestURI",
    "EdgeStartTimestamp", "ZoneName", "ClientASN", "ClientCountry",
    "ClientDeviceType", "ClientSrcPort", "ClientRequestBytes", "ClientRequestPath",
    "ClientRequestReferer", "ClientRequestScheme", "ClientRequestUserAgent"
]

# Analisar e exibir os valores mais frequentes de cada coluna
for column in columns_to_analyze:
    print(f"\nTop valores para {column} (HTTP):")
    print(get_top_values(column))

# Salvar a análise em um arquivo CSV para relatório
output_file = "top_valores_http.csv"
top_values = {column: get_top_values(column).to_dict() for column in columns_to_analyze}
report_df = pd.DataFrame.from_dict(top_values, orient='index').transpose()
report_df.to_csv(output_file, index=False)

print(f"\nAnálise de tráfego HTTP salva em: {output_file}")
