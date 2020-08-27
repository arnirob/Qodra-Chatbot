
      function createRowUser(text) {
        $chatlog = $('#chatlog');
        var $row = $('<div class="row p-1"><div class="col-sm-12 text-right pt-3"><p class="h-chat"> <span>'+ text +'</span> </p></div></div>');

        // $row.text(text);
        $chatlog.append($row);
      }

       function createRowBot(text) {
        $chatlog = $('#chatlog');
        var $row = $('<div class="row p-1"> <div class="col-sm-1"><img src="{% static "img/bot (1).svg" %}" alt="" class="img-fluid boot-image"> </div><div class="col-sm-11"><p class="bot-chat"><span>'+text+'</span> </p></div></div>');

        // $row.text(text);
        $chatlog.append($row);
      }

      function makeReq(chatterbotUrl, statement, token ){
        $.ajax({
              type: 'POST',
              url: chatterbotUrl,
              data: {
                statement : statement,
                csrfmiddlewaretoken: token,
              },
              success: function(gotIt,status){
               console.log(gotIt)
                var cmd = "";
                createRowBot(gotIt['text']);

              },
              error : function(){
                alert('Console');
              }
            })
      }

     

      $(document).ready(function(e){

          $("#train").click(function(e){
            e.preventDefault();
            var chatterbotUrl = '{% url "chatterbot" %}';
            var token = '{{csrf_token}}';
            var statement = $("#statement").val();
            $("#statement").val("");
            createRowUser(statement);
            // console.log(statement);
            makeReq(chatterbotUrl,statement,token);

          });

          $('#statement').keypress(function(e){
            if(e.which == 13){//Enter key pressed
                $('#train').click();//Trigger search button click event
            }
          });

        });
