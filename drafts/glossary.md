{% for item in glossary_list %}

- {{ item.term }}: {{ item.definition }}
  {% endfor %}
