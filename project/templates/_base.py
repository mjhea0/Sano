<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <title>Welcome to Sano!!</title>

    <!-- styles -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">

  </head>
  <body>
    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/">Sano</a>
        </div>
        <div class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            {% if not session.logged_in %}
              <li><a href="{{ url_for('') }}">Signup</a></li>
            {% else %}
              <li><a href="{{ url_for('') }}">Signout</a></li>
            {% endif %}
          </ul>
          {% if session.logged_in %}
          <ul class="nav navbar-nav navbar-right">
            <li><a>Welcome, {{username}}. </a></li>
          </ul>
          {% endif %}
        </div>
      </div>
    </div>

    <div class="container">
      <div class="content">

        {% for message in get_flashed_messages() %}
          <div class="alert alert-success">{{ message }}</div>
        {% endfor %}

        {% if error %}
          <div class="error"><strong>Error:</strong>{{ error }}</div>
        {% endif %}

        {% block content %}
        {% endblock %}

      </div>

    </div>

    <!-- scripts -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>

  </body>
</html>
