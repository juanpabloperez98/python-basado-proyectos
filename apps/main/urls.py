from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('',views.home.as_view(),name = 'index'),
    path('teoria/',views.teoria_index.as_view(),name = 'teoria_index'),
    # Estructuras de secuencia
    path('estructuras-de-secuencia/',views.estructuras_de_secuencia.as_view(),name = 'estructuras_de_secuencia'),
    # Tipos de datos
    path('tipos_datos/',views.tipos_datos.as_view(),name = 'tipos_datos'),
    path('tipos-datos-numeros/',views.numeros.as_view(),name = 'numeros'),
    path('tipos-datos-secuencia/',views.secuencia.as_view(),name = 'secuencia'),
    # Ejemplos tipos-de-datos
    path('tipos-datos/ejemplo1/',views.ejemplo1_td.as_view(),name = 'ejemplo1-td'),
    path('tipos-datos/ejemplo2/',views.ejemplo2_td.as_view(),name = 'ejemplo2-td'),
    path('tipos-datos/ejemplo3/',views.ejemplo3_td.as_view(),name = 'ejemplo3-td'),
    path('tipos-datos/ejemplo4/',views.ejemplo4_td.as_view(),name = 'ejemplo4-td'),
    path('tipos-datos/ejemplo5/',views.ejemplo5_td.as_view(),name = 'ejemplo5-td'),
    path('tipos-datos/ejemplo6/',views.ejemplo6_td.as_view(),name = 'ejemplo6-td'),
    # Operadores
    path('operadores/',views.operadores.as_view(),name = 'operadores'),
    path('tipos-operadores/asignacion',views.tipos_operadores_asig.as_view(),name = 'tipos-operadores-asig'),
    path('tipos-operadores/aritmeticos',views.tipos_operadores_arit.as_view(),name = 'tipos-operadores-arit'),
    path('tipos-operadores/relacionales',views.tipos_operadores_rel.as_view(),name = 'tipos-operadores-rel'),
    # Ejemplos operadores
    path('operadores/ejemplo1/',views.ejemplo1_op.as_view(),name = 'ejemplo1-op'),
    path('operadores/ejemplo2/',views.ejemplo2_op.as_view(),name = 'ejemplo2-op'),
    path('operadores/ejemplo3/',views.ejemplo3_op.as_view(),name = 'ejemplo3-op'),
    path('operadores/ejemplo4/',views.ejemplo4_op.as_view(),name = 'ejemplo4-op'),
    path('operadores/ejemplo5/',views.ejemplo5_op.as_view(),name = 'ejemplo5-op'),
    path('operadores/ejemplo6/',views.ejemplo6_op.as_view(),name = 'ejemplo6-op'),

]
