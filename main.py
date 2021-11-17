import typer
import pandas as pd
from enum import Enum


class FileFormat(Enum):
    parquet = 'parquet'
    json = 'json'


app = typer.Typer()


@app.command()
def generate(file_name: str, file_format: FileFormat):
    typer.echo(f"Gerando arquivo {file_name} no format {file_format.value}")
    
    try:
        df = pd.read_excel('files/base_populacao_idhm.xls')
        getattr(df, f'to_{file_format.value}')(file_name, orient='records')
    except Exception as err:
        typer.echo(f"Problema ao gerar o arquivo: {err}")
    
    typer.echo(f"Arquivo gerado com sucesso.")


if __name__ == "__main__":
    app()
