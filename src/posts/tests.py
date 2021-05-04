from django.test import TestCase

# Create your tests here.
            <div class="extra content">
                <div class="mb-5">         
                </div>
                {% if obj.num_comments >= 1 %}
                <button class="cmt_btn ui button mb-5 SeeMore2">daha fazla göster</button>
                <div class="comment-box">
                {% if obj.comment_set.all %}
                    {% for c in obj.comment_set.all %}
                    
                        <div class="ui segment mb-5">
                            <img class="ui avatar image" src={{c.user.avatar.url}}>
                            <span>{{ c.user }}</span>
                            <div class='mt-5'>{{ c.body }}</div>
                        </div>
                    
                    {% endfor %}
                {% endif %}
                </div>
                {% endif %}


  
                <form action="" method="POST"class='ui fluid form'>
                    {% csrf_token %}
                    <input type="hidden" name="post_id" value={{obj.id}}>
                    {{ c_form.as_p }}
                    <button type="submit" name="submit_c_form" class="ui right floated button mt-5 w-full">Yorum Yap</button>
                </form>
            </div>



                        <div class="ui comments">
                            <div class="comment">
                                <a class="avatar">
                                    <img src={{c.author.avatar}}>
                                </a>
                                <div class="content">
                                <a class="author">{{c.author.user}}</a>
                                <div class="metadata">
                                    <span class="date">{{c.created}}</span>
                                </div>
                                <div class="text">
                                    {{c.body}}
                                </div>
                            </div>
                        </div>