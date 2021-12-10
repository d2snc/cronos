from django.urls import path

from . import views


app_name = "pages"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("inscricaomateria/",views.InscricaoPageView.as_view(), name="inscricaomateria"),
    path("eventos/",views.EventoPageView.as_view(), name="eventos"),
    path("consulta_aluno/",views.ConsultaAlunoPageView.as_view(), name="consulta_aluno"),
    path("consulta_turmas/",views.ConsultaTurmasPageView.as_view(), name="consulta_turmas")
]