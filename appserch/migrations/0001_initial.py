# Generated by Django 4.2.7 on 2023-11-22 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=100, verbose_name='Nombre del Cliente')),
                ('telefono', models.CharField(max_length=100, verbose_name='Telefono')),
                ('correo_cliente', models.CharField(max_length=100, verbose_name='Correo Electronico')),
                ('direccion', models.CharField(max_length=100, verbose_name='Direccion')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('fecha_actualizacion', models.DateField(auto_now=True, verbose_name='Fecha actualizacion')),
            ],
            options={
                'db_table': 'cliente',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de Empleado')),
                ('rol', models.CharField(max_length=100, verbose_name='Roll Empleado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('fecha_actualizacion', models.DateField(auto_now=True, verbose_name='Fecha actualizacion')),
            ],
            options={
                'db_table': 'empleado',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_marca', models.CharField(max_length=100, verbose_name='Nombre')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('fecha_actualizacion', models.DateField(auto_now=True, verbose_name='Fecha actualizacion')),
            ],
            options={
                'db_table': 'marca',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripcion')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='precio')),
                ('stock', models.IntegerField(verbose_name='Stock')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('fecha_actualizacion', models.DateField(auto_now=True, verbose_name='Fecha actualizacion')),
            ],
            options={
                'db_table': 'producto',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(verbose_name='Fecha')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('fecha_actualizacion', models.DateField(auto_now=True, verbose_name='Fecha actualizacion')),
                ('id_empleado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appserch.empleado', verbose_name='ID Empleado')),
                ('id_producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appserch.producto', verbose_name='ID Producto')),
            ],
            options={
                'db_table': 'venta',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proveedor', models.CharField(max_length=100, verbose_name='Nombre Proveedor')),
                ('contacto', models.CharField(max_length=100, verbose_name='Contacto')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('fecha_actualizacion', models.DateField(auto_now=True, verbose_name='Fecha actualizacion')),
                ('id_marca', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appserch.marca', verbose_name='ID Marca')),
            ],
            options={
                'db_table': 'proveedor',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateTimeField(verbose_name='Fecha de pedido')),
                ('fecha_entrega', models.DateTimeField(verbose_name='Fecha de entrega')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('fecha_actualizacion', models.DateField(auto_now=True, verbose_name='Fecha actualizacion')),
                ('id_proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appserch.proveedor', verbose_name='ID Proveedor')),
            ],
            options={
                'db_table': 'pedido',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='marca',
            name='id_producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appserch.producto', verbose_name='ID Producto'),
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=100, verbose_name='Producto')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Monto')),
                ('resto', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Resto')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('fecha_actualizacion', models.DateField(auto_now=True, verbose_name='Fecha actualizacion')),
                ('id_cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appserch.cliente', verbose_name='ID Cliente')),
                ('id_venta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appserch.venta', verbose_name='ID Venta')),
            ],
            options={
                'db_table': 'detalleventa',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Descuento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Porcentaje')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('fecha_actualizacion', models.DateField(auto_now=True, verbose_name='Fecha actualizacion')),
                ('id_producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appserch.producto', verbose_name='ID Producto')),
            ],
            options={
                'db_table': 'descuento',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo_inicial', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Saldo inicial')),
                ('saldo_final', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Saldo Final')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('fecha_actualizacion', models.DateField(auto_now=True, verbose_name='Fecha actualizacion')),
                ('id_Empleado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appserch.empleado', verbose_name='ID Empleado')),
            ],
            options={
                'db_table': 'caja',
                'ordering': ['id'],
            },
        ),
    ]