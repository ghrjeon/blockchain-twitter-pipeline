/*
    Union tables and order by date.
*/

{% macro union_date(tables, ascending=true) %}
    select * from (
        {% for table in tables %}
            select * from {{ table }}
            {% if not loop.last %}
                union all
            {% endif %}
        {% endfor %}
    )
    {% if ascending %}
        order by date
    {% else %}
        order by date desc
    {% endif %}
{% endmacro %}

