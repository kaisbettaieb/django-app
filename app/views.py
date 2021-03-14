from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView

from django.views import View


class AccueilView(TemplateView):
    """
        La classe herite la classe générique TemplateView
        View basé sur une class
        l'url de cette vue est : /
        attr: template_name: string: Represente le nom du fichier html a afficher
        PS: Django cherche le dossier "templates" pour trouver les fichiers html
    """
    template_name = "accueil.html"


class MajDetails(View):
    """
    La classe herite la classe générique View
    l'url de cette vue : /update/email
    """
    def post(self, request, *args, **kwargs):
        """
        Cette fonction est envoquer quand une request POST a ete envoyé au url "/update/email"
        :param request:
        :return: la nouvelle adresse de l'utilisateur
                else:
                    erreur
        """
        if request.user.is_authenticated:
            email = request.POST.get("email")
            if email:
                request.user.email = email
                request.user.save()
                return JsonResponse(
                    {"status": "succes", "message": "Votre adresse mail a été bien changer.", "email": request.user.email},
                    content_type='application/json',status=200)

            else:
                return JsonResponse({"status": "erreur", "message": "Il faut preciser une nouvelle adresse mail."},
                                    content_type='application/json', status=500)
        return JsonResponse(
            {"status": "erreur", "message": "If faut se connecter pour pouvoir changer l'adresse mail."}, content_type='application/json', status=401)
