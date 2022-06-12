from black import out
import gdown

url = "https://drive.google.com/file/d/1fVEgtlZs37j01xuU63qlJcVndHj8IRsl/view?usp=sharing"
output="file.zip"
gdown.download(url, output, quiet=False)