# Odoo transportes
Módulo de odoo que permite gestionar camiones, conductores y los transportes que estos realizan.

## Instalación
1. Clonar el repositorio en el container de odoo. 
Esto nos dejará una carpeta llamada transportes, y dentro se encuentra toda la estructura de carpetas y archivos.
2. Añadir al addons path la ruta en la que ha sido clonado el repositorio. Por ejemplo, si ha sido clonado en _/opt/odoo/src_, esta es la ruta que se debe añadir al addons path.

## Cómo se usa
El módulo consta de tres modelos: camión, conductor y viaje.
Su principal funcionalidad es la de gestionar el transporte de mercancías.
Se requiere primero haber dado de alta algún producto ('product.product') en el módulo de ventas.

Una vez dados de alta camiones y conductores(modelo heredado de empleados) podremos crear un registro de viaje al cual asignaremos un camión, un conductor, un producto y un destino.

El viaje cuenta con un campo 'Entregado' el cual indica si el producto ya ha sido entregado o no. Para facilitar el control de cuales han sido entregados y cuales no cuenta con una vista kanban que agrupa los viajes en función de este campo.

 
## Elementos de interfaz
Los modelos viaje y camión cuentan con una vista formulario personalizada, mientras que el modelo conductor hereda la vista del formulario del modelo empleado.

Todos los modelos cuentan con una vista tree y el modelo viaje cuenta además con una vista kanban que agrupa los registros en funcion de si han sido entregados o no.


