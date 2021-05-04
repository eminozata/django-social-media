from django.test import TestCase
{% extends 'base.html' %}

{% block title %}
istekler
{% endblock title %}

{% block content %}

    {%if is_empty%}
        <h2>Gelen istek yok :(</h2>
    {%endif%}

    {%for obj in qs%}
        <div class="ui segment">
            <div class="ui grid">
                <div class="row">
                    <div class="three wide column">
                        <img src={{obj.avatar.url}} class="ui small circular image" >
                    </div>
                    <div class="thirteen wide column">
                        <h3>{{obj.user}}</h3>
                        <p>{{obj.bio}}</p>
                        <br>
                        <a href={{obj.get_absolute_url}}>
                            <button class="ui primary button w-big mb-5">Profili Gör</button>
                        </a>
                        <form action="{% url 'profiles:accept-invite' %}" method="POST">
                            {% csrf_token %}
                            <input type="hidden" name="profile_pk" value={{obj.pk}}>
                            <button type="submit" class="ui positive basic button w-big mb-5"><i class="check icon"></i>
                                Onayla
                            </button>
                        </form>
                        <form action="{% url 'profiles:reject-invite' %}" method="POST">
                            {% csrf_token %}
                            <input type="hidden" name="profile_pk" value={{obj.pk}}>
                            <button type="submit" class="ui negative basic button w-big mb-5"><i class="close icon"></i>
                                Sil
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    {%endfor%}


{% endblock content %}