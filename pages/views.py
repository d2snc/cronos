from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"
    
class InscricaoPageView(TemplateView):
    template_name = "inscricao.html"
    
class EventoPageView(TemplateView):
    template_name = "eventos.html"
    
class ConsultaAlunoPageView(TemplateView):
    template_name = "consulta_aluno.html"
    
class ConsultaTurmasPageView(TemplateView):
    template_name = "consulta_turmas.html"