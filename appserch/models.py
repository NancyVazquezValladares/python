from django.db import models

class Empleado(models.Model):
    nombre=models.CharField(max_length=100,null=False,verbose_name='Nombre de Empleado')
    rol=models.CharField(max_length=100,null=False,verbose_name='Roll Empleado')
    fecha_creacion=models.DateField(auto_now_add=True,verbose_name='Fecha creacion')
    fecha_actualizacion=models.DateField(auto_now=True,verbose_name='Fecha actualizacion')

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table='empleado'
        ordering=['id']
        
class Caja(models.Model):
    saldo_inicial = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name='Saldo inicial')
    saldo_final = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name='Saldo Final')
    id_Empleado = models.ForeignKey(Empleado, null=True, blank=True,verbose_name='ID Empleado',on_delete=models.CASCADE)
    fecha_creacion=models.DateField(auto_now_add=True,verbose_name='Fecha creacion')
    fecha_actualizacion=models.DateField(auto_now=True,verbose_name='Fecha actualizacion')
    
    def __str__(self):
        return str(self.saldo_final)
    
    class Meta:
        db_table='caja'
        ordering = ['id']
        
class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=100, null=False, verbose_name='Nombre del Cliente')
    telefono = models.CharField(max_length=100, null=False, verbose_name='Telefono')
    correo_cliente = models.CharField(max_length=100, null=False, verbose_name='Correo Electronico')
    direccion = models.CharField(max_length=100, null=False, verbose_name='Direccion')
    fecha_creacion=models.DateField(auto_now_add=True,verbose_name='Fecha creacion')
    fecha_actualizacion=models.DateField(auto_now=True,verbose_name='Fecha actualizacion')
    
    def __str__(self):
        return self.nombre_cliente
    
    class Meta:
        db_table='cliente'
        ordering=['id']
        
class Producto(models.Model):
    descripcion = models.CharField(max_length=100, null=False, verbose_name='Descripcion')
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name='precio')
    stock = models.IntegerField(null=False, verbose_name='Stock')
    fecha_creacion=models.DateField(auto_now_add=True,verbose_name='Fecha creacion')
    fecha_actualizacion=models.DateField(auto_now=True,verbose_name='Fecha actualizacion')
    
    def __str__(self):
        return self.descripcion
    
    class Meta:
        db_table = 'producto'
        ordering = ['id']
        
class Venta(models.Model):
    fecha = models.DateTimeField(null=False, verbose_name='Fecha')
    cantidad = models.IntegerField(null=False, verbose_name='Cantidad')
    id_empleado = models.ForeignKey(Empleado, null=True,blank=False,on_delete=models.CASCADE, verbose_name='ID Empleado')
    id_producto = models.ForeignKey(Producto, null=True, blank=False,on_delete=models.CASCADE, verbose_name='ID Producto')
    fecha_creacion=models.DateField(auto_now_add=True,verbose_name='Fecha creacion')
    fecha_actualizacion=models.DateField(auto_now=True,verbose_name='Fecha actualizacion')
    
    def __str__(self):
        return str(self.fecha)
    
    class Meta:
        db_table = 'venta'
        ordering = ['id']
        
class DetalleVenta(models.Model):
    producto = models.CharField(max_length=100, null=False, verbose_name='Producto')
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name='Precio')
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name='Total')
    monto = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name='Monto')
    resto = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name='Resto')
    id_venta = models.ForeignKey(Venta, null=True, blank=False,on_delete=models.CASCADE, verbose_name='ID Venta')
    id_cliente = models.ForeignKey(Cliente, null=True, blank=False,on_delete=models.CASCADE, verbose_name='ID Cliente')
    fecha_creacion=models.DateField(auto_now_add=True,verbose_name='Fecha creacion')
    fecha_actualizacion=models.DateField(auto_now=True,verbose_name='Fecha actualizacion')
    
    def __str__(self):
        return self.producto
    
    class Meta:
        db_table='detalleventa'
        ordering=['id']
        
class Descuento(models.Model):
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name='Porcentaje')
    id_producto = models.ForeignKey(Producto, null=True, blank=False,on_delete=models.CASCADE, verbose_name='ID Producto')
    fecha_creacion=models.DateField(auto_now_add=True,verbose_name='Fecha creacion')
    fecha_actualizacion=models.DateField(auto_now=True,verbose_name='Fecha actualizacion')
    
    def __str__(self):
        return str(self.porcentaje)
    
    class Meta:
        db_table='descuento'
        ordering=['id']
        
class Marca(models.Model):
    nombre_marca = models.CharField(max_length=100, null=False, verbose_name='Nombre')
    id_producto = models.ForeignKey(Producto, null=True, blank=False,on_delete=models.CASCADE, verbose_name='ID Producto')
    fecha_creacion=models.DateField(auto_now_add=True,verbose_name='Fecha creacion')
    fecha_actualizacion=models.DateField(auto_now=True,verbose_name='Fecha actualizacion')
    
    def __str__(self):
        return self.nombre_marca
    
    class Meta:
        db_table='marca'
        ordering=['id']
        
class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=100, null=False, verbose_name='Nombre Proveedor')
    contacto = models.CharField(max_length=100, null=False, verbose_name='Contacto')
    id_marca = models.ForeignKey(Marca, null=True, blank=False,on_delete=models.CASCADE, verbose_name='ID Marca')
    fecha_creacion=models.DateField(auto_now_add=True,verbose_name='Fecha creacion')
    fecha_actualizacion=models.DateField(auto_now=True,verbose_name='Fecha actualizacion')
    
    def __str__(self):
        return self.nombre_proveedor
    
    class Meta:
        db_table='proveedor'
        ordering=['id']
        
class Pedido(models.Model):
    fecha_pedido = models.DateTimeField(null=False, verbose_name='Fecha de pedido')
    fecha_entrega = models.DateTimeField(null=False, verbose_name='Fecha de entrega')
    id_proveedor = models.ForeignKey(Proveedor, null=True, blank=False,on_delete=models.CASCADE, verbose_name='ID Proveedor')
    fecha_creacion=models.DateField(auto_now_add=True,verbose_name='Fecha creacion')
    fecha_actualizacion=models.DateField(auto_now=True,verbose_name='Fecha actualizacion')
    
    def __str__(self):
        return str(self.fecha_pedido)
    
    class Meta:
        db_table='pedido'
        ordering=['id']
        

