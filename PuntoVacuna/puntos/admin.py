from django.contrib import admin
from .models import Usuario, Tipo_usuario, Comuna, Centro, Vacuna,DireccionC, DireccionU,Comentario,Vac_cen
# Register your models here.


admin.site.register(Usuario)
admin.site.register(Tipo_usuario)
admin.site.register(Comuna)
admin.site.register(Centro)
admin.site.register(Vacuna)
admin.site.register(DireccionC)
admin.site.register(DireccionU)
admin.site.register(Comentario)
admin.site.register(Vac_cen)
