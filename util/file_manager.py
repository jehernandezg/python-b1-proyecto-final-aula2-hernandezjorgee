import pandas as pd

class CSVFileManager:
  def __init__(self, path: str):
    self.path = path

  def read(self):
    # Retorna un DataFrame de pandas
    return pd.read_csv(self.path)
  
  def write(self, dataFrame):
    # Opcional: Escribe el DataFrame a un CSV
    dataFrame.to_csv(self.path, index=False)