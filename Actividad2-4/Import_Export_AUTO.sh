cd 
cd Documents/Actividad2-4/

mongoexport --db=Agencia --collection=Automovil --type=csv --fields=Marca,SubMarca,Modelo,Version,Precio,Transmision,Carroceria,Puertas,Combustible,Motor,Llantas,PortaObjetos --out="Agencia-"`date +"%T-%d-%m-%y"`.csv


mongoexport --db=Magueyes --collection=Variedad --type=json --out="Magueyes-"`date +"%T-%d-%m-%y"`.json


mongoimport --db=AgenciaNueva --collection="Automovil-"`date +"%T-%d-%m-%y"` --type=csv --headerline --file="Agencia-"`date +"%T-%d-%m-%y"`.csv --ignoreBlanks

mongoimport --db=MagueyesNuevos --collection="Variedad-"`date +"%T-%d-%m-%y"`--type=json --file="Magueyes-"`date +"%T-%d-%m-%y"`.json


